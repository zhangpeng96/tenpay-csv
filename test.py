import json, time, csv

with open("example.json", "rt", encoding="utf-8") as file:
    data = json.load(file)

records = data['record']



with open("test.csv", "w+", encoding="gbk", newline="") as output:
    csvwriter = csv.writer(output, dialect=("excel"))
    csvwriter.writerow((records[0]).keys())

    for rec in records:
        csvwriter.writerow(rec.values())
