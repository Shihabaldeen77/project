# Generated by Django 3.2.14 on 2022-07-06 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='jop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='applay_job', to='job.job'),
            preserve_default=False,
        ),
    ]
