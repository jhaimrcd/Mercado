import tkinter as tk

root = tk.Tk()
root.title("Jhai")
root.geometry("500x500")
root.configure(bg="light blue")

name = tk.Entry(root)
name.grid(row=0, column=0, padx=20)

counter = 1
def display_text():
    global counter
    print(f"{counter}. {name.get()}")
    counter += 1

button = tk.Button(root, text="Run", command=display_text)
button.grid(row=0, column=1, padx=20, pady=20)

root.mainloop()