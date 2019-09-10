from Utils.SpiceParser import SpiceParser
from Utils.HsParser import HsParser
from Utils.ManualBodeParser import ManualBodeParser
from Utils.OscParser import OscParser

from Components.Signal import Signal

class Brain:
    def __init__(self):
        
        #Store PATHS
        self.raw_hs = None #Parmas of the transfer functions
        self.spice_signals_paths = []
        self.measures_paths  = []
        self.osc_paths = []
        #LTspice Parser
        self.lt_parser = SpiceParser()
        self.hs_parser = HsParser()
        self.manual_parser = ManualBodeParser()
        self.osc_parser = OscParser()


        #Stored Signals individually
        self.loaded_hs = []
        self.loaded_spice_paths = []
        # self.loaded_meas = None

        #Stores the corresponding DataFrames for each signal
        self.signals = []

    def load_spice_signals(self,path):
        loaded_spice_paths += path
        # for signal in self.lt_parser.parse(path):
        #     print(signal.head())
        #     self.signals.append(signal)

    



# https://www.datacamp.com/community/tutorials/docstrings-python
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://www.tutorialspoint.com/python/tk_grid#
# https://www.tutorialspoint.com/python/tk_button.htm
# file:///C:/Users/Msrt/Downloads/Microelectronic%20Circuits%20by%20Sedra%20Smith%205th%20edition.pdf
# https://www.tutorialspoint.com/python/tk_button
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.tutorialspoint.com/python/tk_frame.htm