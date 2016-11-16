from django.db import models
from django.core.urlresolvers import reverse


class Timemixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Categories(Timemixin):
    '''
        Handles the categories
    '''
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "{}".format(self.name)


class Books(Timemixin):
    '''
        Handles Books Data
    '''
    title = models.CharField(max_length=32, unique=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('library:index')





