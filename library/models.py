from django.db import models
from django.core.urlresolvers import reverse


class Timemixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Categories(Timemixin):
    '''
    Handles the Categories
    '''
    name = models.CharField(max_length=32)

    def __str__(self):
        return "{}".format(self.name)


class Books(Timemixin):
    '''
        Handles Books Data
    '''
    title = models.CharField(max_length=32)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('library:index')





