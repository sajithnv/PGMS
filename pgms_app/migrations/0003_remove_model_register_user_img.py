# Generated by Django 3.1.7 on 2022-09-02 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgms_app', '0002_auto_20220902_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_register',
            name='user_img',
        ),
    ]
