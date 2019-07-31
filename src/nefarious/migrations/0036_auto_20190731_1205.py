# Generated by Django 2.1.5 on 2019-07-31 12:05

from django.db import migrations
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0035_auto_20190730_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keywordsearchfilters',
            name='settings',
        ),
        migrations.AddField(
            model_name='nefarioussettings',
            name='keyword_filters',
            field=jsonfield.fields.JSONField(blank=True, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={}, null=True),
        ),
        migrations.DeleteModel(
            name='KeywordSearchFilters',
        ),
    ]