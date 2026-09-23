import tkinter as tk
from tkinter import messagebox

def check_even_odd():
    try:
        num = int(entry.get())
        if num % 2 == 0:
            messagebox.showinfo("Result", f"{num} is Even")
        else:
            messagebox.showinfo("Result", f"{num} is Odd")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

root = tk.Tk()
root.title("Even or Odd Checker")
root.geometry("500x350")

label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Check", command=check_even_odd)
button.pack(pady=10)

root.mainloop()


