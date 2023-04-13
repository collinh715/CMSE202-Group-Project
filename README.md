# CMSE202-Group-Project
Group project for CMSE 202 concerning the oxygen tolerance of bacteria


# How to Run the Code
## Imports
To be able to run the code, one first needs to import a new package that creates the .mp4 files.

Use `pip install moviepy` to install the new package

## Running The Run File
Once this new package is installed, you are ready to run the code. Now all you need to do is to run the filed named `run.py` with `python run.py <runame>` where `runname` is an optional argument. 

Once running this file, it creates a new directory called `Results` or `Results_runame` if that argument was given. It then creates files for each type of bacteria, saving a .gif and .mp4 file of the simulated bacteria and a .png of the final time step. 

If you want to change the initial amount of bacteria or time steps, you can go into the `main()` function in the `run.py`. `num_bac` is the number of bacteria, and `time` is the amount of time steps.


# Group Member Contribution
**Collin**
1. constructed the initial bacteria file
2. constructed the container file
3. collected data for result comparison

**Julia**
1. contributed to bacteria file
2. contributed to container file
3. constructed the presentation slides
4. contributed to the README.md file

**Sam**
1. contributed to bacteria file
2. contribbuted to container file
3. constructed the part of the container file to save the simulation
4. constructed the run file
5. contributed to the README.md file
