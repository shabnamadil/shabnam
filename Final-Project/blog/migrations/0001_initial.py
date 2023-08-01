# Generated by Django 4.1.7 on 2023-07-18 22:39

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_az', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_es', models.CharField(max_length=255, null=True)),
                ('blog', ckeditor_uploader.fields.RichTextUploadingField()),
                ('blog_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('blog_az', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('blog_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('blog_es', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('slug', models.SlugField(max_length=255, unique_for_date='published_at')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_name_en', models.CharField(max_length=200, null=True)),
                ('category_name_az', models.CharField(max_length=200, null=True)),
                ('category_name_ru', models.CharField(max_length=200, null=True)),
                ('category_name_es', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=250)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.blogcategory'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-created_at'], name='blog_commen_created_1f5393_idx'),
        ),
        migrations.AddIndex(
            model_name='blog',
            index=models.Index(fields=['-published_at'], name='blog_blog_publish_fd0506_idx'),
        ),
    ]
