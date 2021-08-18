# Generated by Django 3.2 on 2021-04-11 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='meadia/slider/%y/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]