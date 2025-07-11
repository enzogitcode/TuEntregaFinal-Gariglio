# Generated by Django 5.2.4 on 2025-07-09 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('author_last_name', models.CharField(max_length=100)),
                ('author_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, default=list)),
                ('date_of_publication', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('resume', models.CharField(max_length=500)),
                ('text_article', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('author_last_name', models.CharField(max_length=100)),
                ('author_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.CharField(max_length=500)),
                ('text_paper', models.TextField()),
                ('date_of_publication', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('college', models.CharField(max_length=100)),
                ('career', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('course', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
