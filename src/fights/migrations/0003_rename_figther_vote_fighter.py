# Generated by Django 4.0.5 on 2022-06-27 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fights', '0002_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='figther',
            new_name='fighter',
        ),
    ]
