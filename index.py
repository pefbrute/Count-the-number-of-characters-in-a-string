import pyautogui
import pyperclip
import time
import subprocess
import tempfile

def copy_text():
    """Copies the currently selected text to the clipboard."""
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait a bit for the text to be copied to the clipboard

def get_text_from_clipboard():
    """Retrieves text from the clipboard."""
    return pyperclip.paste()

def count_characters(text):
    """Counts the number of characters in the given text."""
    return len(text)

def open_gedit_and_display_count(count):
    """Opens gedit and displays the given character count."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(f'Character count: {count}\n')
        tmp_file_path = tmp_file.name
    subprocess.run(['gedit', tmp_file_path])

copy_text()
text = get_text_from_clipboard()
char_count = count_characters(text)
open_gedit_and_display_count(char_count)
