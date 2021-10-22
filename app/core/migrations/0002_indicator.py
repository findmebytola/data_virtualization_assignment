# Generated by Django 3.2.8 on 2021-10-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scorecard_name', models.CharField(max_length=255)),
                ('step', models.IntegerField()),
                ('milestone', models.CharField(max_length=255)),
                ('score', models.IntegerField(choices=[(0, 'Not yet achieved'), (1, 'Patially achieved'), (2, 'Fully achieved')])),
                ('narrative', models.TextField(max_length=700)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
