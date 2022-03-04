# Generated by Django 3.2.8 on 2022-02-22 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reagents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='begining',
            name='confirmed_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='begining',
            name='expires_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ending',
            name='date_finished',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reagent',
            name='finish',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reagents.ending'),
        ),
        migrations.AlterField(
            model_name='reagent',
            name='ingredient01',
            field=models.ManyToManyField(blank=True, null=True, related_name='_Reagents_reagent_ingredient01_+', to='Reagents.Reagent'),
        ),
        migrations.AlterField(
            model_name='reagent',
            name='preparation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reagents.begining'),
        ),
    ]