import tkinter as tk

your_name = "Jhaira Mercado"
your_section = "BSIT-2A"
root = tk.Tk()
root.title(f"OOP LA29 {your_name} {your_section}")
root.geometry("400x300")
root.configure(bg="white")

name = tk.Label(font=100, text=(f"OOP LA29 {your_name} {your_section}"))
name.grid(row=0, column=0, padx=75, pady=90)

root.mainloop()