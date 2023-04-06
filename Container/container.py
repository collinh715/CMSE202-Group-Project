#imports
import random
import time
import numpy as np
import matplotlib.pyplot as plt

class Petri_dish():
    """Petri_dish class. 
    """
    
    def __init__(self, xsize=1000, ysize=100, ):
        self.xsize = xsize
        self.ysize = ysize
        self.environ = np.zeros((self.xsize,self.ysize,3))
        self.environ[:,:,0] = 0.38
        self.environ[:,:,1] = 0.19
        self.environ[:,:,2] = 0.04
        self.bacteria_agents = []
        o2_level=[1, .8, .7, .6, .5, .4, .3, .2, .1, 0]
        

    
    def add_agent(self,agent):
        self.bacteria_agents.append(agent)
    
    def simulate(self,tot_time):
        for dt in range(tot_time):
            clear_output(wait=True)
            plt.figure(figsize=(6, 6))    
            plt.imshow(self.environ) 
            ax = plt.gca()   
            
            # loop over each animal
            temp_agents = []
            for agent in self.bacteria_agents:
                agent.movement()
                agent.draw(ax)
                
            self.bacteria_agents.clear
            self.bacteria_agents = temp_agents
            plt.xlim(0,self.xsize)
            plt.ylim(0,self.ysize)
            plt.show()   
            time.sleep(0.001)      

    def simulate_plot_populations(self,tot_time):
        self.light_brown_animals = []
        self.dark_brown_animals = []
        self.times = []
        for dt in range(tot_time):
            
            # loop over each animal agent
            temp_agents = []
            for agent in self.bacteria_agents:
                agent.movement()
                
            self.bacteria_agents.clear
            self.bacteria_agents = temp_agents

            self.times.append(dt)
            self.light_brown_animals.append(0)
            for agent in self.bacteria_agents:
                if agent.color == 'goldenrod':
                    self.light_brown_animals[-1] += 1

        plt.plot(self.times,self.light_brown_animals)   
        plt.show()