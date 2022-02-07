#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:57:21 2020

@author: andrzej łysko
andrzejlysko@gmail.com
"""

import treepoem
import progressbar
import time
from fpdf import FPDF
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import glob,os,time



licznik = pd.read_csv('licznik.txt', nrows=1, header = None)
print(licznik[0].iloc[0])
def multipage_simple():
    pdf=FPDF('P', 'mm', (26,12))
    pdf.set_font("Helvetica",'B',size=10)
    numer=int(a.get())
    start=numer
    zakres=int(b.get())
    liczniksave=zakres+licznik
    liczniksave.to_csv('licznik.txt', sep=' ', index=False, header=False)
    timestr = time.strftime("%Y_%m_%d-%H%M%S")
    prefix="UGDA."
    for i in progressbar.progressbar(range(zakres)):
        pdf.add_page()
        value="{:07}".format(numer)
        pdf.text(x=2, y=5, txt=prefix)
        pdf.text(x=0.5,y=9, txt=value)
        img = treepoem.generate_barcode(barcode_type='datamatrix', data=prefix+value,options={"eclevel": "H"})
        img.convert('1').save('qr'+str(numer)+'.gif')
        pdf.image('qr'+str(numer)+'.gif', x=14.2, y=0.25, w=11.5)
        numer+=1
    pdf.output("wydruk_26x12mm_"+timestr+'-s_'+str(start)+'-k_'+str(numer)+".pdf")
    for i in glob.glob("*.gif"):
        os.remove(i)
    tk.messagebox.showinfo("Wydruk", "Wydrukowano")

def close_window(): 
    master.destroy()    
    
if __name__ == '__main__':
    master = tk.Tk()
    master.title("Drukowanie etykiet")
    tk.Label(master, 
             text="Numer początkowy").grid(row=0)
    tk.Label(master, 
             text="Liczba etykiet").grid(row=1)
    a = tk.Entry(master)
    a.insert(0,licznik[0].iloc[0])
    b = tk.Entry(master)
    a.grid(row=0, column=1)
    b.grid(row=1, column=1)
    tk.Button(master, 
              text='Koniec', 
              command=close_window).grid(row=3, 
                                        column=0, 
                                        sticky=tk.W, 
                                        pady=4)
    tk.Button(master, text='Drukuj', command=multipage_simple).grid(row=3, column=1, sticky=tk.W, pady=4)
    tk.mainloop()
     

       


