# Generated by Django 4.2.1 on 2023-05-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0006_remove_actor_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(to='movies_app.actor'),
        ),
        migrations.DeleteModel(
            name='MovieActor',
        ),
    ]