import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x400+100+50")
root.configure(bg="#111")

label = tk.Label(root, font=("CourieDejaVu Sans Mono", 50, "bold"), bg="#000", fg="#0ff")
label.pack(expand=True)

def tick():
    now = datetime.now()
    label.config(text=now.strftime("%d %b %Y\n%H:%M:%S"))
    root.after(1000 - now.microsecond // 1000, tick)

tick()
root.mainloop()


































































