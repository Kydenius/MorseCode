import tkinter as tk
from tkinter import messagebox, Text, Scrollbar
import winsound
import time

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 'ß': '...--..',  # Representation for German 'ß'
    'Å': '.--.-',   # Representation for Swedish 'Å'
    'Ö': '---.',    # Representation for German/Finnish/Swedish 'Ö'
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    ' ': ' '  # Space
}
def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + ' '
    return morse

def morse_to_sound(morse_code):
    for char in morse_code:
        if char == '.':
            winsound.Beep(1000, 100)  # Short beep (100ms)
            time.sleep(0.1)  # Short pause after beep
        elif char == '-':
            winsound.Beep(1000, 300)  # Long beep (300ms)
            time.sleep(0.3)  # Short pause after beep
        elif char == ' ':
            time.sleep(0.3)  # Pause (300ms)

def on_convert_click():
    user_input = input_entry.get()
    morse_code = text_to_morse(user_input)
    morse_to_sound(morse_code)

def on_convert_click():
    user_input = input_entry.get()
    morse_code = text_to_morse(user_input)

    if vibrate_var.get():
        try:
            morse_to_sound(morse_code)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    if show_text_var.get():
        morse_output.delete(1.0, tk.END)
        morse_output.insert(tk.END, morse_code)


REVERSED_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def morse_to_text(morse_code):
    words = morse_code.split('  ')  # Split Morse code into words
    decoded_message = ''

    for word in words:
        letters = word.split()  # Split words into individual Morse code letters
        for letter in letters:
            if letter in REVERSED_MORSE_CODE_DICT:
                decoded_message += REVERSED_MORSE_CODE_DICT[letter]
        decoded_message += ' '  # Adds space after each word

    return decoded_message.strip()  # Removes trailing space

def on_decode_click():
    morse_code = morse_output.get(1.0, tk.END).strip()  # Get Morse code from morse_output Text widget
    decoded_text = morse_to_text(morse_code)
    decoded_output.delete(1.0, tk.END)  # Clear previous decoded texts
    decoded_output.insert(tk.END, decoded_text)  # Insert decoded texts

# GUI for the Morse Code App
root = tk.Tk()
root.title("Text to Morse Vibration")

label = tk.Label(root, text="Enter text:")
label.pack(pady=10)

input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=10)

# Checkboxes
vibrate_var = tk.IntVar()
vibrate_cb = tk.Checkbutton(root, text="Vibrate", variable=vibrate_var)
vibrate_cb.pack(pady=5)

show_text_var = tk.IntVar()
show_text_cb = tk.Checkbutton(root, text="Show as Text", variable=show_text_var)
show_text_cb.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=on_convert_click)
convert_button.pack(pady=20)

decode_button = tk.Button(root, text="Decode", command=on_decode_click)
decode_button.pack(pady=20)

# Text output for Morse code
morse_output = Text(root, height=5, width=40)
scroll = Scrollbar(root, command=morse_output.yview)
morse_output.configure(yscrollcommand=scroll.set)
morse_output.pack(pady=10)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Text output for decoded text
decoded_output_label = tk.Label(root, text="Decoded Text:")
decoded_output_label.pack(pady=5)
decoded_output = Text(root, height=5, width=40)
scroll_decoded = Scrollbar(root, command=decoded_output.yview)
decoded_output.configure(yscrollcommand=scroll_decoded.set)
decoded_output.pack(pady=10)
scroll_decoded.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()