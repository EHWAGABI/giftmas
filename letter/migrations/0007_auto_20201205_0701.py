# Generated by Django 3.0.7 on 2020-12-05 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0006_gift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='gift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letter.Gift'),
        ),
    ]