import tkinter as tk
from Components.Signal import Signal
class DisplaySignals(tk.Frame):

    def __init__(self,master,controller):
        self.master = master
        self.controller = controller
        
        tk.Frame.__init__(self,self.master)
        self.signal_components = []
        self.configure()
        self.create_view()
        
    def configure(self):
        self.grid(row=6,column=0)
        self.config(bg="green",width=300)
        
    def create_view(self):
        tk.Label(self,text="hola", width=20).grid(row=6,column=0)
        tk.Label(self,text="hola", width=20).grid(row=7,column=0)
        tk.Label(self,text="hola", width=20).grid(row=8,column=0)
    
    def update_signals(self):

        for row, signal in enumerate(self.controller.signals):
            self.signal_components.append(Signal(self,signal,row))
        
        print(f'El largo de los signal_components es {len(self.signal_components)}')
        print(self.signal_components[0].check_visible==self.signal_components[1].check_visible)

