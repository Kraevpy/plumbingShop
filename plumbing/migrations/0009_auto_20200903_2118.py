# Generated by Django 3.1.1 on 2020-09-03 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plumbing', '0008_auto_20200903_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='child',
            field=models.ManyToManyField(blank=True, to='plumbing.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_field', to='plumbing.category'),
        ),
    ]
