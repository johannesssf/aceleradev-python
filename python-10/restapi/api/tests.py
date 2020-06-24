from django.test import TestCase


class TestChallenge10(TestCase):
    def test_0(self):
        response = self.client.post(
            '/lambda/',
            {"question": [2, 3, 2, 4, 5, 12, 2, 3]},
            content_type='application/json'
        )
        assert isinstance(response.data, dict)
        self.assertEqual(response.status_code, 200)

    def test_01(self):
        response = self.client.post(
            '/lambda/',
            {"question": [2, 3, 2, 4, 5, 12, 2, 3]},
            content_type='application/json'
        )
        assert len(response.data['solution']) == 8
        self.assertEqual(response.status_code, 200)

    def test_post_without_question(self):
        response = self.client.post(
            '/lambda/',
            {'other-field':[2, 3, 2, 4, 5, 12, 2, 3]},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_question_without_a_list(self):
        response = self.client.post(
            '/lambda/',
            {'question': 'not a list value'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_question_solution(self):
        solution = [6, 6, 6, 6, 2, 2, 2, 1, 3]
        response = self.client.post(
            '/lambda/',
            {'question': [2, 2, 2, 6, 6, 6, 6, 1, 3]},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['solution'], solution)
