# Generated by Django 3.1.7 on 2022-09-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100, verbose_name='User_Name')),
                ('phone_number', models.IntegerField(max_length=10, verbose_name='Phone_Number')),
                ('user_img', models.FileField(upload_to=None)),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('registered', models.BooleanField(default=0)),
            ],
        ),
    ]
