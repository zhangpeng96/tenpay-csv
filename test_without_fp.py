import json, time, csv

with open("example.json", "rt", encoding="utf-8") as file:
    data = json.load(file)

records = data['record']

for rec in records:
    rec['fee'] = rec['fee'] / 100
    rec['trans_id'] = str(rec['trans_id'])
    rec['out_trade_no'] = str(rec['out_trade_no'])
    rec['timestamp'] = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(rec['timestamp']))


print((records[0]).keys())

for rec in records:
    print(rec.values())
