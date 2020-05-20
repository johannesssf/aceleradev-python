from datetime import datetime
from pprint import pprint

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


def calc_diurnal_minutes(start, end):
    """Calculates how many minutes occurred in the diurnal period in a
    phonecall. The diurnal period is between 6:00 and 22:00.

    Arguments:
        start {int} -- Starting timestamp
        end {int} -- Ending timestamp

    Returns:
        int -- minutes in diurnal period
    """
    call_start = datetime.fromtimestamp(start)
    call_end = datetime.fromtimestamp(end)
    MARK_06H = datetime(call_start.year,
                        call_start.month,
                        call_start.day, 6, 0, 0)

    MARK_22H = datetime(call_start.year,
                        call_start.month,
                        call_start.day, 22, 0, 0)

    MINUTES_IN_16HOURS = 16 * 60
    minutes = 0

    # case 1: call started and finished between 0h and 6h
    if (0 <= call_start.hour < 6) and (0 <= call_end.hour < 6):
        return minutes

    # case 2: call started and finished between 6h and 22h
    if (6 <= call_start.hour < 22) and (6 <= call_end.hour < 22):
        diff = call_end - call_start
        minutes = diff.seconds // 60
        return minutes

    # case 3: call started and finished between 22h and 24h
    if (22 <= call_start.hour < 24) and (22 <= call_end.hour < 24):
        return minutes

    # case 4: call started before 6h and finished between 6h and 21h
    if (call_start.hour < 6) and (6 <= call_end.hour < 22):
        minutes = (call_end - MARK_06H).seconds // 60
        return minutes

    # case 5: call started between 6h and 22 and finished after 22h
    if (6 <= call_start.hour < 22) and (22 <= call_end.hour):
        minutes = (call_end - MARK_22H).seconds // 60
        return minutes

    # case 6: call started before 6h and finished after 22h
    if (call_start.hour < 6) and (22 <= call_end.hour):
        return MINUTES_IN_16HOURS

    # if we get here, probably it's an invalid record
    return minutes


def order_bills_by_value_desc(bill):
    """Orders a list of bills by its totals in descending order.

    The elements of the list are dics in the following form:
    {'source': <source phone number>, 'total': <value>}

    Arguments:
        bill {list} -- Unordered list

    Returns:
        list -- Ordered list
    """
    for i in range(len(bill)-1):
        for j in range(i+1, len(bill)):
            if bill[j]['total'] > bill[i]['total']:
                bill[j], bill[i] = bill[i], bill[j]

    return bill


def calculate_bills(records):
    """Calculates the total expense for each source phone number.

    Each call has a fixed value of 0.36 for the call connection and an
    extra fare of 0.09 for each minute during the diurnal period
    comprehended from 6:00 to 22:00.

    For example:
    call started at 01/01/2000 5:55
    call ended at 01/01/2000 6:05 (5 minutes)
    total: 0.36 (fixed value) + 5 (diurnal) * 0.09 (extra fare)

    Arguments:
        records {list} -- Phone call records

    Returns:
        list -- Calculated bills ordered by values descending
    """
    bills = {}
    for record in records:
        minutes = calc_diurnal_minutes(record['start'], record['end'])
        total = 0.36 + (minutes * 0.09)

        if record['source'] in bills:
            bills[record['source']] = bills[record['source']] + total
        else:
            bills[record['source']] = total

    bills = [{'source': key, 'total': round(val, 2)}
             for key, val in bills.items()]

    return order_bills_by_value_desc(bills)


def classify_by_phone_number(records):
    """Calculates and classify a list of phone calls.

    Arguments:
        records {list} -- Phone call records list

    Returns:
        list -- List with the calculated totals
    """
    return calculate_bills(records)


if __name__ == "__main__":
    result = classify_by_phone_number(records)
    pprint(result)
