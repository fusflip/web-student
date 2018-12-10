# Generated by Django 2.1.1 on 2018-12-10 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('filename', models.CharField(max_length=100)),
                ('size', models.FloatField()),
                ('extension', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('createDate', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('setType', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=50)),
                ('regDate', models.DateTimeField()),
                ('roleId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='back.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('status', models.IntegerField()),
                ('authorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='back.User')),
                ('paperId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.Paper')),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='authorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='back.User'),
        ),
    ]