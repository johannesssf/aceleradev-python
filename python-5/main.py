from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1546314000, 'start': 1546313400},
    # extra case 4
    {'source': '48-996383691', 'destination': '41-885633781', 'end': 1567336500, 'start': 1567307700},
    {'source': '48-996383691', 'destination': '41-885633781', 'end': 1567328820, 'start': 1567328280},
    {'source': '48-996383691', 'destination': '41-885633781', 'end': 1546330439, 'start': 1546329315},
    {'source': '48-996383691', 'destination': '41-885633781', 'end': 1546389000, 'start': 1546385400},
    # extra case 5
    {'source': '48-996383692', 'destination': '41-885633782', 'end': 1567562400, 'start': 1567515600},
    {'source': '48-996383693', 'destination': '41-885633783', 'end': 1567559755, 'start': 1567556110},
    # extra case 6
    {'source': '48-996383692', 'destination': '41-885633782', 'end': 1567908000, 'start': 1567843200},
    {'source': '48-996383693', 'destination': '41-885633783', 'end': 1569027720, 'start': 1568969880},
    {'source': '48-996383693', 'destination': '41-885633783', 'end': 1546387500, 'start': 1546329300},
]


def calc_minutes_in_period(start, end):
    t0 = datetime.fromtimestamp(start)
    t1 = datetime.fromtimestamp(end)
    nocturne_min = 0
    diurnal_min = 0

    # case 1: call started and finished between 00:00 and 05:59
    if (0 <= t0.hour < 6) and (0 <= t1.hour < 6):
        diff = t1 - t0
        nocturne_min = diff.seconds // 60
        return nocturne_min, diurnal_min

    # case 2: call started and finished between 06:00 and 21:59
    if (6 <= t0.hour < 22) and (6 <= t1.hour < 22):
        diff = t1 - t0
        diurnal_min = diff.seconds // 60
        return nocturne_min, diurnal_min

    # case 3: call started and finished between 22:00 and 23:59
    if (22 <= t0.hour < 24) and (22 <= t1.hour < 24):
        diff = t1 - t0
        nocturne_min = diff.seconds // 60
        return nocturne_min, diurnal_min

    # case 4: call started before 06:00 and finished between 06:00 and 21:59
    if (t0.hour < 6) and (6 <= t1.hour < 22):
        nocturne_min = (6 - t0.hour) * 60 - t0.minute
        diurnal_min = (t1.hour - 6) * 60 + t1.minute
        return nocturne_min, diurnal_min

    # case 5: call started between 06:00 and 21:59 and finished after 22:00
    if (6 <= t0.hour < 22) and (22 <= t1.hour):
        nocturne_min = (22 - t0.hour) * 60 - t0.minute
        diurnal_min = (t1.hour - 22) * 60 + t1.minute
        return nocturne_min, diurnal_min

    # case 6: call started before 06:00 and finished after 22:00
    if (t0.hour < 6) and (22 <= t1.hour):
        nocturne_min = (6 - t0.hour) * 60 - t0.minute
        nocturne_min += (22 - t1.hour) * 60 + t1.minute
        diurnal_min = 16 * 60
        return nocturne_min, diurnal_min


def order_bill_by_value_asc(bill):
    for i in range(len(bill)-1):
        for j in range(i+1, len(bill)):
            if bill[j]['total'] < bill[i]['total']:
                bill[j], bill[i] = bill[i], bill[j]

    return bill


def classify_by_phone_number(records):
    bill = []
    for record in records:
        nocturne_min, diurne_min = calc_minutes_in_period(record['start'], record['end'])
        # t0 = datetime.fromtimestamp(record['start'])
        # t1 = datetime.fromtimestamp(record['end'])

        # total_sec = (t1-t0).seconds
        # total_min = total_sec // 60

        # dt_start = t0.strftime('%H:%M:%S %d-%m-%y')
        # dt_end = t1.strftime('%H:%M:%S %d-%m-%y')

        # print(dt_start, dt_end, nocturne_min, diurne_min, (nocturne_min + diurne_min) * 60)
        total = (nocturne_min + diurne_min) * 0.36 + (diurne_min * 0.09)
        bill.append({'source': record['source'], 'total': round(total, 2)})

    return order_bill_by_value_asc(bill)


if __name__ == "__main__":
    print(classify_by_phone_number(records))