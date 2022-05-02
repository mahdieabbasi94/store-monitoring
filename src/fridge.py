"""laus deo
project name: store monitoring
project description: simulate a smart store and monitor it
module name: fridge
module description: simulate fridge sensors used in this project
developer: M.Abbasi 
Date: May. 2022
"""
import logging

import numpy as np # no need this library. generate normal distribution with random
import random

class Fridge:
    """Fridge sensors to 
    """
    def __init__(self, fridge_configs: dict) -> None:
        
        # temperature sensor configs
        self.tempAve = fridge_configs.get('TemperatureAverage') 
        self.tempVar = fridge_configs.get('TemperatureVariance')
        
        # humidity sensor configs
        self.HumidityAve = fridge_configs.get('HumidityAverage')
        self.HumidityVar = fridge_configs.get('HumidityVariance')
        

    @staticmethod
    def binary_sensor()-> bool:
        """report a binary sensor

        Returns:
            bool: Boolian True or False output
        """
        return random.choice([True, False])

    @staticmethod
    def continious_sensors(mean:float, var:float)->float:
        """generate analog sensor answers with specified mean and variance
            in random normal distribiution. 

        Args:
            mean (float): mean of output 
            var (float): variance of output

        Returns:
            float: output of sensor
        """
        ##
        ## refactor this method with random function using
        ##
        return np.random.normal(loc=mean, scale =var , size = 1)

    def Temperature(self)->float:
        """generate temperature value

        Returns:
            float: tempereture value
        """
        return self.continious_sensors(self.tempAve, self.tempVar)


    def Humidity(self)->float:
        """generate humidity of fridge

        Returns:
            float: humidity value
        """
        return self.continious_sensors(self.HumidityAve, self.HumidityAve)
        
    def Fan_status(self) -> bool: 
        """_summary_

        Returns:
            bool: _description_
        """
        return self.binary_sensor()
        
    def Oil_alarm_status(self)->bool: 
        
        return self.binary_sensor()
        
    def Door_status(self)->bool:
        
        return self.binary_sensor()
        