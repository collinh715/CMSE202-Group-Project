import subprocess
import os
from Bacteria.bacteria import Bacteria
from Container.container import Petri_dish

runname = ''

def main(runname = ''):

    bacteria_types = ['Anaerobe','Aerobe']
    num_bac = 100

    os.makedirs(f'{runname}_Results')
    # for bac in bacteria_types:
    #     petri = Petri_dish()
    #     for i in range(num_bac):
    #         org = Bacteria()# bac astype of bacteria 
    #         petri.add_agent(org)
        
    #     petri.simulate_plot_populations()







if __name__ == '__main__':
    main()
