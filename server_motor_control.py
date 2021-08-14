from flask import Flask, render_template, send_from_directory, Response, request
# from flask_socketio import SocketIO
from pathlib import Path
from capture import capture_and_save
from camera import Camera
import argparse, logging, logging.config, conf
import l298n_dc
import dc_motor 

logging.config.dictConfig(conf.dictConfig)
logger = logging.getLogger(__name__)

camera = Camera(fps=40)
camera.run()

app = Flask(__name__)
# app.config["SECRET_KEY"] = "secret!"
# socketio = SocketIO(app)

TOP_LEFT_MOTOR = dc_motor.dc_motor(EN1, PIN1, PIN2) 
TOP_RIGHT_MOTOR = dc_motor.dc_motor(EN2, PIN3, PIN4)
BACK_LEFT_MOTOR = dc_motor.dc_motor(EN3, PIN5, PIN6)
BACK_RIGHT_MOTOR = dc_motor.dc_motor(EN4, PIN7, PIN8) 

MECANUM_PLATFORM = dc_motor.mecanum(TOP_LEFT_MOTOR, TOP_RIGHT_MOTOR, BACK_LEFT_MOTOR, BACK_RIGHT_MOTOR) 


@app.after_request
def add_header(r):
	"""
	Add headers to both force latest IE rendering or Chrome Frame,
	and also to cache the rendered page for 10 minutes
	"""
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers["Cache-Control"] = "public, max-age=0"
	return r

@app.route("/")
def entrypoint():
	logger.debug("Requested /")
	return render_template("index.html")

@app.route("/r")
def capture():
	logger.debug("Requested capture")
	im = camera.get_frame(_bytes=False)
	capture_and_save(im)
	return render_template("send_to_init.html")

@app.route("/images/last")
def last_image():
	logger.debug("Requested last image")
	p = Path("images/last.png")
	if p.exists():
		r = "last.png"
	else:
		logger.debug("No last image")
		r = "not_found.jpeg"
	return send_from_directory("images",r)


def gen(camera):
	logger.debug("Starting stream")
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
			   b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

@app.route("/stream")
def stream_page():
        print(request)
        print("stream page called")
        logger.debug("Requested stream page")
        if "start_motor" in request.form:
                print("starting motor now")

        if "stop_motor" in request.form:
                print("stopping motor now")

        return render_template("stream.html")

@app.route("/video_feed")
def video_feed():
	return Response(gen(camera),
		mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/start")
def start_motor():
        l298n_dc.motor_go(l298n_dc.in1, l298n_dc.in2, True)
        response = "starting"
        return response, 200, {'Content-Type': 'text/plain'}

@app.route("/stop")
def stop_motor():
        l298n_dc.motor_stop(l298n_dc.in1, l298n_dc.in2)
        response = "stopping" 
        return response, 200, {'Content-Type': 'text/plain'}

if __name__=="__main__":
	# socketio.run(app,host="0.0.0.0",port="3005",threaded=True)
	parser = argparse.ArgumentParser()
	parser.add_argument('-p','--port',type=int,default=5000, help="Running port")
	parser.add_argument("-H","--host",type=str,default='0.0.0.0', help="Address to broadcast")
	args = parser.parse_args()
	logger.debug("Starting server")
	app.run(host=args.host,port=args.port)
