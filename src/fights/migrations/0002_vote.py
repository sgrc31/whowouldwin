# Generated by Django 4.0.5 on 2022-06-27 15:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('fight', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='fights.fight')),
                ('figther', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='fights.fighter')),
            ],
        ),
    ]
