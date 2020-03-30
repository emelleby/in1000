import tkinter as tk
from spillebrett import Spillebrett as S

class App:

    def __init__(self, master):
        # Create a new frame `frm_spill` to contain the Labels
        frm_spill = tk.Frame(master, relief=tk.SUNKEN, borderwidth=3)
        # Frame for text about generation and status
        frm_status = tk.Frame(master)
        # Frame for the buttons
        frm_btn = tk.Frame(master)
        # Pack the frames into the window
        frm_spill.pack()
        frm_status.pack()
        frm_btn.pack()

        # Generate labels for the board
        for idx, row in enumerate(labels._brett):    
            for i, state in enumerate(row):

                label = tk.Label(master=frm_spill, width=2, text=state.hentStatusTegn(), bg="green" if state._alive else "red")

                label.grid(row=idx, column=i, padx=2, pady=2)
        

        self.lbl_gen = tk.Label(frm_status, text=f"Generation {labels._gen}")
        self.lbl_gen.pack()

        self.button = tk.Button(
            frm_btn, text="QUIT", fg="red", command=frm_spill.quit
            )
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frm_btn, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print(f"hi there, everyone! + {labels._gen}")

    def update(self):
        pass


root = tk.Tk()
labels = S(3,4)
app = App(root)
S.oppdatering(labels)
root.mainloop()