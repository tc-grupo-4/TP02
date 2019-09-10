from tkinter import ttk
import tkinter as tk
from tkinter.colorchooser import *
import numpy as np
class Signal(tk.Frame):
    def __init__(self,master,signal_data,row):
        tk.Frame.__init__(self,master)
        self.grid(row=row,column=0,columnspan=5,padx=2)
        self.signal_data = signal_data
        self.visible = False
        self.signal_toggle = tk.Button(self,text=self.signal_data.columns[0],width=10,command=self.toggle_visible,justify=tk.RIGHT)
        self.signal_toggle.grid(row=row,column=0,pady=2)
        self.signal_toggle.config(bg ="white")
        #Enter signals name
        self.name = tk.Entry(self)
        self.name.grid(row=row,column=2,padx=2)
        self.trash_icon = tk.PhotoImage(file="Assets\img\icons8-trash-can-26.png")
        self.delete_btn = tk.Button(self,image=self.trash_icon, command=self.delete)
        self.combo = ttk.Combobox(self,width=10)
        self.combo.grid(row=row, column=3)
        self.markers = ["None","o", ".", "s", "X"]
        self.combo["values"] = ["None","o", ".", "s", "X","_"]
        self.delete_btn.grid(row=row,column=5,pady=2)       
        self.type = None
        self.set_type()
        self.color = "default"
        self.colBtn = tk.Button(self,text='Select Color', command=self.getColorDialog)
        self.colBtn.grid(row=row,column=4,pady=2)
    
    def get_marker(self):
        return self.combo.get()

    def getColorDialog(self):
        color = askcolor() #Return RGB and Hexadecimal color code representation of the choosen color
        self.color = color[1]
        self.colBtn.config(bg=self.color)

    def get_color(self):
        return self.color

    def delete(self):
        self.grid_forget()
        self.signal_toggle.grid_forget()
        self.name.grid_forget()
        self.delete_btn.grid_forget()
        self.combo.grid_forget()
        self.signal_data.index = np.zeros(len(self.signal_data.index))
        self.signal_data[0] = np.zeros(len(self.signal_data.index))
        self.hide()

    def set_type(self):
        #Perform this operation to know how to draw
        if "MAG" in self.signal_data.columns[0]:
            self.type = "MAG"
        elif "PHA" in self.signal_data.columns[0]:
            self.type = "PHA"
        else:
            self.type = "TIME"

    def get_type(self):
        return self.type

    def block_cb(self):
        self.signal_toggle.config(state=tk.DISABLED)
        
    def unblock_cb(self):
        self.signal_toggle.config(state=tk.NORMAL)

    def toggle_visible(self):
        self.visible = not self.visible
        if self.visible == True:
            self.signal_toggle.config(bg = "#1ae559")
        else:
            self.signal_toggle.config(bg ="white")
    
    def hide(self):
        self.visible = False

    def is_visible(self):
        return self.visible
        
    def get_name(self):
        return self.signal_data.columns[0]
    
    def get_x(self):
        return np.array(self.signal_data.index)
        
    def get_y(self):
        return np.array(self.signal_data.iloc[:,0].values)