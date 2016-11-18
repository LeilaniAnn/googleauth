
# -*- coding: utf-8 -*-

from django.db import migrations, models
from django.core.management import call_command


def loadfixture(apps, schema_editor):
    call_command('loaddata', 'initial_data.json')


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(loadfixture),

    ]