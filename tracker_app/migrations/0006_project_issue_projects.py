# Generated by Django 4.1.6 on 2023-03-10 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0005_status_remove_issue_types_remove_type_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(verbose_name='Дата и время создания')),
                ('completed_at', models.DateField(blank=True, null=True, verbose_name='Дата и время окончания')),
                ('name', models.CharField(default='No name', max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=3000, verbose_name='описание')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='projects',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='issues', to='tracker_app.project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]
