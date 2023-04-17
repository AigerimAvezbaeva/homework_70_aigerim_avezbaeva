# Generated by Django 4.1.6 on 2023-04-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0010_alter_issue_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, max_length=3000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issues', to='tracker_app.project', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issues', to='tracker_app.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='summary',
            field=models.CharField(blank=True, default='Задача', max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.ManyToManyField(related_name='issues', to='tracker_app.type', verbose_name='Тип'),
        ),
    ]
