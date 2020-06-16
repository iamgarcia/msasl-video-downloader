import json
import os
import shutil

def deleteFile(directory):
    if os.path.exists(directory):
        os.remove(directory)
    else:
        print(directory + ' does not exist.')

def deleteDirectory(directory):
    if os.path.exists(directory):

        # Delete an empty directory
        if len(directory) == 0:
            os.rmdir(directory)

        # Delete a non-empty directory
        else:
            shutil.rmtree(directory)
    else:
        print(directory + ' does not exist.')

def byLabel(video):
    return video['label']

unique_file = open('temp/MSASL_test_unique.json')
json_array = json.load(unique_file)
unique_file.close()

json_array.sort(key=byLabel)

deleteFile('MSASL_test.json')

with open('MSASL_test.json', 'w') as fp:
    fp.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in json_array) +
        ']')

deleteDirectory('temp')