import tkinter as tk
from spillebrett import Spillebrett as S

"""
def ruter(rader, kolonner):


    # lag en nøstet liste
    brett = []
    # counter = 0
    for rad in range(rader):
        rad = []
        for kolonne in range(kolonner):
            rad.append("O")

        brett.append(rad)
    return brett
"""

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Spillebrett")

# Create a new frame `frm_spill` to contain the Label
# and Entry widgets for entering address information.
frm_spill = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_spill.pack()

# List of field labels
labels = S(13,33)
"""
[
    ["dead", "alive", "dead"],
    ["dead", "dead", "alive"],
    ["alive", "alive", "dead"]
]
"""
# Loop over the list of field labels
for idx, row in enumerate(labels):
    
    for i, state in enumerate(row):
        # Create a LabelFrame widget with the text from the labels list or a frame and then a label
        frm_cell = tk.Frame(master=frm_spill, width=25, height=25)
        frm_cell.grid(row=idx, column=i, padx=2, pady=2)
        label = tk.Label(master=frm_cell, width=2, text=state, bg="red" if state == "." else "green")
        # Use the grid geometry manager to place the Label and
        # Entry widgets in the row whose index is idx
        label.pack() #, sticky="e")
        # frm_spill.columnconfigure(i, minsize=60)

# Frame for text about generation and status
frm_status = tk.Frame()
frm_status.pack(fill=tk.X)

lbl_gen = tk.Label(master=frm_status, text="Generation X")
lbl_gen.pack()


# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
btn_submit = tk.Button(master=frm_buttons, text="Stop")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Run")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

# Start the application
window.mainloop()