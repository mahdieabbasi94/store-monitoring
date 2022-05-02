"""laus deo
project name: store monitoring
project description: simulate a smart store and monitor it
module name: sensors
module description: simulate sensors used in this project
developer: M.Abbasi 
Date: May. 2022
"""
import logging

from fridge import Fridge

class Store:
    def __init__(self, sensors_configs:dict) -> None:
        self.store_configs = sensors_configs
        self.fridges = self.fridge_iniriator()


    def fridge_iniriator(self):
        """generate fridges with giveen configs
        """
        fridge_list = []
        for fridge_config in self.store_configs.get('fridge_sensors'):
            fridge_list.append(Fridge(fridge_configs= fridge_config))
        
        return fridge_list

    