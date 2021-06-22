# Generated by Django 3.2.3 on 2021-06-21 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pricipal', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Students', to='basic_app.school')),
            ],
        ),
    ]