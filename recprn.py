import tkinter as tk
from tkinterdnd2 import DND_TEXT, COPY, Tk
from win32printing import Printer

# pip install -r requirements
# pyinstaller -F .\recprn.py -w --additional-hooks-dir=.

def main():
    name = "POS-58"
    target_text = f"""\
Drop Text Here
--or--
Right Click To
Print To {name}"""

    def to_printer(text):
        font = {
            # "height": 8,  # 35 chars @ 8
            # "height": 10,  # 29 chars @ 10
            "height": fontsize.get(),  # 24 chars @ 12
            "faceName": "Consolas",
            # "strikeOut": True,
        }
        with Printer(printer_name=name, linegap=1) as printer:
            printer.text(text, font_config=font)

    def right_click(event):
        paste = win.clipboard_get()
        to_printer(paste)

    def drop_enter(event):
        event.widget.focus_force()
        return event.action

    def drop_position(event):
        return event.action

    def drop_leave(event):
        return event.action

    def drop(event):
        if event.data:
            to_printer(event.data)

        return event.action

    def drag_init(event):
        data = target['text']
        return (COPY, DND_TEXT, data)

    win = Tk()
    win.title("Munbyn")
    # win.overrideredirect(1) # will remove the top badge of window
    win.attributes('-toolwindow', True)
    # win.resizable(0,0)  # Remov minimize/maximize
    fontsize_label = tk.Label(text="Font:")
    #fontsize_label.pack()

    fontsize = tk.IntVar(win, 10)
    fontsize_widget = tk.Spinbox(from_=8, to=14, textvariable=fontsize, width=4)
    #fontsize_widget.pack()

    fontsize_label.grid(row=0, column=0)
    fontsize_widget.grid(row=0, column=1)

    target = tk.Label(text=target_text.lstrip())
    target.grid(row=1, columnspan=2)
    #target.pack()
    target.bind("<Button-3>", right_click)
    target.drop_target_register(DND_TEXT)
    target.dnd_bind('<<DropEnter>>', drop_enter)
    target.dnd_bind('<<DropPosition>>', drop_position)
    target.dnd_bind('<<DropLeave>>', drop_leave)
    target.dnd_bind('<<Drop>>', drop)
    target.drag_source_register(DND_TEXT)
    target.dnd_bind('<<DragInitCmd>>', drag_init)

    win.mainloop()


if __name__ == "__main__":
    main()
    print("Done\n")
