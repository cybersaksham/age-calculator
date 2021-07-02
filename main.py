from tkinter import *
from datetime import datetime
from tkcalendar import Calendar


class GUI(Tk):
    def __init__(self, title="Window", width=200, height=200, bg="white", resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()

    def stop(self):
        self.destroy()


def find_diff():
    year, month, day = str(cal.selection_get()).split("-")
    dob = datetime(day=int(day), month=int(month), year=int(year))
    time_now = datetime.now()
    time_diff = time_now - dob
    str_label = str(time_diff.days) + " Days"
    if time_diff.days < 0:
        str_label = "Invalid"
    lb = Label(root, text=str_label, bg=bg, width=10)
    lb.grid(row=2, column=1, pady=5)


if __name__ == '__main__':
    bg = "white"

    # Making Window
    root = GUI(title="Age Calculator", width=271, height=270)

    msg = Label(root, text="Enter your DOB", bg=bg, font=("Times", 10))
    msg.grid(row=0, column=0, columnspan=2)

    cal = Calendar(root, selectmode='day',
                   year=datetime.now().year, month=datetime.now().month,
                   day=datetime.now().day)
    cal.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

    day_btn = Button(root, text="Get Age", width=10, command=find_diff)
    day_btn.grid(row=2, column=0)

    # Starting Window
    root.start()
