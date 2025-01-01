# Generated by Django 5.1.3 on 2024-12-31 07:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('tag', '0002_rename_tag_tag_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_wise_posts', to='category.subsubcategory')),
                ('related_article', models.ManyToManyField(blank=True, null=True, to='post.post')),
                ('tag', models.ManyToManyField(to='tag.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='post.post')),
            ],
            options={
                'unique_together': {('post', 'user')},
            },
        ),
    ]
