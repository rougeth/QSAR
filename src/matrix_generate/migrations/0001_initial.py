# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import matrix_generate.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_dimension_x', models.IntegerField(default=3)),
                ('box_dimension_y', models.IntegerField(default=3)),
                ('box_dimension_z', models.IntegerField(default=3)),
                ('box_coordinate_x', models.IntegerField(default=0)),
                ('box_coordinate_y', models.IntegerField(default=0)),
                ('box_coordinate_z', models.IntegerField(default=0)),
                ('coo', models.BooleanField(verbose_name='COO-')),
                ('nh3', models.BooleanField(verbose_name='NH3+')),
                ('ch3', models.BooleanField(verbose_name='CH3-')),
                ('arc', models.BooleanField(verbose_name='Ar(C-H)')),
                ('oh', models.BooleanField(verbose_name='O-H')),
                ('nh2', models.BooleanField(verbose_name='NH2')),
                ('arn', models.BooleanField(verbose_name='Ar(N-H)')),
                ('c_o', models.BooleanField(verbose_name='C=O')),
                ('sh', models.BooleanField(verbose_name='SH')),
                ('nh2_arg', models.BooleanField(verbose_name='NH2(ARG)')),
                ('h2o', models.BooleanField(verbose_name='(H2O)HO')),
                ('zn2', models.BooleanField(verbose_name='Zn2+')),
                ('cl', models.BooleanField(verbose_name='Cl-')),
                ('na', models.BooleanField(verbose_name='Na+')),
            ],
        ),
        migrations.CreateModel(
            name='MatrixGenerate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number_of_molecules', models.IntegerField(default=1)),
                ('configured', models.BooleanField(default=False)),
                ('process_finished', models.BooleanField(default=False)),
                ('email_sent', models.BooleanField(default=False)),
                ('started', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Molecule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=matrix_generate.models.path_builder)),
                ('matrix_generate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matrix_generate.MatrixGenerate')),
            ],
        ),
        migrations.AddField(
            model_name='box',
            name='matrix_generate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matrix_generate.MatrixGenerate'),
        ),
    ]