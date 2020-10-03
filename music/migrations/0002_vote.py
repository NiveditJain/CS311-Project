# Generated by Django 3.1.1 on 2020-09-28 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(choices=[(False, 'Downvote'), (True, 'Upvote')])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='music.music')),
            ],
        ),
    ]