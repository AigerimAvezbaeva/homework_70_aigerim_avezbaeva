# Generated by Django 4.1.6 on 2023-04-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0009_issue_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата и время удаления'),
        ),
    ]
