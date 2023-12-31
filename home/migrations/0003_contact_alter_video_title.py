# Generated by Django 4.1.5 on 2023-01-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_caption_video_title_remove_video_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
