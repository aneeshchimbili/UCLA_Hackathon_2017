import tkinter

INITIAL_HEIGHT = 500
INITIAL_WIDTH = 500
UNIV_FONT = ('Comic Sans', 12)

root = tkinter.Tk()
root.title("LAHacks 2017")

# Text Field (Zip Code)
zip_code_field = tkinter.StringVar(master = root)
zip_code = tkinter.Entry(root, width = 50)
zip_code_1 = tkinter.Label(master = root, font = UNIV_FONT, textvariable = zip_code_field)
zip_code_1.grid(row=0, column=0)





root.mainloop()
