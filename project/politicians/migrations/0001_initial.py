# Generated by Django 4.2.6 on 2023-10-10 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('firstlast', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('first_elected', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('webform', models.CharField(max_length=100)),
                ('congress_office', models.CharField(max_length=100)),
                ('bioguide_id', models.CharField(max_length=100)),
                ('votesmart_id', models.CharField(max_length=100)),
                ('feccandid', models.CharField(max_length=100)),
                ('twitter_id', models.CharField(max_length=100)),
                ('youtube_url', models.CharField(max_length=100)),
                ('facebook_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle', models.CharField(default='2022', max_length=4)),
                ('origin', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('industry_code', models.CharField(max_length=6)),
                ('industry_name', models.CharField(max_length=200)),
                ('indivs', models.CharField(max_length=12)),
                ('pacs', models.CharField(max_length=12)),
                ('total', models.CharField(max_length=12)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politicians.politician')),
            ],
        ),
    ]
