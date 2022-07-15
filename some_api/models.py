from django.db import models


class Some_Table(models.Model):
    test = models.CharField(max_length=100)

    def __str__(self):
        return self.test
