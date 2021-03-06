# Generated by Django 3.0.4 on 2020-03-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0007_psn_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
