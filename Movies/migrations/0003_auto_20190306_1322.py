# Generated by Django 2.1.5 on 2019-03-06 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0002_movies_rented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='rented',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Customer.Customer'),
        ),
    ]
