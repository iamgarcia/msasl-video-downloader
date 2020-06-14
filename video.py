class Video:
    
    def __init__(self):
        self.__url = 'empty'
        self.__start_time = 0.0
        self.__end_time = 0.0
        self.__label = -1

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def start_time(self):
        return self.__start_time
    
    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time):
        self.__end_time = end_time

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    def displayVars(self):
        print('url: ' + self.__url +
                '\nstart_time: ' + str(self.__start_time) +
                '\nend_time: ' + str(self.__end_time) +
                '\nlabel: ' + str(self.__label) + '\n')

# Testing class attributes
# video_1 = Video() # Create video object
# video_1.displayVars() # Display class variables

# video_1.url = 'https://www.youtube.com/watch?v=C37R_Ix8-qs'
# video_1.start_time = 0.0
# video_1.end_time = 2.767
# video_1.label = 830

# video_1.displayVars()