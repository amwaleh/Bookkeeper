from django.test import TestCase
from library.models import Categories, Books


class TestModels(TestCase):
    def setUp(self):
        self.data = "sports"
        self.category = Categories(name=self.data)
        self.category.save()

    def test_add_record_to_category(self):
        res = Categories.objects.all().first()
        self.assertEquals(self.data, res.name)

    def test_insert_into_Books(self):
        title = "world"
        res = Books(title=title, category=self.category)
        res.save()
        count = Books.objects.count()
        self.assertEquals(count,1)




