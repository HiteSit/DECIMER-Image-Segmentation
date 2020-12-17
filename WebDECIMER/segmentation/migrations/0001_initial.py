# Generated by Django 3.1.3 on 2020-11-17 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SegmentedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ori_image', models.ImageField(blank=True, max_length=500, upload_to='images')),
                ('bnw_image', models.ImageField(blank=True, max_length=500, upload_to='images')),
                ('clean_image', models.ImageField(blank=True, max_length=500, upload_to='images')),
                ('smiles', models.CharField(blank=True, max_length=500)),
                ('ori_article_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadedArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.FileField(upload_to='articles')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('path_to_segmented_images', models.CharField(blank=True, max_length=600)),
                ('all_segmented_images_names', models.TextField(blank=True)),
            ],
        ),
    ]
