# Generated by Django 5.1.4 on 2024-12-13 17:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artwork',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.collection'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.year'),
        ),
    ]
