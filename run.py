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










if __name__ == '__main__':
    main(runname=runname)


