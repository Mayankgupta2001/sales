# Generated by Django 5.0.4 on 2024-06-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menpageapp', '0004_men_product_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='men_bottom_poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottom_img', models.CharField(max_length=50)),
            ],
        ),
    ]
