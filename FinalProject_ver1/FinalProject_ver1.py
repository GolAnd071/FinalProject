import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename

import pygame

from PIL import Image
import numpy as np

import waterdetect

import Algorithm


class Main():
    def __init__(self):
        ''' Entry point of the programm '''
        self.root = tk.Tk()
        self.screen = pygame.display.set_mode((600, 600))
        self.screen.fill(pygame.Color(0, 0, 0))
        pygame.display.init()
        pygame.display.update()
        print('Message: Windows created.')
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()

        # Variables creation
        self.water_map = None
        self.fig = None
        self.mode = tk.StringVar()
        self.in_dir = tk.StringVar()
        self.out_dir = tk.StringVar()
        self.prod_type = tk.StringVar()
        self.step = tk.StringVar()

        # Tkinter vidgets creation
        ttk.Combobox(self.frame, textvariable=self.mode, values=['Batch', 'Single']).grid(column=0, row=2)
        ttk.Label(self.frame, textvariable=self.in_dir, width=16).grid(column=1, row=2)
        ttk.Button(self.frame, text='Choose input directory', command=lambda: self.in_dir.set(askdirectory())).grid(column=2, row=2)
        ttk.Label(self.frame, textvariable=self.out_dir, width=16).grid(column=3, row=2)
        ttk.Button(self.frame, text='Choose output directory', command=lambda: self.out_dir.set(askdirectory())).grid(column=4, row=2)
        ttk.Combobox(self.frame, textvariable=self.prod_type, values=['S2_THEIA', 'L8_USGS', 'S2_L1C', 'S2_S2COR']).grid(column=5, row=2)
        ttk.Button(self.frame, text='Detect water', command=lambda: self.detect_water()).grid(column=6, row=2)
        ttk.Button(self.frame, text='Show image', command=lambda: self.render_image()).grid(column=6, row=3)
        ttk.Button(self.frame, text='Choose coastline', command=lambda: self.choose_coastline()).grid(column=0, row=3)
        ttk.Entry(self.frame, textvariable=self.step).grid(column=1, row=3)
        ttk.Button(self.frame, text='Make broken line', command=lambda: self.brake_line()).grid(column=2, row=3)

        # Main loop
        self.root.mainloop()

    def detect_water(self):
        ''' Neural network that detects water on the satellite product '''
        if (self.mode == '') or (self.in_dir == '') or (self.out_dir == '') or (self.prod_type == ''):
            # If arguments are invalid
            print('Error: Arguments for water detection are invalid.')
        else:
            # Water detection
            print('Message: Water detection started.')
            self.water_map = waterdetect.DWWaterDetect.run_water_detect(input_folder=self.in_dir.get(),
                                                                        output_folder=self.out_dir.get(), 
                                                                        product=self.prod_type.get(),
                                                                        single_mode=True if self.mode.get() == 'Single' else False)
            print('Message: Water detection ended.')

    def choose_coastline(self):
        ''' Working with algorithm '''
        print('Message: Choosing coastline started.')
        for i in range(10980):
             if self.water_map.water_mask[0][i] == 0:
                 sp = (0, i)
                 break
        self.cstln = Algorithm.Coastline(sp, 10980, self.water_map.water_mask)
        self.cstln.create_line()
        print('Message: Choosing coastline ended.')

    def brake_line(self):
        ''' Creating class BrokenLine '''
        print('Message: Braking line started.')
        self.brkln = Algorithm.BrokenLine(int(self.step.get()), self.cstln.coords)
        self.brkln.create_line()
        print('Message: Braking line ended.')

    def render_image(self):
        ''' Rendering final image '''
        print('Message: Rendering started.')
        self.matrix = [[(0, (1 - abs(self.water_map.water_mask[i][j])) * 255, abs(self.water_map.water_mask[i][j]) * 255) for j in range(10980)] for i in range(10980)]

        for i, j in self.cstln.coords:
            self.matrix[i][j] = (255, 0, 0)

        im = Image.fromarray(np.uint8(self.matrix))
        im.save('image1.png')

        surf = pygame.Surface((10980, 10980))
        img = pygame.image.load('image1.png')

        img_rect = img.get_rect(bottomright=(10980, 10980))
        surf.blit(img, img_rect)
        if self.brkln.island:
            rng = range(len(self.brkln.vertices))
        else:
            rng = range(1, len(self.brkln.vertices))
        for i in rng:
            pygame.draw.line(surf, (255, 255, 0), (self.brkln.vertices[i-1][1], self.brkln.vertices[i-1][0]), (self.brkln.vertices[i][1], self.brkln.vertices[i][0]), width=50)
        surf = pygame.transform.scale(surf, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(surf, (0, 0))
        pygame.display.update()
        print('Message: Rendering ended.')


app = Main()
