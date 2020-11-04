from manimlib.imports import *
import numpy as np

class Normal(GraphScene):
    
    def construct(self):
        pdf = lambda sigma, miu: lambda x: 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-0.5*((x - miu)/sigma)**2) 

        
