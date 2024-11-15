import tkinter as tk

root = tk.Tk()
root.title("Jhai")
root.geometry("400x300")
root.configure(bg="light blue")

anime_title = "Campfire Cooking"
def display_text():
    print(f"My favorite anime is {anime_title}")

button = tk.Button(root, text="Run", command=display_text)
button.grid(row=0, column=0, padx=120, pady=30)

root.mainloop()