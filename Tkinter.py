import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, what's your name?",
        fg="white",
        bg="darkred",
        width=20,
        height=2
        )

submit = tk.Button(
    text="Submit",
    fg="white",
    bg="skyblue",
    width= 10,
    height=1
)


naamInput = tk.Entry(
    fg="darkblue",
    bg="lightgreen"
)

greeting.pack()
naamInput.pack()
submit.pack()

window.wm_title("Wisam")

window.mainloop()