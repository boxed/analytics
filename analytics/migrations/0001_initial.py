# Generated by Django 2.2.5 on 2019-09-25 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.URLField()),
                ('count', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PageCounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.URLField(db_index=True)),
                ('count', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Referrers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.URLField(db_index=True)),
                ('referrer', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAgents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(db_index=True, max_length=200)),
                ('count', models.BigIntegerField(default=0)),
            ],
        ),
    ]
