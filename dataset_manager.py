import os
import shutil
import json
from video import Video

class DatasetManager:

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(DatasetManager, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self):
        self.__MSASL_100 = 'MS-ASL100'
        self.__MSASL_200 = 'MS-ASL200'
        self.__MSASL_500 = 'MS-ASL500'
        self.__MSASL_1000 = 'MS-ASL1000'
        self.__dataset_size = 0

        # Empty list to be filled with Video objects
        self.__dataset = []

    def isValidDataset(self, dataset):
        return True if dataset == 1 or dataset == 2 or dataset == 3 or dataset == 4 else False

    def createDirectoryHandler(self, directory):
        if directory == 1:
            self.createDirectory(self.__MSASL_100)
        elif directory == 2:
            self.createDirectory(self.__MSASL_200)
        elif directory == 3:
            self.createDirectory(self.__MSASL_500)
        else:
            self.createDirectory(self.__MSASL_1000)

    def createDirectory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print(directory + ' already exists.')

    def deleteDirectory(self, directory):
        if os.path.exists(directory):

            # Delete an empty directory
            if len(directory) == 0:
                os.rmdir(directory)

            # Delete a non-empty directory
            else:
                shutil.rmtree(directory)
        else:
            print(directory + ' does not exist.')

    def deleteDirectoryHandler(self, directory):
        if directory == 1:
            self.deleteDirectory(self.__MSASL_100)
        elif directory == 2:
            self.deleteDirectory(self.__MSASL_200)
        elif directory == 3:
            self.deleteDirectory(self.__MSASL_500)
        else:
            self.deleteDirectory(self.__MSASL_1000)

    def generateDataset(self):
        loop = True
        while loop:
            self.generateDatasetMenu()
            answer = int(input('Enter your choice [1-4]: '))
            if self.isValidDataset(answer):
                self.createDirectoryHandler(answer)
                
                # TODO
                
                loop = False
            else:
                print('Invalid option. Please try again.')   

    def deleteDataset(self):
        loop = True
        while loop:
            self.deleteDatasetMenu()
            answer = int(input('Enter your choice [1-4]: '))
            if self.isValidDataset(answer):
                self.deleteDirectoryHandler(answer)
                loop = False
            else:
                print('Invalid option. Please try again.')

    def menu(self):
        print()
        print(15 * '-', 'DATASET MANAGER', 15 * '-')
        print('[1] Generate a dataset')
        print('[2] Delete a dataset')
        print('[3] Back to main menu')
        print(47 * '-')

    def generateDatasetMenu(self):
        print()
        print(15 * '-', 'GENERATE DATASET', 15 * '-')
        print('[1] MS-ASL100')
        print('[2] MS-ASL200')
        print('[3] MS-ASL500')
        print('[4] MS-ASL1000')
        print(48 * '-')

    def deleteDatasetMenu(self):
        print()
        print(15 * '-', 'DELETE DATASET', 15 * '-')
        print('[1] MS-ASL100')
        print('[2] MS-ASL200')
        print('[3] MS-ASL500')
        print('[4] MS-ASL1000')
        print(46 * '-')