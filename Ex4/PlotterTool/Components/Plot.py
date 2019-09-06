import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk as toolbar
from matplotlib.figure import Figure

#https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot/43439132#43439132
class Plot(tk.Frame):
    def __init__(self, master): 
        self.master = master
        tk.Frame.__init__(self,self.master)    
        self.graph = tk.Canvas(self.master)
        #Placing the canvas in place
        self.graph.place(x=50, y=20,width=900,height=600) 

        self.fig = Figure(figsize=(8,6.5))
        self.plt = self.fig.add_subplot(1,1,1) #los dos primeros parámetros le da una escala a la figura (mientras más grandes son los parámetros, mas chico será la figura). El tercero le da la posición en el self.window.
        self.ax1 = self.fig.gca()
        self.data_plt = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.data_plt._tkcanvas.pack(anchor=tk.N,fill=tk.BOTH,expand=True,side=tk.LEFT)
        
        self.ax2 = self.ax1.twinx()  # instantiate a second axes that shares the same x-axis

        self.fig.tight_layout()  # otherwise the right y-label is slightly clippe
        
        
        self.nav_tool = toolbar(self.data_plt, self.master)
        self.nav_tool.update()
        self.markers = ["o", ".", "s", "X"]
    
    #RECORDAR SECUENCIA!!
    def clear(self):
        self.ax1.reset_position()
        self.ax2.reset_position()
        self.plt.clear()
        self.ax1.cla()
        self.ax2.cla()

    def plot_time(self,x,y,legend,color,marker):
        if marker == "None" or marker not in self.markers: 
            if color == "default":
                self.plt.plot(x,y,label=legend)
            else:
                self.plt.plot(x,y,color=color,label=legend)
            self.plt.legend()
        elif marker in self.markers:
            if color == "default":
                self.plt.plot(x,y,label=legend,marker=marker)
            else:
                self.plt.plot(x,y,color=color,label=legend,marker=marker)
            self.plt.legend()

    def plot_mag(self,x,y,legend,color,marker):
        if marker == "None" or marker not in self.markers: 
            if color == "default":
                self.ax1.semilogx(x,y,label=legend)
            else:
                self.ax1.semilogx(x,y,color=color,label=legend)
            self.ax1.legend()
        elif marker in self.markers:
            if color == "default":
                self.ax1.semilogx(x,y,label=legend,marker=marker)
            else:
                self.ax1.semilogx(x,y,color=color,label=legend,marker=marker)
            self.ax1.legend()

    def plot_pha(self,x,y,legend,color,marker):
        if marker == "None" or marker not in self.markers: 
            if color == "default":
                self.ax2.semilogx(x,y,label=legend)
            else:
                self.ax2.semilogx(x,y,color=color,label=legend)
            self.ax2.legend()
        elif marker in self.markers:
            if color == "default":
                self.ax2.semilogx(x,y,label=legend,marker=marker)
            else:
                self.ax2.semilogx(x,y,color=color,label=legend,marker=marker)
            self.ax2.legend()

#https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot/43439132#43439132
    def draw(self,TIME,PHA,MAG):

        if MAG == True or TIME == True:
            # Shrink current axis's height by 10% on the bottom
            box = self.ax1.get_position()
            self.ax1.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

            # Put a legend below current axis
            self.ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
                fancybox=True, shadow=True, ncol=5)

        if PHA == True:
            # Shrink current axis's height by 10% on the bottom
            box = self.ax2.get_position()
            self.ax2.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

            # Put a legend below current axis
            self.ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
                fancybox=True, shadow=True, ncol=5)

        if PHA == True and MAG == True:
             # Shrink current axis's height by 10% on the bottom
            box = self.ax1.get_position()
            self.ax1.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

            # Put a legend below current axis
            self.ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                fancybox=True, shadow=True, ncol=5)
            
            self.ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

        self.ax1.relim()      # make sure all the data fits
        self.ax1.autoscale()
        self.ax2.relim()      # make sure all the data fits
        self.ax2.autoscale()
        self.data_plt.draw()
        self.fig.tight_layout()  # otherwise the right y-label is slightly clippe

    def set_time_domain_plot(self,xlabel,ylabel):
        # self.ax2.remove()
        self.ax2.set_yticklabels([])
        # self.ax2.set_xticklabels([])
        self.ax1.set_xlabel(xlabel)
        self.ax1.set_ylabel(ylabel)
        

    def set_frequency_domain_plot(self):
        # self.ax2 = self.ax1.twinx()  # instantiate a second axes that shares the same x-axis
        # self.fig.tight_layout()  # otherwise the right y-label is slightly clippe
        self.ax1.set_xlabel("$Hz$")
        self.ax1.set_ylabel("Magnitud Db")
        self.ax2.set_ylabel("$Fase °$")
        # self.fig.tight_layout()  # otherwise the right y-label is slightly clippe

    def set_mag_plot(self):
        self.ax2.set_yticklabels([])
        self.ax1.set_xlabel("$Hz$")
        self.ax1.set_ylabel("$Magnitud Db$")
    
    def set_pha_plot(self):
        self.ax1.set_ylabel("$Fase °$")
        self.ax1.set_xlabel("$Hz$")

#matplotlib          2.2.3
