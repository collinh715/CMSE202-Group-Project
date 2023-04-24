import random
import numpy as np

class Bacteria():
    """Bacteria class. 
    
    Methods:
        get_loc: 
            Returns location of bacteria in x and y cords.
        
        movement: 
            Sets up movement with probability the the bacteria will move towards its prefered oxygen concentration.
        
        alive:
            Sets up requirements for the survival of the bacteria, as well as conditions for its probable death.
    """
    
    def __init__(self,type,  x_max=20, y_max=100):
        """Initializes a bacteria with random starting point on 2D plane. Default location is (0, 0).
           Default o2 affinity is 0.5.
        
        Args:
            x [type: int]
                Specifies the column of the bacteria in a 2d grid.
            
            y [type: int]
                Specifies the row of the bacteria in a 2d grid.
                
            type [type: float]
                Type of bacteria we are aiming to model.

            death [type: float]
                a float that represents the sum of the normalizes distance a bacteria is away from prefered concentration, 
                when greater than a specified number the bacteria dies
            
            stay[type: bool]
                a boolean that represents whether or not a faculative anaerobe will be indifferent to the o2 concentration
        """
        self.x_max = x_max
        self.y_max = y_max
        self.x = random.randint(0, self.x_max)#x,y are randomly generated between the maxes
        self.y = random.randint(0, self.y_max)
        self.loc = [self.x, self.y] # location in x,y coordinates
        self.type = type
        self.death = 0

        self.stay = True
        if np.random.rand() < 0.8:# there is an 80% probanility that a bacteria will not stay put for FA's
            self.stay = False
    
    def get_loc(self):
        '''
        Returns the location of a bacteria in x,y coordinates
        '''
        return self.loc
        
    def movement(self,gradient,vx=1,vy=1):
        '''
        Sets up movement with probability the the bacteria will move towards its prefered oxygen concentration.

        Args:
            gradient[type: numpy array]:
                a multi dimensional array that contains the oxygen gradient at every location

            vx,vy [type: int]:
                The max movement in the x and y direction repesctively

        A bacteria will move randomly if it in its perfered oxygen concentration, if it is not, it will preferntially
        move towards the prefered oxygen with some probability. This movement towards and away is only for the y direction
        the x direction movement is completely random for all type of bacteria.
        '''
        x = self.x
        y = self.y

        grad = gradient[x,y]

        if self.type == 'Obligate Aerobe':
            if grad >= 0.85:
                dy = random.randint(-vy,vy)
            else:
                if np.random.rand() < 0.8:

                    dy = random.randint(0,vy)
                else:
                    dy = random.randint(-vy,0)
        elif self.type == 'Obligate Anaerobe':
            if grad <= 0.15:
                dy = random.randint(-vy,vy)
            else:
                if np.random.rand() < 0.2:

                    dy = random.randint(0,vy)
                else:
                    dy = random.randint(-vy,0)
        elif self.type == 'Facultative Anaerobes':
            if grad >= 0.85 or self.stay:
                dy = random.randint(-vy,vy)

            else:
                if  (1-grad) < np.random.rand():
                    dy = random.randint(-vy,vy)
                else:
                    dy = random.randint(0,vy)


            
        elif self.type == 'Aerotolerant Anaerobes':
            dy = random.randint(-vy,vy)

        elif self.type == 'Microaerophiles':
            if grad <= 0.8  and grad >= 0.7:
                dy = random.randint(-vy,vy)
            elif  gradient[self.x,self.y] > 0.8:
                dy = random.randint(-vy,0)
            else:
                dy = random.randint(0,vy)

        dx = random.randint(-vx,vx)
        '''
        This part checks if the bacteria's movement will move outside of the vile, if it does
        it mantains its current position in that direction.
        '''
        if (self.x + dx > self.x_max) or (self.x + dx < 0):
            self.x -= dx
        else:
            self.x += dx
        if (self.y + dy > self.y_max) or (self.y + dy < 0):
            self.y -= dy
        else:
            self.y += dy
        
        self.loc = [self.x,self.y]

    def alive(self,gradient):
        '''
        Sets up requirements for the survival of the bacteria, as well as conditions for its probable death.

        Args:
            gradient[type: numpy array]:
                a multi dimensional array that contains the oxygen gradient at every location

        This method will add a float to the death attribute depending on how far away the bacteria
        is from its prefered oxygen concentration. This is a normalized value. If the death attribute 
        is more than a specified value, then the bacteria is dead, and alive is set to false, if it is
        not, it remains true and the bacteria is set for the next interation.
      
        '''
        x = self.x
        y = self.y

        grad = gradient[x,y]
        alive = True

        if self.type == 'Obligate Aerobe':
            if grad < .85:
                val = (.85-grad)/(.85)
                self.death += val 

        elif self.type == 'Obligate Anaerobe':
            if grad > .15:
                val = (grad-0.15)/(.85)
                self.death += val 

        elif self.type == 'Facultative Anaerobes':
            pass
        elif self.type == 'Aerotolerant Anaerobes':
            pass

        elif self.type == 'Microaerophiles':
            if grad > 0.8:
                val = (grad - 0.8)/0.7
                self.death += val
            elif grad < 0.7:
                val = (0.7 - grad)/0.8
                self.death += val 
                

        if self.death >40:
            alive = False

        return alive

