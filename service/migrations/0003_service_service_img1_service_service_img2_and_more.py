# Generated by Django 5.0.2 on 2024-04-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_service_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_img1',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='service/'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_img2',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='service/'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_img3',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='service/'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_img4',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='service/'),
        ),
    ]
