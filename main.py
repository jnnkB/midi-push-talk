import mido
from pynput.keyboard import Key, Controller

USE_SPACE = False

keyboard = Controller()


def toggle_shortcut():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.alt)
    keyboard.type("m")
    keyboard.release(Key.ctrl)
    keyboard.release(Key.alt)


pressed = False

with mido.open_input("USB MIDI cable Port 2") as inport:
    for msg in inport:
        if msg.type == "control_change" and msg.control == 64:
            if msg.value > 64:
                if not pressed:
                    if USE_SPACE:
                        keyboard.press(Key.space)
                    else:
                        toggle_shortcut()
                    pressed = True
            else:
                if pressed:
                    if USE_SPACE:
                        keyboard.release(Key.space)
                    else:
                        toggle_shortcut()
                    pressed = False
