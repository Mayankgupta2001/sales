# Generated by Django 5.0.4 on 2024-06-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menpageapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='men_poster_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_img', models.CharField(max_length=50)),
            ],
        ),
    ]