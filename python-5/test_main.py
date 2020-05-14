from datetime import datetime

from main import classify_by_phone_number, records, order_bill_by_value_asc, \
                 calc_minutes_in_period


class TestChallenge1:

    def test_len(self):
        result = classify_by_phone_number(records)
        # len will change only if there are invalid records
        valid_records = 0
        for rec in records:
            t0 = datetime.fromtimestamp(rec['start'])
            t1 = datetime.fromtimestamp(rec['end'])
            if t0.year == t1.year and t0.month == t1.month and t0.day == t1.day:
                valid_records += 1
        assert len(result) == valid_records

    def test_order_bill_by_value_asc(self):
        unordered = [
            {'total': 1.2},
            {'total': 2.2},
            {'total': 3.3},
            {'total': 1.1},
            {'total': 2.3},
        ]
        ordered = [
            {'total': 1.1},
            {'total': 1.2},
            {'total': 2.2},
            {'total': 2.3},
            {'total': 3.3},
        ]
        resutl = order_bill_by_value_asc(unordered)
        assert resutl == ordered

    def test_calc_minutes_in_period_nocturne_or_diurne(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546314000,
                'start': 1546313400,
                'nocturne': 10,
                'diurne': 0,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546322455,
                'start': 1546322405,
                'nocturne': 0,
                'diurne': 0,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546330255,
                'start': 1546329600,
                'nocturne': 0,
                'diurne': 10,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546359005,
                'start': 1546355718,
                'nocturne': 0,
                'diurne': 54,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546394399,
                'start': 1546387200,
                'nocturne': 119,
                'diurne' : 0,
            },
            {
                'source': '41-885633788',
                'destination': '41-886383097',
                'end': 1546393679,
                'start': 1546392845,
                'nocturne': 13,
                'diurne': 0,
            },
        ]

        for rec in local_records:
            noc_min, diu_min = calc_minutes_in_period(rec['start'], rec['end'])
            assert noc_min == rec['nocturne']
            assert diu_min == rec['diurne']

    def test_calc_minutes_in_period_nocturne_and_diurne(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546330439,
                'start': 1546329315,
                'nocturne': 5,
                'diurne': 13,
            },
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546331400,
                'start': 1546327800,
                'nocturne': 30,
                'diurne': 30,
            },
        ]

        for rec in local_records:
            noc_min, diu_min = calc_minutes_in_period(rec['start'], rec['end'])
            assert noc_min == rec['nocturne']
            assert diu_min == rec['diurne']

    def test_calc_minutes_in_period_diurne_and_nocturne(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546387260,
                'start': 1546387140,
                'nocturne': 1,
                'diurne': 1,
            },
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546389000,
                'start': 1546385400,
                'nocturne': 30,
                'diurne': 30,
            },
        ]

        for rec in local_records:
            noc_min, diu_min = calc_minutes_in_period(rec['start'], rec['end'])
            assert noc_min == rec['nocturne']
            assert diu_min == rec['diurne']

    def test_calc_minutes_in_period_nocturne_and_nocturne(self):
        local_records = [
            {
                'source': '48-996355555',
                'destination': '48-666666666',
                'end': 1546387500,
                'start': 1546329300,
                'nocturne': 10,
                'diurne': 960,
            },
            # {
            #     'source': '48-996355555',
            #     'destination': '48-666666666',
            #     'end': 1546389000,
            #     'start': 1546385400,
            #     'nocturne': 30,
            #     'diurne': 30,
            # },
        ]

        for rec in local_records:
            noc_min, diu_min = calc_minutes_in_period(rec['start'], rec['end'])
            assert noc_min == rec['nocturne']
            assert diu_min == rec['diurne']