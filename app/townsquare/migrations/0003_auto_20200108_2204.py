# Generated by Django 2.2.4 on 2020-01-08 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0011_auto_20191106_0237'),
        ('townsquare', '0002_auto_20200107_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offers', to='kudos.Token'),
        ),
        migrations.AddField(
            model_name='offer',
            name='style',
            field=models.CharField(choices=[('announce1', 'announce1'), ('announce2', 'announce2'), ('announce3', 'announce3'), ('announce4', 'announce4')], db_index=True, default='announce1', max_length=50),
        ),
    ]