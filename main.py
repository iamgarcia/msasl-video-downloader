import sys
from dataset_manager import DatasetManager
from gloss_lookup import GlossLookup

# Instantiate singleton classes
gl = GlossLookup()
dm = DatasetManager()

def menu():
    print()
    print(15 * '-', 'MAIN MENU', 15 * '-')
    print('[1] Gloss Lookup' + '\n[2] Dataset manager' + '\n[3] Exit program')
    print(41 * '-')
    
def glossLookup():
    loop = True
    while loop:
        gl.menu()
        answer = int(input('Enter the class (an integer between 0 to 999): '))
        
        if gl.wordExists(answer):
            print('Word: ' + gl.searchGlossary(answer))
            loop = False
        else:
            print('Invalid class. Please enter a valid class.')

def datasetManager():
    loop = True
    while loop:
        dm.menu()
        answer = int(input('Enter your choice [1-3]: '))

        if answer == 1:
            dm.generateDataset()
        elif answer == 2:
            dm.deleteDataset()
        elif answer == 3:
            loop = False
        else:
            print('Invalid option. Please try again.')

def main():
    loop = True
    while loop:
        menu()
        answer = int(input('Enter your choice [1-3]: '))

        if answer == 1:
            glossLookup()
        elif answer == 2:
            datasetManager()
        elif answer == 3:
            loop = False
        else:
            print('Invalid option. Please try again.')

    sys.exit()

# Main driver
if __name__ == '__main__':
    main()