import json

data_record = []

for i in range(5, 10):
    with open("stream-response ("+ str(i) +").txt", "rt", encoding="utf-8") as file:
        data = json.load(file)
        for rec in data['record']:
            data_record.append(rec)

data['record'] = data_record
data_str = json.dumps(data, indent = 2)

f = open('concat.json', 'w', encoding="utf-8")
f.write(data_str)
f.close()
