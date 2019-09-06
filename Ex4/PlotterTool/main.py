import tkinter as tk

from Components.Buttons import *
from Components.Signal import Signal
from Components.Plot import Plot

from Utils.Brain import Brain

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk as toolbar
from matplotlib.figure import Figure

def main():
    #Create the window
    root = tk.Tk()
    root.geometry("800x800")

    #Initialize state_manager
    state_manager = Brain() 
    #The loaded Signals objects will be stored here
    available_signals = [ ]

    #Loads LTSpice data from the simulation files
    #Maneja la carga de datos desde el archivo LTSpice. Carga los archivos e inicializa los objetos Signal
    row_offset = 7
    def pre_render_set_up(loaded_signals):
        offset = len(state_manager.signals)
         # #Add Signals to Nav Bar with the proper initial state
        for row, signal in enumerate(loaded_signals):
            available_signals.append(Signal(nav,signal,row+offset+row_offset))

            if timeCheckVar1.get() == True:
                if available_signals[row+offset].get_type() == "MAG"  or available_signals[row+offset].get_type() == "PHA":
                    available_signals[row+offset].block_cb()
                elif available_signals[row+offset].get_type() == "TIME":
                    available_signals[row+offset].unblock_cb()

            if freqCheckVar2.get() == True:
                if available_signals[row+offset].get_type() == "MAG"  or available_signals[row+offset].get_type() == "PHA":
                    available_signals[row+offset].unblock_cb()
                elif available_signals[row+offset].get_type() == "TIME":
                    available_signals[row+offset].block_cb()

    def spice_callback(path):
        state_manager.loaded_spice_paths.append(path)
        loaded_signals = state_manager.lt_parser.parse(path)
        pre_render_set_up(loaded_signals)
        state_manager.signals += loaded_signals

    def hs_callback(path):
        state_manager.loaded_hs.append(path)
        loaded_signals = state_manager.hs_parser.parse(path)
        pre_render_set_up(loaded_signals)
        state_manager.signals += loaded_signals

    def manual_callback(path):
        state_manager.loaded_hs.append(path)
        loaded_signals = state_manager.manual_parser.parse(path)
        pre_render_set_up(loaded_signals)
        state_manager.signals += loaded_signals
        
    def osc_callback(path):
        state_manager.osc_paths.append(path)
        loaded_signals = state_manager.osc_parser.parse(path)
        pre_render_set_up(loaded_signals)
        state_manager.signals += loaded_signals
               
    #Define how to perform a secure exit
    def exitFunction():
        # funciones de tkinter que administran que debe suceder cuando salimos del programa
        root.quit()
        root.destroy()
   
    root.protocol('WM_DELETE_WINDOW', exitFunction)
    #Set App title 
    root.title("PlotterTool TC 2019")
    root.minsize(width=700, height=500)
    root.geometry("800x600")
    
    #Master Frame
    master = tk.Frame(root)
    master.pack(side="top", fill="both", expand=True)
    master.config(bg="#f2620d")
    
    #Navigation Bar
    nav = tk.Frame(master)
    nav.pack(side=tk.LEFT, fill=tk.Y,anchor=tk.W, expand=False)
    nav.config(bg="#b04f93",width=340)
    logo = tk.Label(nav,text="PlotterTool TC 2019 G3",width=60,height=2,anchor=tk.CENTER)
    logo.config(font=("Verdana", 8))
    logo.grid(row=0,column=0,pady=2,columnspan=2)
    #Ponemos los botones de carga
    spiceBtn = spiceButton(nav,"Load LTspice Files", 1, 0, spice_callback)
    transBtn = transferButton(nav,"Load Transfer H(s)",2, 0, hs_callback)
    measBtn = measBodeButton(nav,"Load Meas",3, 0, manual_callback)
    oscBtn = oscilloscopeButton(nav,"Load Osciloscope",4, 0, osc_callback)
    
    
   #DOMAIN SELECTION
    timeCheckVar1 = tk.IntVar()
    freqCheckVar2 = tk.IntVar()
    time_domain_btn = None
    freq_domain_btn = None

    def change_to_freq():
        time_domain_btn.deselect()
        freq_domain_btn.select()
        for signal in available_signals:
            if signal.get_type() == "MAG"  or signal.get_type() == "PHA":
                signal.unblock_cb()
            elif signal.get_type() == "TIME":
                signal.block_cb()                 
    
    def change_to_time():
        freq_domain_btn.deselect()
        time_domain_btn.select()

        for signal in available_signals:
            if signal.get_type() == "MAG"  or signal.get_type() == "PHA":
                signal.block_cb()
            elif signal.get_type() == "TIME":
                signal.unblock_cb()


    domain_frame = tk.Frame(nav)
    domain_frame.config(bg="#9fd52a")
    domain_frame.grid(row=5,column=0,pady=5)

    domain_select_label = tk.Label(domain_frame,text="Choose a domain",width=30,bg="white",anchor=tk.CENTER)
    domain_select_label.grid(row=1,column=0,columnspan=2,pady=10)
    time_domain_btn = tk.Checkbutton(domain_frame, variable=timeCheckVar1, text="Time",justify=tk.CENTER,onvalue = 1, offvalue = 0,command=change_to_time, bg="white")
    freq_domain_btn = tk.Checkbutton(domain_frame,variable=freqCheckVar2, text="Frequency",justify=tk.CENTER,onvalue = 1, offvalue = 0, command=change_to_freq, bg="white")
    time_domain_btn.grid(row=2,column=0,padx=3,pady=4)
    freq_domain_btn.grid(row=2,column=1,padx=3,pady=4)

    #Label Frame
    labels_frame = tk.Frame(nav)
    labels_frame.config(bg="red")
    labels_frame.grid(row=5,column=1,pady=5)

    #Xlabel
    xlabel_lab = tk.Label(labels_frame,text="xlabel",bg="white")
    xlabel_lab.grid(row=1,column=0)
    xlabel_entry = tk.Entry(labels_frame)
    xlabel_entry.grid(row=1,column=1)
    #Ylabel
    ylabel_lab = tk.Label(labels_frame,text="ylabel",bg="white")
    ylabel_lab.grid(row=2,column=0)
    ylabel_entry = tk.Entry(labels_frame)
    ylabel_entry.grid(row=2,column=1)
    #Title
    title_plot = tk.Label(labels_frame,text="Title",bg="white")
    title_plot.grid(row=3,column=0)
    title_entry = tk.Entry(labels_frame)
    title_entry.grid(row=3,column=1)
    
    #Initial state
    freq_domain_btn.select()

    # Plotttting    
    
    #https://stackoverflow.com/questions/28493106/tkinter-frame-doesnt-fill-remaining-space
    plot_frame = tk.Frame(master)
    plot_frame.pack(anchor=tk.N,fill=tk.BOTH,expand=True,side=tk.TOP)
    plot_frame.config(bg="green")
    plotting_frame = Plot(plot_frame) 
    plotting_frame.set_frequency_domain_plot()

    def update_plot():
        MAG = False
        PHA = False
        TIME = False

        plotting_frame.clear()
        plotting_frame.ax1.set_title(title_entry.get())
        plotting_frame.plt.grid(True,which='major')
        
        #Plot Time domain Signals
        if timeCheckVar1.get() == True:
            plotting_frame.set_time_domain_plot(xlabel_entry.get(),ylabel_entry.get())
            for signal in available_signals:
                if signal.is_visible() and signal.get_type()=="TIME":
                    TIME = True   
                    plotting_frame.plot_time(signal.get_x(),signal.get_y(),signal.name.get(),signal.get_color(),signal.get_marker())

        #Plot frequency domain Signals
        elif freqCheckVar2.get() == True:
            plotting_frame.set_frequency_domain_plot()
            for signal in available_signals:
                print(signal.combo.get())
                if signal.is_visible() and signal.get_type() == "PHA":
                    PHA = True
                    plotting_frame.plot_pha(signal.get_x(),signal.get_y(),signal.name.get(),signal.get_color(),signal.get_marker())
                elif signal.is_visible() and signal.get_type() == "MAG":
                    MAG = True
                    plotting_frame.plot_mag(signal.get_x(),signal.get_y(),signal.name.get(),signal.get_color(),signal.get_marker())
        
        plotting_frame.draw(TIME,PHA,MAG)
        
    #Fits graph better into the screen
    def update_screen():
        update_plot()
        update_plot()

    
    graph_btn = tk.Button(nav,text="Update Plot",command=update_screen)
    graph_btn.invoke()
    graph_btn.invoke()
    graph_btn.grid(row=6,column=0, columnspan=3)
    

    root.mainloop()



if __name__ == "__main__":
    main()