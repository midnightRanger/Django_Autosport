from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    mass = models.FloatField()
    model = models.TextField(blank=True)
    mark = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    ENGINE_TYPE_CHOICES = [
        ("INLINE", "Inline"),
        ("V Engine", "V Engine"),
        ("VR Engine", "VR Engine"),
        ("W Engine", "W Engine")
    ]

    engine_type = models.CharField(
        default = "INLINE",
        choices= ENGINE_TYPE_CHOICES
    )

    def __str__(self):
        return self.name