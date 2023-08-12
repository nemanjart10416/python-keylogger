from pynput.mouse import Listener
import win32gui

def get_active_window_title():
    active_window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(active_window)
    return window_title

def on_click(x, y, button, pressed):
    if not pressed:  # Check if the button is released
        window_title = get_active_window_title()
        print(f"\n[{window_title}]\n")

with Listener(on_click=on_click) as listener:
    listener.join()