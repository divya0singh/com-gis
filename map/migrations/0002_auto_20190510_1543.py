# Generated by Django 2.2.1 on 2019-05-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layers',
            name='select_theme',
            field=models.CharField(choices=[('NON', 'None'), ('CEN', 'Census'), ('EDU', 'Education'), ('RUL', 'Rural'), ('WAT', 'Water'), ('HEL', 'Health'), ('OTH', 'Other')], default='None', max_length=6),
        ),
        migrations.AlterField(
            model_name='layers',
            name='style_file_available',
            field=models.CharField(choices=[('NON', 'None'), ('Y', 'Yes'), ('N', 'No')], default='None', max_length=2),
        ),
        migrations.AlterField(
            model_name='layers',
            name='types',
            field=models.CharField(choices=[('NON', 'None'), ('GJ', 'GeoJSON'), ('EL', 'Excel'), ('CV', 'CSV'), ('GL', 'GML'), ('ZS', 'Zipped Shapefile'), ('KL', 'KML'), ('PF', 'PDF'), ('TF', 'TIF'), ('PG', 'PNG'), ('JG', 'JPEG')], default='None', max_length=6),
        ),
    ]
