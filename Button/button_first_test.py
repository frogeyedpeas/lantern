from gpiozero import Button

if __name__ == '__main__':
    button = Button(21)
    button.wait_for_press()
    print("Button was pressed!")
