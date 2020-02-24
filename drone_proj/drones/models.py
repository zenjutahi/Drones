from django.db import models

# Create your models here.
class DroneCategory(models.Model):
    """DroneCategory Model"""
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Drone(models.Model):
    """Drone Model."""
    name = models.CharField(max_length=250)
    drone_category = models.ForeignKey(DroneCategory, related_name='drones', on_delete=models.CASCADE)
    manufacturing_date = models.DateField()
    it_has_completed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Pilot(models.Model):
    """Pilot Model."""
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )
    name = models.CharField(max_length=150, blank=False, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    races_count = models.IntegerField(default=0)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Competition(models.Model):
    """DroneCategory Model"""
    pilot = models.ForeignKey(
        Pilot,
        related_name='competitions',
        on_delete=models.CASCADE)
    drone = models.ForeignKey(
        Drone,
        on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateField()

    class Meta:
        ordering = ('-distance_in_feet',)

    def __str__(self):
        return self.name
