import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader
from tkinter import filedialog, messagebox


merger = PdfFileMerger()


def open_file():
    filepath = askopenfilename(multiple=True, filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])
    for f in filepath:
        listbox.insert(END, f)

    if listbox.size() >= 2 and button_merge['state'] == "disabled":
        button_merge["state"] = "normal"


def merge_pdfs():
    output_filename = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save File", filetypes=(('pdf file', '*.pdf'),))

    for i in range(listbox.size()):
        merger.append(PdfFileReader(open(listbox.get(i), "rb")))

    merger.write(output_filename)
    delete_all()
    messagebox.showinfo(title="Message", message="Done !")
    window.update_idletasks()


def delete():
    listbox.delete(ANCHOR)
    if listbox.size() < 2:
        button_merge["state"] = "disabled"


def delete_all():
    listbox.delete(0, END)
    listbox.config(height=listbox.size())
    button_merge["state"] = "disabled"


window = Tk()
window.title("PDF Marge")
window.geometry("500x400")

listbox = Listbox(window,
                  bg="#f7ffde",
                  width=50,
                  )
listbox.pack()
frame = Frame(window, bd=3)
open_label = Label(frame, text="Please choose PDFs to join: (2 and above)")
open_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
open_button = Button(frame, text="Open file(s)", command=lambda: open_file())
open_button.grid(row=1, column=0, sticky="ew", padx=5)
frame.pack()

frame2 = Frame(window, bd=3)
button_merge = Button(frame2,
                      text="Merge PDF",
                      state="disabled",
                      command=merge_pdfs)
button_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=2)
delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()
button_delete_all = Button(window, text="Delete All", command=lambda:delete_all())
button_delete_all.pack()
frame2.pack()

exit_button = Button(window, text="Exit", command=window.destroy, bd=2)
exit_button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.FALSE)

if __name__ == "__main__":
    window.mainloop()

