#imports
import random
import time
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.cm as cm
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
        

        o2_level=[1, .8, .7, .6, .5, .4, .3, .2, .1, 0]
        

   
    def add_agent(self,agent):
        self.bacteria_agents.append(agent)
    
    def simulate(self,tot_time):
        for dt in range(tot_time):
            # clear_output(wait=True)
            plt.figure(figsize=(6, 6))    
            # plt.imshow(self.environ) 
            ax = plt.gca()   
            
            # loop over each animal
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

    def simulate_plot_populations(self,tot_time):
        self.light_brown_animals = []
        self.dark_brown_animals = []
        self.times = []
        for dt in range(tot_time):
            
            # loop over each animal agent
            temp_agents = []
            for agent in self.bacteria_agents:
                agent.movement(self.gradient)
                
            self.bacteria_agents.clear
            self.bacteria_agents = temp_agents

            self.times.append(dt)
            self.light_brown_animals.append(0)
            for agent in self.bacteria_agents:
                if agent.color == 'goldenrod':
                    self.light_brown_animals[-1] += 1

        plt.plot(self.times,self.light_brown_animals)   
        plt.show()

    def simulate_save(self,tot_time,bac):
        gradient = self.gradient
        frames = []
        fig, ax = plt.subplots(figsize=(1,5))
        # fig = plt.figure(figsize=(1,5),facecolor='khaki')
        # plt.axhline(50,0,20)
        for dt in range(tot_time):
    
            
            # loop over each animal
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

