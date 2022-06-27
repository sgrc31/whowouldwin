from django.db import models

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
