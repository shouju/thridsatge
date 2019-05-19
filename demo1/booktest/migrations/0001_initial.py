# Generated by Django 2.2.1 on 2019-05-14 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Heroinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gendle', models.BooleanField(default=True)),
                ('skill', models.CharField(max_length=30, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.Bookinfo')),
            ],
        ),
    ]