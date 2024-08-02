# Generated by Django 5.0.7 on 2024-08-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('movieTitle', models.CharField(max_length=39)),
                ('director', models.CharField(max_length=40)),
                ('review_content', models.CharField(max_length=35)),
                ('rating', models.IntegerField()),
                ('created_da', models.DateField()),
                ('review_email_id', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=39)),
                ('genres', models.CharField(max_length=49)),
            ],
        ),
    ]
