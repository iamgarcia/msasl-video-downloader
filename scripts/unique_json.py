import json

class_list = []
for x in range(1000):
    class_list.append(x)

filtered_file = open('temp/MSASL_test_filtered.json')
json_array = json.load(filtered_file)

unique_list = []

for item in json_array:
    if not class_list == []:
        if item['label'] in class_list:
            video = { "url": None, "start_time": None, "end_time": None, "label": None}
            if 'https://' in item['url']:
                video['url'] = item['url']
            else:
                video['url'] = 'https://' + item['url']
            video['start_time'] = item['start_time']
            video['end_time'] = item['end_time']
            video['label'] = item['label']
            unique_list.append(video)
            class_list.remove(item['label'])

with open('temp/MSASL_test_unique.json', 'w') as fp:
    fp.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in unique_list) +
        ']')