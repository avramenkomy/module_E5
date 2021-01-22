from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.title

class Car(models.Model):

    GEAR_CHOICES = (
        ("Robot", "ROBOT_GEAR"),
        ("Automatic", "AUTOMATIC_GEAR"),
        ("Manual", "MANUAL_GEAR"),
    )

    manufacturer = models.ForeignKey(Manufacturer, related_name="cars", on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    gear = models.CharField(max_length=255, choices=GEAR_CHOICES, default="Manual")
    color = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='cars_photo', blank=True)
    small_photo = models.ImageField(upload_to='cars_photo/small', blank=True)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return str(self.manufacturer) + " " + str(self.model)
