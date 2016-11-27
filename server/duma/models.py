from django.db import models

# просто зарисовочки на будущее


class Faction(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()  # do we really need it?

    logo = models.CharField(max_length=100)  # logo file path here
    color1 = models.CharField(max_length=7)
    color2 = models.CharField(max_length=7) # colors for card rendering

    # Faction.Deputy_set - для работы с депутатами конкретной партии

    def __str__(self):
        return self.name


class Deputy(models.Model):
    name = models.CharField(max_length=40)
    faction = models.ForeignKey(Faction)

    votes = models.ManyToManyField(Law_voting, through='Vote')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'deputies'


class Law_voting(models.Model):
    title = models.TextField()
    vote_date = models.DateField()

    def __str__(self):
        return self.title


class Vote(models.Model):  # TODO: maybe replace add choise to CharField
    vote = models.CharField(max_length=7)

    deputy = models.ForeignKey(Deputy)
    law_voting = models.ForeignKey(Law_voting)

    def __str__(self):
        return self.vote
