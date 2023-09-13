from django.db import models

class person(models.Model):
    Name = models.CharField(max_length=100, null=False, blank=True,unique=True)
    date_time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.Name