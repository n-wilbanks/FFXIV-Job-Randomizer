# Final Fantasy XIV Roulette Job Randomizer
# Written and tested in Python 3.11.5 on Windows 10
# This application is provided without warranty
# Modify this at your own risk

import string
import random
import os
import time
from pathlib import Path

path = Path('./jobs.txt')
system_random = random.SystemRandom()
jobs = ['Warrior', 'Paladin', 'Dark Knight', 'Gunbreaker', 'White Mage', 'Scholar', 'Astrologian', 'Sage', 'Monk', 'Samurai', 'Ninja', 'Viper', 'Dragoon', 'Reaper', 'Bard', 'Machinist', 'Dancer', 'Black Mage', 'Summoner', 'Red Mage', 'Pictomancer']

def main():
    # Main Menu
    print("Non-Mentors will probably want Option 2.")
    print("Please make a selection: ")
    print("    1: Job Streak Roulette (a file named 'jobs.txt' will be created where this program is saved)")
    print("    2: Choose my job at random (no files created)")
    print("    3: Explain the options")
    print("  Q/q: Quit this application")
    
    choice = input()
    
    match choice:
        case '1':
            chooseAndRemove()
            time.sleep(5)
            print("The application is now exiting...")
            exit()
        case '2':
            justChoose()
            time.sleep(5)
            print("Exiting...")
            exit()
        case '3':
            print("\nOption 1 on a first run will import every job in the game into a file, read it,\nselect a job for you, and remove that job from the list before saving the file. \nThis is to ensure you cannot receive that job again when selecting this option.")
            print("On a second run, Option 1 will read the file saved as 'jobs.txt', import all jobs within that file,\nand select from those.")
            print("If jobs.txt does not exist, this will run as if it were a first run, so be careful not to move or delete the file!\n")
            print("Option 1 will check to see if jobs.txt is empty on every run.  If it is, it will repopulate the file.\n")
            print("If you are looking to do streaks of varying length with a randomized job, this option is for you.\n")
            print("Option 2 will select a random job for you and the application will automatically close after 5 seconds.\n")
            print("Option 3 will display this menu and return to the main menu after 5 seconds.\n")
            print("Q or q will immediately quit the application.\n")
            time.sleep(5)
            main()
        case 'Q' | 'q':
            print("Exiting...")
            exit()
    
# Choose a job and remove it from the list - Previously intended for Mentor Roulette streaks to encourage job mastery
def chooseAndRemove():
    print("Checking for", path)
    time.sleep(3)
    # If jobs.txt exists, reads in the file and picks a job from what's left
    if path.exists():
        try:
            jobsLeft = ""
            # Check if jobs is empty. If yes, repopulate the list
            if os.stat(path).st_size == 0:
                with open(path, "w") as fil:
                    fil.write("\n".join(jobs))
                    fil.close()
            with open(path, "r") as fi:
                jobsLeft = fi.read().splitlines()
                fi.close()
            with open(path, "w") as f:
                jobChosen = system_random.choice(jobsLeft)
                print(jobChosen)
                jobsLeft.remove(jobChosen)
                f.write("\n".join(jobsLeft))
                f.close()
        except ValueError as e:
            print("Something went wrong! Closing...")
            print(e)
            time.sleep(3)
            exit()
    # If jobs.txt does not exist, create a file with all jobs and select from those
    if not path.exists():
        try:
            with open(path, "w") as f:
                jobChosen = system_random.choice(jobs)
                print(jobChosen)
                jobs.remove(jobChosen)
                f.write("\n".join(jobs))
                f.close()
        except ValueError as e:
            print("Something went wrong! Closing...")
            print(e)
            time.sleep(3)
            exit()

# Just choose a job - Intended for everything other than job streaks
def justChoose():
    print(system_random.choice(jobs))

if __name__ == "__main__":
	main()