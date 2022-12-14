# Generated by Django 4.0.6 on 2022-07-29 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publicada')),
                ('corpo', models.TextField()),
                ('publicada', models.DateField(default=django.utils.timezone.now)),
                ('criada', models.DateTimeField(auto_now_add=True)),
                ('atualizada', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicadas', 'Publicadas')], default='rascunho', max_length=10)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'post',
                'ordering': ('-publicada',),
            },
        ),
    ]
