from django.db import models

# просто зарисовочки на будущее


class LawVoting(models.Model):
    title = models.TextField()  # название закона
    vote_date = models.DateField()

    appearance_v = models.SmallIntegerField()  # количество отданных голосов

    overall_accept_v = models.FloatField()  # доля "за" от appearance_v
    overall_denied_v = models.FloatField()  # доля "против"
    overall_refrain_v = models.FloatField()  # доля "воздержался"

    overall_absent_v = models.FloatField()  # процент не голосовавших
    overall_appearance_v = models.FloatField()  # явка

    def __str__(self):
        return self.title


class Faction(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()

    logo = models.CharField(max_length=100)  # logo file path here
    color1 = models.CharField(max_length=7)
    color2 = models.CharField(max_length=7)  # colors for card rendering

    av_accept = models.FloatField()  # процент "за" в голосованиях депутатов партии
    av_denied = models.FloatField()  # процент "против"
    av_refrain = models.FloatField()  # процент "воздержался"

    av_appearance = models.FloatField()  # средний процент присутствующих депутатов фракции
    av_absent = models.FloatField()  # средний процент неявки депутатов фракции

    protest_level = models.FloatField()  # оппозиционность партии

    votes = models.ManyToManyField(LawVoting, through='FactionVotes')

    # Faction.Deputy_set - для работы с депутатами конкретной партии
    def __str__(self):
        return self.name


class FactionVotes(models.Model):

    f_appearance_v = models.SmallIntegerField()  # Количество голосов от партии в этом голосовании

    av_accept_v = models.FloatField()  # доля "за" от f_appearance
    av_denied_v = models.FloatField()  # доля "против"
    av_refrain_v = models.FloatField()  # доля "воздержался"

    absent_v = models.FloatField()  # процент отсутствующих депутатов партии
    # appearance_v = models.FloatField()  # процент присутствующих депутатов партии (может понадобится)

    faction = models.ForeignKey(Faction)
    law_voting = models.ForeignKey(LawVoting)

    def __str__(self):
        return self.vote


class Deputy(models.Model):

    name = models.CharField(max_length=40)
    faction = models.ForeignKey(Faction)

    votes = models.ManyToManyField(LawVoting, through='DeputyVote')

    lifetime = models.SmallIntegerField() # количество голосований, в которых он указан как депутат
    appearance = models.SmallIntegerField()  # количество голосований, в которых он участвовал
    absent_number = models.SmallIntegerField()  # количество пропусков депутата

    accept = models.FloatField()  # процент голосований, в которых депутат участвовал
    denied = models.FloatField()  # (и это важно!) и проголосовал "за", "против" и
    refrain = models.FloatField() # воздержался от голосования соответственно

    absent_percentage = models.FloatField()  # процент голосований, в которых депутат не участвовал
    appearance_percentage = models.FloatField()  # процент голосований, в которых депутат участвовал

    protest_level = models.FloatField()  # оппозиционность (проценты)
    faction_protest_level = models.FloatField()  # оппозиционность относительно партии

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'deputies'


class DeputyVote(models.Model):

    vote = models.CharField(max_length=7)  # TODO: maybe add choices to CharField

    deputy = models.ForeignKey(Deputy)
    law_voting = models.ForeignKey(LawVoting)

    def __str__(self):
        return self.vote


class OverallStats(models.Model):

    appearance = models.IntegerField()  # общее количество отданных голосов

    overall_accept = models.FloatField()  # доля "за" от appearance
    overall_denied = models.FloatField()  # доля "против"
    overall_refrain = models.FloatField()  # доля "воздержался"

    overall_absent = models.FloatField()  # процент не голосовавших
    overall_appearance = models.FloatField()  # явка
