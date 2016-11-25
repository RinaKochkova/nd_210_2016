from django.db import models

# просто зарисовочки на будущее


class Faction(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.name


class Deputy(models.Model):
    name = models.CharField(max_length=40)
    faction = models.ForeignKey(Faction)
    # accept/decline relation - float
    # important projects

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'deputies'


# Create your models here.
