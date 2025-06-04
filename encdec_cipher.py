import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def run_cipher():
    text = message_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be a number.")
        return

    mode = mode_var.get()
    if mode == "Encrypt":
        output = encrypt(text, shift)
    elif mode == "Decrypt":
        output = decrypt(text, shift)
    else:
        output = "Invalid mode."

   
    result_label.config(text="Successfully Completed\nResult: " + output)

root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter the text:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack()

tk.Label(root, text="Enter the Shift Value:").pack(pady=5)
shift_entry = tk.Entry(root, width=10)
shift_entry.pack()

mode_var = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt").pack()
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt").pack()

tk.Button(root, text="Submit", command=run_cipher).pack(pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

root.mainloop()
