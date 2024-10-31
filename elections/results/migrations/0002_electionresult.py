# Generated by Django 5.0.6 on 2024-10-31 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionResult',
            fields=[
                ('election_result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('votes', models.PositiveIntegerField(default=0)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.party')),
                ('polling_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.pollingunit')),
            ],
            options={
                'unique_together': {('polling_unit', 'party')},
            },
        ),
    ]