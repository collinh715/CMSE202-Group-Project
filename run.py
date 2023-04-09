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

    os.makedirs(f'Results{runname}')

    # shutil.move('movie.gif','_Results')
    for bac in bacteria_types:
        os.makedirs(f'Results{runname}/{bac}')

        # petri = Petri_dish()
        # for i in range(num_bac):
        #     org = Bacteria()# bac astype of bacteria 
        #     petri.add_agent(org)
        
        # petri.simulate_plot_populations()







# if __name__ == '__main__':
#     main(runname=runname)

pet = Petri_dish()
for i in range(100):
    org = Bacteria()
    pet.add_agent(org)
pet.simulate_save(10)
