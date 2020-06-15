import json

input_file = open('MSASL_test.json')
json_array = json.load(input_file)

filtered_list = []

for item in json_array:
    video_details = { "url": None, "start_time": None, "end_time": None, "label": None}
    video_details['url'] = item['url']
    video_details['start_time'] = item['start_time']
    video_details['end_time'] = item['end_time']
    video_details['label'] = item['label']
    filtered_list.append(video_details)

with open('MSASL_test_filtered.json', 'w') as fp:
    fp.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in filtered_list) +
        ']')