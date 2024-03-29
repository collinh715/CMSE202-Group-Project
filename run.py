import subprocess
import os
import shutil
import sys
from Bacteria.bacteria import Bacteria
from Container.container import Petri_dish

if len(sys.argv) == 2:
    runname = f'_{sys.argv[1]}'
else:
    runname = ''

def main(runname = ''):
    '''
    The main program takes an optional argument runame, to rename the the directory of the results file
    The purpose of this function and script is to interate through each type of bacteria, given an intial amount num_bac
    and total time, time, for the simulation to run, and it will run the simulation by importing the two classes made in
    the other files. It then saves and moves each of the .png, .gif. and .mp4 files into a create directory with the name 
    of the bacteria. This creates a simple way to create and store resultsin files without having to do them manually. 
    Running this script will run the main function.
    '''

    bacteria_types = ['Obligate Aerobe','Obligate Anaerobe', 'Facultative Anaerobes', 'Aerotolerant Anaerobes','Microaerophiles']
    num_bac = 100
    time = 200
    if os.path.exists(f'Results{runname}'):
        shutil.rmtree(f'Results{runname}')
    os.makedirs(f'Results{runname}')


    for bac in bacteria_types:

        if len(bac.split()) == 2:
            name = f'{bac.split()[0]}_{bac.split()[1]}'
        else:
            name = f'{bac}'

        dir = f'Results{runname}/{name}'
        os.makedirs(dir)


        petri = Petri_dish()
        for i in range(num_bac):
            org = Bacteria(type=bac)
            petri.add_agent(org)

    

        petri.simulate_save(time,bac)

        shutil.move(f'{name}.gif',dir)
        shutil.move(f'{name}.mp4',dir)
        shutil.move(f'{name}.png',dir)











if __name__ == '__main__':
    main(runname=runname)


