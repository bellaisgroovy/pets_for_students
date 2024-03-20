# Generated by Django 2.1.5 on 2024-03-20 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('noCats', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='ownerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets_for_students.Student'),
        ),
    ]