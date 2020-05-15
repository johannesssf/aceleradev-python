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
    """Calculates minutes
    """
    call_start = datetime.fromtimestamp(start)
    call_end = datetime.fromtimestamp(end)
    MARK_06H = datetime(call_start.year,
                        call_start.month,
                        call_start.day, 6, 0, 0)

    MARK_22H = datetime(call_start.year,
                        call_start.month,
                        call_start.day, 22, 0, 0)

    MINUTES_16HOURS = 16 * 60
    noct_minutes = 0
    diur_minutes = 0

    # case 1: call started and finished between 0h and 6h
    if (0 <= call_start.hour < 6) and (0 <= call_end.hour < 6):
        diff = call_end - call_start
        noct_minutes = diff.seconds // 60
        return noct_minutes, diur_minutes

    # case 2: call started and finished between 6h and 22h
    if (6 <= call_start.hour < 22) and (6 <= call_end.hour < 22):
        diff = call_end - call_start
        diur_minutes = diff.seconds // 60
        return noct_minutes, diur_minutes

    # case 3: call started and finished between 22h and 24h
    if (22 <= call_start.hour < 24) and (22 <= call_end.hour < 24):
        diff = call_end - call_start
        noct_minutes = diff.seconds // 60
        return noct_minutes, diur_minutes

    # case 4: call started before 6h and finished between 6h and 21h
    if (call_start.hour < 6) and (6 <= call_end.hour < 22):
        noct_minutes = (MARK_06H - call_start).seconds // 60
        diur_minutes = (call_end - MARK_06H).seconds // 60
        return noct_minutes, diur_minutes

    # case 5: call started between 6h and 22 and finished after 22h
    if (6 <= call_start.hour < 22) and (22 <= call_end.hour):
        noct_minutes = (MARK_22H - call_start).seconds // 60
        diur_minutes = (call_end - MARK_22H).seconds // 60
        return noct_minutes, diur_minutes

    # case 6: call started before 6h and finished after 22h
    if (call_start.hour < 6) and (22 <= call_end.hour):
        noct_minutes = (MARK_06H - call_start).seconds // 60
        noct_minutes += (call_end - MARK_22H).seconds // 60
        diur_minutes = MINUTES_16HOURS
        return noct_minutes, diur_minutes

    # if we get here, probably it's an invalid record
    return noct_minutes, diur_minutes


def order_bill_by_value_desc(bill):
    for i in range(len(bill)-1):
        for j in range(i+1, len(bill)):
            if bill[j]['total'] > bill[i]['total']:
                bill[j], bill[i] = bill[i], bill[j]

    return bill


def calc_fare(minutes):
    """Calcultes the fare according to call duration.

    We have a fixed value for all calls and an extra value for each
    minute.
    """
    total = 0.36 + (minutes * 0.09)
    return total


def classify_by_phone_number(records):
    bill = {}
    for record in records:
        noct, diur = calc_minutes_in_period(record['start'], record['end'])
        total = calc_fare(diur)

        if record['source'] in bill:
            bill[record['source']] = bill[record['source']] + total
        else:
            bill[record['source']] = total

    bill = [{'source': key, 'total': round(val, 2)}
            for key, val in bill.items()]

    return order_bill_by_value_desc(bill)


if __name__ == "__main__":
    result = classify_by_phone_number(records)
