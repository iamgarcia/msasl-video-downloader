import json

class DownloadDatasets:

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(DownloadDatasets, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self):
        pass