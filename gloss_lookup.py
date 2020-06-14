import json

class GlossLookup:
    
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(GlossLookup, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self):
        self.__glossary = []
        self.decodeGlossary()

    @property
    def glossary(self):
        return self.__glossary

    def showGlossary(self):
        for i in range(len(self.__glossary)):
            print(self.__glossary[i])

    def decodeGlossary(self):
        # Open MSASL_classes JSON file
        input_file = open('MSASL_classes.json',)

        # Read JSON encoded data from file and convert it into Python dictionary
        self.__glossary = json.load(input_file)

    def wordExists(self, label_id):
        return True if label_id >= 0 and label_id <= 999 else False

    def searchGlossary(self, label_id):
        if(self.wordExists(label_id)):
            # Search through list using label_id as index
            # Decalre variable label and assign it to the value at label_id
            # Return value of label
            return self.glossary[label_id]

    def menu(self):
        print()
        print(15 * '-', 'GLOSS LOOKUP', 15 * '-')
        print('This glossary represents classes in the classification task.')
        print('The first word in the set (hello) is class 0.')
        print('The last word in the set (challenge) is class 999.')
        print(44 * '-')