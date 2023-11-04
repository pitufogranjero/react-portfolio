from django.db import models

class projects(models.Model):

    name = models.CharField(max_length=255,null=False)
    hard = models.IntegerField(default=7)
    url = models.CharField(max_length=255)
    img = models.CharField(max_length=255, null=True)
    type_id = models.IntegerField(max_length=3, null=True)

    def __str__(self):
        return self.name

class types(models.Model):

    type = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
    