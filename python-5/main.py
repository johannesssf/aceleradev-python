from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000},
]


def calc_minutes_in_period(start, end):
    t0 = datetime.fromtimestamp(start)
    t1 = datetime.fromtimestamp(end)
    MARK_06H = datetime(t0.year, t0.month, t0.day, 6, 0, 0)
    MARK_22H = datetime(t0.year, t0.month, t0.day, 22, 0, 0)
    MINUTES_16HOURS = 16 * 60
    noct_minutes = 0
    diur_minutes = 0

    # case 1: call started and finished between 00:00 and 05:59
    if (0 <= t0.hour < 6) and (0 <= t1.hour < 6):
        diff = t1 - t0
        noct_minutes = diff.seconds // 60
        return noct_minutes, diur_minutes

    # case 2: call started and finished between 06:00 and 21:59
    if (6 <= t0.hour < 22) and (6 <= t1.hour < 22):
        diff = t1 - t0
        diur_minutes = diff.seconds // 60
        return noct_minutes, diur_minutes

    # case 3: call started and finished between 22:00 and 23:59
    if (22 <= t0.hour < 24) and (22 <= t1.hour < 24):
        diff = t1 - t0
        noct_minutes = diff.seconds // 60
        return noct_minutes, diur_minutes

    # case 4: call started before 06:00 and finished between 06:00 and 21:59
    if (t0.hour < 6) and (6 <= t1.hour < 22):
        noct_minutes = (MARK_06H - t0).seconds // 60
        diur_minutes = (t1 - MARK_06H).seconds // 60
        return noct_minutes, diur_minutes

    # case 5: call started between 06:00 and 21:59 and finished after 22:00
    if (6 <= t0.hour < 22) and (22 <= t1.hour):
        noct_minutes = (MARK_22H - t0).seconds // 60
        diur_minutes = (t1 - MARK_22H).seconds // 60
        return noct_minutes, diur_minutes

    # case 6: call started before 06:00 and finished after 22:00
    if (t0.hour < 6) and (22 <= t1.hour):
        noct_minutes = (MARK_06H - t0).seconds // 60
        noct_minutes += (t1 - MARK_22H).seconds // 60
        diur_minutes = MINUTES_16HOURS
        return noct_minutes, diur_minutes


def order_bill_by_value_asc(bill):
    for i in range(len(bill)-1):
        for j in range(i+1, len(bill)):
            if bill[j]['total'] > bill[i]['total']:
                bill[j], bill[i] = bill[i], bill[j]

    return bill


def calc_fare(nocturne, diurne):
    total = 0.36 + (diurne * 0.09)
    return total


def classify_by_phone_number(records):
    bill = {}
    for record in records:
        nocturne_min, diurne_min = calc_minutes_in_period(record['start'], record['end'])
        total = calc_fare(nocturne_min, diurne_min)
        if record['source'] in bill:
            bill[record['source']] = bill[record['source']] + total
        else:
            bill[record['source']] = total

    bill = [{'source': k, 'total': round(v, 2)} for k, v in bill.items()]

    return order_bill_by_value_asc(bill)


if __name__ == "__main__":
    result = classify_by_phone_number(records)
    print(result)