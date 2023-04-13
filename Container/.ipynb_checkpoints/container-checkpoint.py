#imports
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import moviepy.editor as mp


class Petri_dish():
    """Petri_dish class. 
    """
    
    def __init__(self, xsize=20, ysize=100 ):
        self.xsize = xsize
        self.ysize = ysize
        self.gradient = np.ones((self.xsize+1,self.ysize+1,1))
        self.bacteria_agents = []

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
    
    def simulate(self,tot_time):
        for dt in range(tot_time):
            plt.figure(figsize=(6, 6))    
            ax = plt.gca()   
            
            # loop over each bacteria
            temp_agents = []
            for agent in self.bacteria_agents:
                agent.movement(self.gradient)
                agent.draw(ax)
                temp_agents.append(agent)
                
            self.bacteria_agents.clear
            self.bacteria_agents = temp_agents
            plt.xlim(0,self.xsize)
            plt.ylim(0,self.ysize)
            plt.show()   
            time.sleep(0.001)      

    def simulate_save(self,tot_time,bac):
        gradient = self.gradient
        frames = []
        fig, ax = plt.subplots(figsize=(1,5))
        
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
        
        ax.set_facecolor('khaki')
        plt.axis('off')
        plt.xlim(0,self.xsize)
        plt.ylim(0,self.ysize)


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
