<<<<<<< HEAD
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
    
    def __init__(self,type= 'Obligate Aerobe',  x_max=20, y_max=100, shape="o", color="saddlebrown", saturation_pop=50):
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
        self.x_max = x_max
        self.y_max = y_max
        self.x = random.randint(0, self.x_max)
        self.y = random.randint(0, self.y_max)
        self.color = color
        self.shape = shape
        self.loc = [self.x, self.y] #Need to randomize this to get even spread through the media
        if type == 'Obligate Aerobe':
            self.type = type
            self.o2 = 1
            self.tolerant = 'Intolerant'
        
    def set_o2(self, o2):
        self.o2 = o2
        
    def get_o2(self):
        return self.o2
    
    def get_loc(self):
        return self.loc
        
    def movement(self,gradient,vx=1,vy=1):
        
        if self.type == 'Obligate Aerobe':
            if np.random.rand() < 0.8:

                dy = np.random.randint(0,vy)
            else:
                dy = np.random.randint(-vy,0)
        elif self.type == 'Obligate Anaerobe':
            if np.random.rand() < 0.2:

                dy = np.random.randint(0,vy)
            else:
                dy = np.random.randint(-vy,0)
        elif self.type == 'Facultative Anaerobes':
            pass
        elif self.type == 'Aerotolerant Anaerobes':
            dy = np.random.randint(-vy,vy)

        elif self.type == 'Microaerophiles':
            if gradient[self.x,self.y] <= 0.8  and gradient[self.x,self.y] >= 0.7:
                dy = 0
            elif  gradient[self.x,self.y] > 0.8:
                dy = np.random.randint(-vy,0)
            else:
                dy = np.random.randint(0,dy)



      #['Obligate Aerobe','Obligate Anaerobe', 'Facultative Anaerobes', 'Aerotolerant Anaerobes','Microaerophiles']
        dx = np.random.randint(-vx,vx)

        if (self.x + dx > self.x_max) or (self.x + dx < 0):
            self.x = dx
        else:
            self.x += dx
        if (self.y + dy > self.y_max) or (self.y + dy < 0):
            self.y = dy
        else:
            self.y += dy
        
        self.loc = [self.x,self.y]
    
    def mitosis(self, x, y):
        """Returns new bacteria one "space" next to the parent.
        
           How do we do this? We could set up 4 (or 8) directions that take into
           account the x and y positions and either add or subtract 1 from either,
           and then select a random one of these positions.
            
        """
        pass

    def alive(self,gradient):
        x = self.x
        y = self.y

        grad = gradient[x,y]
        alive = True

        if self.type == 'Obligate Aerobe':
            if grad < 0.75:
                alive = False

        elif self.type == 'Obligate Anaerobe':
            if grad > 0.25:
                alive = False
        elif self.type == 'Facultative Anaerobes':
            pass
        elif self.type == 'Aerotolerant Anaerobes':
            pass

        elif self.type == 'Microaerophiles':
            if grad >= 0.85  or grad <= 0.65:
                alive = False

        return alive


    
    def draw(self,ax):
        ax.scatter(self.x, self.y, s=24.0, c=self.color, marker=self.shape)   
=======
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
    
    def __init__(self,type= 'Obligate Aerobe',  x_max=20, y_max=100, shape="o", color="saddlebrown", saturation_pop=50):
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
        self.x_max = x_max
        self.y_max = y_max
        self.x = random.randint(0, self.x_max)
        self.y = random.randint(0, self.y_max)
        self.color = color
        self.shape = shape
        self.loc = [self.x, self.y] #Need to randomize this to get even spread through the media
        self.type = type
        if type == 'Obligate Aerobe':
            self.type = type
            self.o2 = 1
            self.tolerant = 'Intolerant'
        
    def set_o2(self, o2):
        self.o2 = o2
        
    def get_o2(self):
        return self.o2
    
    def get_loc(self):
        return self.loc
        
    def movement(self,gradient,vx=1,vy=1):
        
        if self.type == 'Obligate Aerobe':
            if np.random.rand() < 0.8:

                dy = random.randint(0,vy)
            else:
                dy = random.randint(-vy,0)
        elif self.type == 'Obligate Anaerobe':
            if np.random.rand() < 0.2:

                dy = random.randint(0,vy)
            else:
                dy = random.randint(-vy,0)
        elif self.type == 'Facultative Anaerobes':
            pass
        elif self.type == 'Aerotolerant Anaerobes':
            dy = random.randint(-vy,vy)

        elif self.type == 'Microaerophiles':
            if gradient[self.x,self.y] <= 0.8  and gradient[self.x,self.y] >= 0.7:
                dy = 0
            elif  gradient[self.x,self.y] > 0.8:
                dy = random.randint(-vy,0)
            else:
                dy = random.randint(0,vy)


    #     dy = random.randint(-vx,vx)
    #   #['Obligate Aerobe','Obligate Anaerobe', 'Facultative Anaerobes', 'Aerotolerant Anaerobes','Microaerophiles']
        dx = random.randint(-vx,vx)

        if (self.x + dx > self.x_max) or (self.x + dx < 0):
            self.x = dx
        else:
            self.x += dx
        if (self.y + dy > self.y_max) or (self.y + dy < 0):
            self.y = dy
        else:
            self.y += dy
        
        self.loc = [self.x,self.y]
    
    def mitosis(self, x, y):
        """Returns new bacteria one "space" next to the parent.
        
           How do we do this? We could set up 4 (or 8) directions that take into
           account the x and y positions and either add or subtract 1 from either,
           and then select a random one of these positions.
            
        """
        pass

    def alive(self,gradient):
        x = self.x
        y = self.y

        grad = gradient[x,y]
        alive = True

        if self.type == 'Obligate Aerobe':
            if grad < 0.75:
                alive = False

        elif self.type == 'Obligate Anaerobe':
            if grad > 0.25:
                alive = False
        elif self.type == 'Facultative Anaerobes':
            pass
        elif self.type == 'Aerotolerant Anaerobes':
            pass

        elif self.type == 'Microaerophiles':
            if grad >= 0.85  or grad <= 0.65:
                alive = False

        return alive


    
    def draw(self,ax):
        ax.scatter(self.x, self.y, s=24.0, c=self.color, marker=self.shape)   
    
 
>>>>>>> 989e4b5f8a5122a589f8fa8f45d6e0eaa0b43ec4
