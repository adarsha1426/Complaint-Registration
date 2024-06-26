# Generated by Django 5.0.6 on 2024-05-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Traffic Violation', 'Traffic Violation'), ('Delayed Services', 'Delayed Services'), ('Service Quality', 'Service Quality'), ('Service Denial', 'Service Denial'), ('Missuse of Funds', 'Missuse of Funds'), ('Road and Transportatoin Issues', 'Road and Transportation Issues'), ('Healthcare Services', 'Healthcare Services'), ('Misconduct Allegations', 'Misconduct Allegations'), ('Abuse of Power', 'Abuse of Power'), ('Other', 'Other')], max_length=100)),
                ('action_taken', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='base_compla_name_7fd254_idx')],
            },
        ),
    ]
