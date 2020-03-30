import tkinter as tk
from spillebrett import Spillebrett as S



# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Spillebrett")

# Create a new frame `frm_spill` to contain the Label
# and Entry widgets for entering address information.
frm_spill = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_spill.pack()

# List of field labels
# S(3,3)
labels = S(3,4)


# print(labels._brett[0][0])
# Bring the cell to life
# labels._brett[0][0]._alive = True
# Frame for text about generation and status
frm_status = tk.Frame()

label = tk.Label(master=frm_spill, width=2)
lbl_gen = tk.Label(master=frm_status, text=f"Generation {labels._gen}")
    
lbl_alive = tk.Label(master=frm_status, text=f"Levende celler er: {labels.finnAntallLevende()}")
# Loop over the list of field labels
for idx, row in enumerate(labels._brett):
    
    for i, state in enumerate(row):

        label = tk.Label(master=frm_spill, width=2, text=state.hentStatusTegn(), bg="green" if state._alive else "red")

        label.grid(row=idx, column=i, padx=2, pady=2)

def update():

    # labels = S.labels
    global label
    global lbl_gen
    global lbl_alive
    # Loop over the list of field labels
    for idx, row in enumerate(labels._brett):
        
        for i, state in enumerate(row):
            # Create a LabelFrame widget with the text from the labels list or a frame and then a label
            # frm_cell = tk.Frame(master=frm_spill, width=25, height=25)
            # frm_cell.grid(row=idx, column=i, padx=2, pady=2)
            label.grid_forget()
            label = tk.Label(master=frm_spill, width=2, text=state.hentStatusTegn(), bg="green" if state._alive else "red")
            # Use the grid geometry manager to place the Label and
            # Entry widgets in the row whose index is idx
            label.grid(row=idx, column=i, padx=2, pady=2) #.pack() #, sticky="e")
            # frm_spill.columnconfigure(i, minsize=60)
    lbl_gen = tk.Label(master=frm_status, text=f"Generation {labels._gen}")
    
    lbl_alive = tk.Label(master=frm_status, text=f"Levende celler er: {labels.finnAntallLevende()}")


#lbl_gen = tk.Label(master=frm_status, text=f"Generation {labels._gen}")
lbl_gen.pack()
#lbl_alive = tk.Label(master=frm_status, text=f"Levende celler er: {labels.finnAntallLevende()}")
lbl_alive.pack()
frm_status.pack(fill=tk.X)

# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
btn_stop = tk.Button(master=frm_buttons, text="Stop", command=window.quit)
btn_stop.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_run = tk.Button(master=frm_buttons, text="Run", command=lambda:[S.oppdatering(labels), update()])
btn_run.pack(side=tk.RIGHT, ipadx=10)

# Update window

# Start the application
window.mainloop()

# Terminal Output
print()
for rad in labels._brett:
    for celle in rad:
        print(celle.hentStatusTegn(), end='')
    print("\n")