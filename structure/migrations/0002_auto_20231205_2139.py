# Generated by Django 3.1.13 on 2023-12-05 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='collections_imgs'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='year',
            field=models.DateField(blank=True, unique_for_year=True),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]