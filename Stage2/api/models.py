from django.db import models

class Location(models.Model):
    locationName = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.locationName
class Item (models.Model):
    itemName = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName