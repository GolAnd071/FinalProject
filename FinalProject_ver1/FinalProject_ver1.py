from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from WaterDetection import *
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

mode = None
in_filename = None
out_filename = None
product_type = None
img = None


def open_input_file_dialog():
    global in_filename

    in_filename = StringVar()
    in_filename.set(askdirectory())


def open_output_file_dialog():
    global out_filename

    out_filename = StringVar()
    out_filename.set(askdirectory())


def detect_water_start():
    global mode
    global in_filename
    global out_filename
    global product_type
    global img

    wd = detect_water(mode.get(), in_filename.get(), out_filename.get(), product_type.get())
    # wd.water_mask - massive
    print("Detection has ended.\n")
    wd_ = [j * 255 for i in wd.water_mask for j in i]
    img_ = Image.fromarray(wd.water_mask)
    img_ = img_.resize(800, 600)
    imgTk_ = ImageTk.PhotoImage(img_)
    img.create_image(0, 0, image=imgTk_)
    print("Image has been showed.\n")


def main():
    global mode
    global in_filename
    global out_filename
    global product_type
    global img

    root = Tk()
    img = Canvas(root, width=800, height=600, bg="black")
    img.grid(column=0, row=0)
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    mode = StringVar()
    in_filename = StringVar()
    out_filename = StringVar()
    product_type = StringVar()
    ttk.Combobox(frm, textvariable=mode, values=["Batch", "Single"]).grid(column=0, row=1)

    ttk.Button(frm, text="Choose input directory", command=open_input_file_dialog).grid(column=2, row=1)

    ttk.Button(frm, text="Choose output directory", command=open_output_file_dialog).grid(column=4, row=1)
    ttk.Combobox(frm, textvariable=product_type, values=["S2_THEIA", "L8_USGS", "S2_L1C", "S2_S2COR"]).grid(column=5, row=1)
    ttk.Button(frm, text="Detect water", command=detect_water_start).grid(column=6, row=1)

    root.mainloop()
    print(mode.get(), in_filename.get(), out_filename.get(), product_type.get())


if __name__ == "__main__":
    main()
