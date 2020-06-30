import mido
from pynput.keyboard import Key, Controller
import argparse

parser = argparse.ArgumentParser(description="Push-to-talk using a midi sustain pedal.")
parser.add_argument("--use-space", dest="use_space", action="store_true")
parser.add_argument("--use-keyboard-shortcut", dest="use_space", action="store_false")
parser.set_defaults(use_space=True)
args = parser.parse_args()

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
                    if args.use_space:
                        keyboard.press(Key.space)
                    else:
                        toggle_shortcut()
                    pressed = True
            else:
                if pressed:
                    if args.use_space:
                        keyboard.release(Key.space)
                    else:
                        toggle_shortcut()
                    pressed = False
