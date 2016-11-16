from django.test import  TestCase, Client


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        res = self.client.get('/')
        self.assertEquals(res.status_code,200)