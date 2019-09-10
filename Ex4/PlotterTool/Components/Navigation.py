import tkinter as tk
from Components.Buttons import transferButton, spiceButton, measurementsButton
from Components.DisplaySignals import DisplaySignals

class Navigation(tk.Frame):
    def __init__(self,master,load_spice_signals):
        self.load_spice_signals = load_spice_signals
        
        self.master = master
        tk.Frame.__init__(self,self.master)
        self.configure_nav()
        self.create_nav_view()

    def configure_nav(self):
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.config(bg="green",width=300)

    def create_nav_view(self):
        #Ponemos los botones de carga
        self.spiceButton = spiceButton(self,"LTSPICE", 1, 0, self.load_spice_signals)
        self.transButton = transferButton(self,"Transfer H(s)",2, 0, lambda:print("Hola"))
        self.measButton = measurementsButton(self,"Mediciones",3, 0, lambda:print("Hola"))
