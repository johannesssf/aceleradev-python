from datetime import datetime

from main import (
    calc_diurnal_minutes,
    calculate_bills,
    classify_by_phone_number,
    order_bills_by_value_desc,
    records,
)


class TestChallenge1:

    def test_len(self):
        result = classify_by_phone_number(records)
        assert len(result) == 6

    def test_order_bills_by_value_desc(self):
        unordered = [
            {'total': 1.2},
            {'total': 2.2},
            {'total': 3.3},
            {'total': 1.1},
            {'total': 2.3},
        ]
        ordered = [
            {'total': 3.3},
            {'total': 2.3},
            {'total': 2.2},
            {'total': 1.2},
            {'total': 1.1},
        ]
        resutl = order_bills_by_value_desc(unordered)
        assert resutl == ordered

    def test_calc_minutes_in_period_nocturne_or_diurne(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546314000,
                'start': 1546313400,
                'diurne': 0,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546322455,
                'start': 1546322405,
                'diurne': 0,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546330255,
                'start': 1546329600,
                'diurne': 10,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546359005,
                'start': 1546355718,
                'diurne': 54,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546394399,
                'start': 1546387200,
                'diurne' : 0,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546393679,
                'start': 1546392845,
                'diurne': 0,
            },
        ]

        for rec in local_records:
            minutes = calc_diurnal_minutes(rec['start'], rec['end'])
            assert minutes == rec['diurne']

    def test_calc_minutes_in_period_nocturne_and_diurne(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546330439,
                'start': 1546329315,
                'diurne': 13,
            },
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546331400,
                'start': 1546327800,
                'diurne': 30,
            },
        ]

        for rec in local_records:
            minutes = calc_diurnal_minutes(rec['start'], rec['end'])
            assert minutes == rec['diurne']

    def test_calc_minutes_in_period_diurne_and_nocturne(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546387260,
                'start': 1546387140,
                'diurne': 1,
            },
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546389000,
                'start': 1546385400,
                'diurne': 30,
            },
        ]

        for rec in local_records:
            minutes = calc_diurnal_minutes(rec['start'], rec['end'])
            assert minutes == rec['diurne']

    def test_calc_minutes_in_period_nocturne_and_nocturne(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546387500,
                'start': 1546329300,
                'diurne': 960,
            },
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546394399,
                'start': 1546308000,
                'diurne': 960,
            },
        ]

        for rec in local_records:
            minutes = calc_diurnal_minutes(rec['start'], rec['end'])
            assert minutes == rec['diurne']

    def test_calculate_bills(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1564610974,
                'start': 1564610674,
                'total': 0.81,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1564506121,
                'start': 1564504821,
                'total': 2.25,
            }
        ]
        bills = calculate_bills(local_records)
        assert bills[0]['total'] == local_records[1]['total']
        assert bills[1]['total'] == local_records[0]['total']
