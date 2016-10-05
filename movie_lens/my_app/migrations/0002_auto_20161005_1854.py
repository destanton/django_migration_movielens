# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 18:54
from __future__ import unicode_literals

from django.db import migrations
import csv


def add_item_rater_data(apps, schema_editor):
    Rater = apps.get_model("my_app", "Rater")
    Item = apps.get_model("my_app", "Item")
    Data = apps.get_model("my_app", "Data")
    with open('rater.csv') as infile:
        contents = csv.reader(infile, delimiter="|")
        for row in contents:
            Rater.objects.create(id=row[0], age=row[1], gender=row[2], occupation=row[3], zip_code=row[4])

    with open('item.csv') as infile:
        contents = csv.reader(infile, delimiter="|")
        for row in contents:
            print(row)
            Item.objects.create(id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3], imdb_url=row[4],
                                unknown=row[5], action=row[6], adventure=row[7], animation=row[8], children=row[9], com)

    raise Exception("BIG TOES!")


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_item_rater_data)
    ]