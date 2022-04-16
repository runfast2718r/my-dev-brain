# Generated by Django 4.0.3 on 2022-04-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userStories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='status',
            field=models.CharField(choices=[('ID', 'Ideated'), ('P', 'Planned'), ('IP', 'In Progress'), ('IT', 'In Test'), ('D', 'Done')], default='ID', max_length=2),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]