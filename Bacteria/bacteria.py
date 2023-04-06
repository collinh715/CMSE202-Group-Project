import random
import numpy as np
import matplotlib.pyplot as plt

class Bacteria():
    """Bacteria class. 
    Each bacteria species needs to have a prefered oxygen 
    concentration as well as rules that governs its motion.
    We also need to distribute and size our population evenly
    
    
    Attributes:
        o2 [type: int64]
            Number from 0 to 1, 0 meaning the bacteria dies from oxygen and
            1 meaning that it needs oxygen to survive.
        loc [type: tuple]
            Ordered pair of coordinates specifying the bacteria's location.
        
    Methods:
        __init__(c=0, r=0, o2=0.5)
        mitosis()
            Returns a new bacteria.
        draw()
            Draws the bacteria.
    """
    
    def __init__(self, x_max=1000, y_max=100, o2=0.5, shape="o", color="saddlebrown", saturation_pop=150):
        """Initializes a bacteria with random starting point on 2D plane. Default location is (0, 0).
           Default o2 affinity is 0.5.
        
        Args:
            x [type: int]
                Specifies the column of the bacteria in a 2d grid.
            
            y [type: int]
                Specifies the row of the bacteria in a 2d grid.
                
            o2 [type: float]
                Probability that bacteria mutate
        """
        self.x = random.randint(0, x_max)
        self.y = random.randint(0, y_max)
        self.xmax = x_max
        self.ymax = y_max
        self.color = color
        self.shape = shape
        self.loc = (x, y) #Need to randomize this to get even spread through the media
        self.o2 = o2
        
        
    def movement(self,vx=1,vy=1):
        dx = np.random.randint(-vx,vx)
        dy = np.random.randint(-vy,vy)

        if (self.x + dx > self.x_max) or (self.x + dx < 0):
            self.x -= dx
        else:
            self.x += dx
        if (self.y + dy > self.y_max) or (self.y + dy < 0):
            self.y -= dy
        else:
            self.y += dy
    
    def mitosis(self, x, y):
        """Returns new bacteria one "space" next to the parent.
        
           How do we do this? We could set up 4 (or 8) directions that take into
           account the x and y positions and either add or subtract 1 from either,
           and then select a random one of these positions.
            
        """
        pass
    
    def set_loc(self):
        #Would be used to set up random locations in our enviroment
        pass
    
    def draw(self,ax):
        ax.scatter(self.x, self.y, s=24.0, c=self.color, marker=self.shape)   
    
 