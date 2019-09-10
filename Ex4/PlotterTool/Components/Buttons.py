import tkinter 
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import json
from tkinter import filedialog

class transferButton:                  #Clase que contiene al boton para cargar jsons con los datos de transferencias
    def __init__(self, root, name,row,column,callback):
        self.root = root
        self.button = Button(root, text=name, width=20,command=self.openFile,bg="white") #Creo el boton con tkinter
        self.help = Button(root, text='?', command=self.openHelp,bg="white")
        self.row = row
        self.column =  column
        self.grid()
        self.callback = callback

    def grid(self):
        self.button.grid(row=self.row, column=self.column)
        self.help.grid(row=self.row, column=self.column+1)

    def invoke(self):
        self.button.invoke()

    def openHelp(self):
        messagebox.showinfo("Help",
        """
        {
            "hs1": {
                "num": [1],
                "den": [1, 600000],
                "legend": "prueba1"
            },
            "hs2": {
                "num": [1, 2, 3],
                "den": [4, 5, 6],
                "legend": "prueba2"
            },
            "hs3": {
                "num": [1, 2, 3],
                "den": [4, 5, 6],
                "legend": "prueba2"
            }
        }
        """
        )

    def openFile(self):
        self.root.fileName = filedialog.askopenfilename(filetypes = ( ("JSON files", ".json") , ("All Files", "*.*") )) #Pido archivo, guardo direccion
        retrieved_data = None
        if self.root.fileName.endswith(".json"): #valido que sea .json
            with open(self.root.fileName, 'r') as jsonFile:
                try:
                    retrieved_data = json.load(jsonFile)  # parseo el json y lo guardo
                except ValueError:
                    messagebox.showerror("Error", "Invalid JSON file. Try reformatting file.")
                except:
                    messagebox.showerror("Error", "An unknown error has ocurred.")
                
                #Sending data to the outer world
                self.callback(self.root.fileName)
                #self.test()
        elif not self.root.fileName:
            pass
        else:
            messagebox.showerror("Error", "Invalid filetype. Input a JSON file for transfer functions.")

    # def test(self):
    #     print(self.data)
    #     for h in self.data["hs"]:
    #         for key, value in h.items():
    #             print(key,value)
                #print(f"This is the key: {key} and this is the value: {value}")
        

class spiceButton: 
    def __init__(self, root,name, row, column, read_spice_func):
        self.root = root
        self.button = tkinter.Button(root, text=name, width=20,command=self.openFile,bg="white")  # Creo el boton con tkinter
        self.help = tkinter.Button(root, text='?', command=self.openHelp,bg="white")
        self.dataArray = []
        self.row = row
        self.column = column
        self.grid()
        self.read_spice_func = read_spice_func

    def grid(self):
        self.button.grid(row=self.row, column=self.column)
        self.help.grid(row=self.row, column=self.column+1)

    def invoke(self):
        self.button.invoke()

    def openHelp(self):
        messagebox.showinfo("Help", "Spice simulations must be exported as .txt files.")

    def openFile(self):
        self.root.fileName = filedialog.askopenfilename(filetypes = ( ("Plain text files", ".txt") , ("All Files", "*.*") )) #Pido archivo, guardo direccion
        if self.root.fileName.endswith(".txt"): #valido que sea .txt
            self.dataArray.append(self.root.fileName)
            self.read_spice_func(self.root.fileName)
            
        elif not self.root.fileName:
            pass
        else:
            messagebox.showerror("Error", "Invalid filetype. Input a plain text file for transfer functions.")

    def test(self):
        print(self.dataArray)

class measBodeButton: 
    def __init__(self, root,name, row, column,callback):
        self.root = root
        self.button = tkinter.Button(root, text=name,  width=20,command=self.openFile,bg="white")  # Creo el boton con tkinter
        self.help = tkinter.Button(root, text='?', command=self.openHelp,bg="white")
        self.row = row
        self.column = column
        self.callback = callback
        self.dataArray = []

        self.grid()

    def grid(self):
        self.button.grid(row=self.row, column=self.column)
        self.help.grid(row=self.row, column=self.column+1)

    def invoke(self):
        self.button.invoke()

    def openHelp(self):
        messagebox.showinfo("Help", "Manual measurements are to be input in .xlsx extension files.")

    def openFile(self):
        self.root.fileName = filedialog.askopenfilename(filetypes = ( ("Excel files", ".xlsx") , ("All Files", "*.*") )) #Pido archivo, guardo direccion
        if self.root.fileName.endswith(".xlsx"): #valido que sea .txt
            self.dataArray.append(self.root.fileName)
            self.callback(self.root.fileName)
        elif not self.root.fileName:
            pass
        else:
            messagebox.showerror("Error", "Invalid filetype. Input an excel table file for manual measurements.")

    def test(self):
        print(self.dataArray)

class oscilloscopeButton: 
    def __init__(self, root,name, row, column,callback):
        self.root = root
        self.button = tkinter.Button(root, text=name,  width=20,command=self.openFile,bg="white")  # Creo el boton con tkinter
        self.help = tkinter.Button(root, text='?', command=self.openHelp,bg="white")
        self.row = row
        self.column = column
        self.callback = callback
        self.dataArray = []

        self.grid()

    def grid(self):
        self.button.grid(row=self.row, column=self.column)
        self.help.grid(row=self.row, column=self.column+1)

    def invoke(self):
        self.button.invoke()

    def openHelp(self):
        messagebox.showinfo("Help", "Oscilloscope measurement are meant to be input raw as .CSV")

    def openFile(self):
        self.root.fileName = filedialog.askopenfilename(filetypes = ( ("Excel files", ".CSV") , ("All Files", "*.*") )) #Pido archivo, guardo direccion
        if self.root.fileName.endswith(".csv"): #valido que sea .txt
            self.dataArray.append(self.root.fileName)
            self.callback(self.root.fileName)
        elif not self.root.fileName:
            pass
        else:
            messagebox.showerror("Error", "Invalid filetype. Input an excel table file for manual measurements.")

    def test(self):
        print(self.dataArray)