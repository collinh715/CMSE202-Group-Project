#imports
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import moviepy.editor as mp


class Petri_dish():
    """Petri_dish class. 
    Constructs our enviroment or test tube for our bacteria to move in. 
    
    Attributes:
        xsize=20, ysize=100: Setting boundaries for our test tube.
        
    Methods:
        add_agent(self,agent): Adds bacteria agents to our simulation.
        
        simulate_save(self,tot_time,bac): Simulates our enviroment and saves the seperate gifs and 
                                          mp4 files into folders.
    """
    
    def __init__(self, xsize=20, ysize=100 ):
        self.xsize = xsize
        self.ysize = ysize
        self.bacteria_agents = []

        #Sets o2 gradiant.
        self.gradient = np.ones((self.xsize+1,self.ysize+1,1))
        gradient = []
        gradient_step = 1/(ysize-1)
        gradient_val = 0
        for i in range(ysize):
            gradient.append(gradient_val)
            gradient_val += gradient_step
        for i in range(ysize):

            self.gradient[:,i] = self.gradient[:,i] * gradient[i]        

   
    def add_agent(self,agent):
        self.bacteria_agents.append(agent)
      
    def simulate_save(self,tot_time,bac):
        gradient = self.gradient
        frames = []
        fig,ax = plt.subplots(figsize=(1,5))
        # plt.figure(figsize=(1,5))
        # ax = plt.gca()
        for dt in range(tot_time):
    
            
            # loop over each bacteria
            temp_agents = []
            x = []
            y = []
            for agent in self.bacteria_agents:
                agent.movement(gradient,vx = 1,vy = 1)
                # if agent.alive(gradient) == True:
                #     temp_agents.append(agent)
                #     x.append(agent.get_loc()[0])
                #     y.append(agent.get_loc()[1])
                temp_agents.append(agent)
                x.append(agent.get_loc()[0])
                y.append(agent.get_loc()[1])

            self.bacteria_agents.clear
            self.bacteria_agents = temp_agents

            frames.append([plt.scatter(x,y,animated=True, color = 'r')])
        
        ax.set_facecolor("orange")
        plt.axis('off')
        plt.xlim(-10,self.xsize+10)
        plt.ylim(-10,self.ysize+10)


        ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True,
                                            repeat_delay=1000)
        

        if len(bac.split()) == 2:
            name = f'{bac.split()[0]}_{bac.split()[1]}'
        else:
            name = f'{bac}'


        ani.save(f'{name}.gif',fps= 10)
        clip = mp.VideoFileClip(f'{name}.gif')
        clip.write_videofile(f'{name}.mp4')
        plt.show()   

