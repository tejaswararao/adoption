# Generated by Django 4.0.1 on 2022-03-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0007_alter_parent_contact1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='dateofbirth',
            field=models.DateField(auto_now=True),
        ),
    ]
