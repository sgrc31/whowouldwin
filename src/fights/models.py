from django.db import models
from django.utils import timezone

from django_extensions.db.fields import ShortUUIDField

class Fighter(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    powers = models.TextField()

    def __str__(self):
        return self.name

class Fight(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    fighter1 = models.ForeignKey(Fighter,
                                 on_delete=models.CASCADE,
                                 related_name='first_contender',
                                 default=1
                                 )
    fighter2 = models.ForeignKey(Fighter,
                                 on_delete=models.CASCADE,
                                 related_name='second_contender',
                                 default=1
                                 )
    small_uuid = ShortUUIDField(editable=False)

    def __str__(self):
        return f'{self.name} - {self.fighter1.name} vs {self.fighter2.name}'


class Vote(models.Model):
    fight = models.ForeignKey(Fight,
                              on_delete=models.CASCADE,
                              related_name='votes',
                              default=1,
                              )
    fighter = models.ForeignKey(Fighter,
                                on_delete=models.CASCADE,
                                related_name='votes',
                                default=1
                                )
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.fight.name} - {self.fighter}'
