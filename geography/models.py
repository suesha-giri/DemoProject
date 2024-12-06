from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_obsolete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Country(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class City(TimeStampedModel):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    country = models.ForeignKey(Country, related_name="cities", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'country')  # To prevent duplicate city names within the same country
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name}, {self.country.name}"