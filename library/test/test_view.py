from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from library.models import Books, Categories


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        res = self.client.get('/')
        self.assertEquals(res.status_code, 200)
        self.assertContains(res, 'Search by')

    def test_search_route(self):
        res = self.client.get(reverse('library:search'))
        self.assertEquals(res.status_code, 200)

    def test_search_route(self):
        data = {'search': 'e', 'category': 'title'}
        res = self.client.get(reverse('library:search'), data=data)
        self.assertEquals(res.status_code, 200)

    def test_search_for_partial_title(self):
        category = Categories(name="novel")
        category.save()
        books = Books(title="motha", category=category)
        books.save()
        data = {'search': 'mo', 'filter': 'title'}
        res = self.client.get(reverse('library:search'), data=data)
        self.assertEquals(res.status_code, 200)
        self.assertContains(res, 'motha')

    def test_search_for_partial_category(self):
        category = Categories(name="novel")
        category.save()
        books = Books(title="mothers ", category=category)
        books.save()
        data = {'search': 'no', 'filter': 'category'}
        res = self.client.get(reverse('library:search'), data=data)
        self.assertEquals(res.status_code, 200)
        self.assertNotContains(res, 'mothers')

    def test_add_Books_view(self):
        data = {
            'title': 'sample book',
            'category_id': 1
        }
        res = self.client.get(reverse('library:book'), data=data)
        path=res.request.get('PATH_INFO')
        self.assertEquals(res.status_code,200)
        self.assertEquals(path, reverse('library:book'))
