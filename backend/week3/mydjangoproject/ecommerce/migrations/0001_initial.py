# Generated by Django 4.2.3 on 2023-07-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productIndex', models.IntegerField(default=0)),
                ('productName', models.CharField(max_length=200)),
                ('productPrice', models.IntegerField(default=0)),
                ('productDescription', models.CharField(max_length=200)),
            ],
        ),
    ]
