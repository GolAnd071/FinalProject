import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import waterdetect

class Main():
    def __init__(self):
        self.root = tk.Tk()
        print('Message: Window created.')
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()

        self.water_map = None
        self.fig = None

        self.mode = tk.StringVar()
        self.in_dir = tk.StringVar()
        self.out_dir = tk.StringVar()
        self.prod_type = tk.StringVar()

        ttk.Combobox(self.frame, textvariable=self.mode, values=['Batch', 'Single']).grid(column=0, row=2)

        ttk.Label(self.frame, textvariable=self.in_dir, width=16).grid(column=1, row=2)
        ttk.Button(self.frame, text='Choose input directory', command=lambda:self.in_dir.set(askdirectory())).grid(column=2, row=2)

        ttk.Label(self.frame, textvariable=self.out_dir, width=16).grid(column=3, row=2)
        ttk.Button(self.frame, text='Choose output directory', command=lambda:self.out_dir.set(askdirectory())).grid(column=4, row=2)

        ttk.Combobox(self.frame, textvariable=self.prod_type, values=['S2_THEIA', 'L8_USGS', 'S2_L1C', 'S2_S2COR']).grid(column=5, row=2)

        ttk.Button(self.frame, text='Detect water', command=lambda:self.detect_water()).grid(column=6, row=2)

        ttk.Button(self.frame, text='Show image', command=lambda:self.render_image(self.water_map.water_mask)).grid(column=6, row=3)

        self.root.mainloop()


    def detect_water(self):
        if (self.mode == '') or (self.in_dir == '') or (self.out_dir == '') or (self.prod_type == ''):
            print('Error: Arguments for water detection are invalid.')
        else:
            print('Message: Water detection started.')
            self.water_map = waterdetect.DWWaterDetect.run_water_detect(input_folder=self.in_dir.get(), output_folder=self.out_dir.get(), product=self.prod_type.get(), single_mode=True if self.mode.get() == 'Single' else False)
            print('Message: Water detection ended.')


    def render_image(self, matrix):
        print('Message: Rendering started.')
        self.fig = Figure(figsize=(0.05, 0.05), dpi=10980)
        self.fig.figimage(matrix)
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=0, row=0, columnspan=7)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(column=0, row=1, columnspan=7)
        print('Message: Rendering ended.')


app = Main()
