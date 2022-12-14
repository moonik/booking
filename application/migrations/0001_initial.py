# Generated by Django 2.2 on 2019-04-18 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('street', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('stat_summary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HotelType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='HotelStatistic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=256)),
                ('positive', models.IntegerField()),
                ('negative', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Hotel')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.HotelType'),
        ),
        migrations.CreateModel(
            name='CommentMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=256)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Comment')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Hotel')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Hotel'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
