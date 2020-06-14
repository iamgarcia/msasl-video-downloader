# try:
#     import video
#     from gloss_lookup import GlossLookup
#     import video_downloader
# except Exception as e:
#     print('Some modules are missing: {}'.format(e))

import sys
from download_datasets import DownloadDatasets
from gloss_lookup import GlossLookup
from os import system, name

# Instantiate singleton classes
gl = GlossLookup()
dd = DownloadDatasets()

def menu():
    print(15 * '-', 'MENU', 15 * '-')
    print('[1] Gloss Lookup' + '\n[2] Download datasets (run only once to download all datasets)' + '\n[3] Exit program')
    print(36 * '-')
    
def clear():
    # For windows
    if name == 'nt':
        _ = system('cls')

    # For Mac and Linux
    else:
        _ = system('clear')

def glossLookup():
    loop = True
    while loop:
        gl.menu()
        answer = int(input('Enter the class (an integer between 0 to 999): '))
        
        if gl.wordExists(answer):
            print('Word: ' + gl.searchGlossary(answer) + '\n')
            loop = False
        else:
            print('Invalid class. Please enter a valid class.')

# TODO 
def downloadDatasets():
    pass

def main():
    loop = True
    while loop:
        menu()
        answer = int(input('Enter your choice [1-3]: '))

        if answer == 1:
            glossLookup()
        elif answer == 2:
            pass
        elif answer == 3:
            pass
            loop = False
        else:
            print('\nInvalid option. Please try again.' + '\n')

    sys.exit()

# Main driver
if __name__ == '__main__':
    main()