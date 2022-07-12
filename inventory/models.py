from django.db import models

# Create your models here.


class Device(models.Model):
    type = models.CharField(max_length=101, blank=False)
    price = models.IntegerField()

    choices = (
        ("AVAILABLE", "Item ready to be purchased"),
        ("SOLD", "Item Sold"),
        ("RESTOCKING", "Item restocking in few days"),
    )

    status = models.CharField(max_length=15, choices=choices, default="SOLD")
    issues = models.CharField(max_length=101, default="No issues")

    def __str__(self):
        return "Type: {0} Price: {1}".format(self.type, self.price)

    class Meta:
        abstract = True


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
