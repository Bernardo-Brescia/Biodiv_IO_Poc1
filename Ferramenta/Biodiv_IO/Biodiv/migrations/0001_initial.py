# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-13 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amostra',
            fields=[
                ('amostra_id', models.IntegerField(db_column='Amostra_ID', primary_key=True, serialize=False)),
                ('lagoa', models.CharField(blank=True, max_length=45, null=True)),
                ('dia', models.IntegerField(blank=True, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('profundidade', models.FloatField(blank=True, null=True)),
                ('cod_profundidade', models.FloatField(blank=True, null=True)),
                ('hora', models.CharField(blank=True, max_length=45, null=True)),
                ('secchi', models.CharField(blank=True, max_length=45, null=True)),
                ('responsavel', models.CharField(blank=True, max_length=45, null=True)),
                ('obs', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'Amostra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxa', models.CharField(db_column='Taxa', max_length=60)),
                ('ordem', models.CharField(blank=True, db_column='Ordem', max_length=45, null=True)),
                ('familia', models.CharField(blank=True, db_column='Familia', max_length=45, null=True)),
                ('classe', models.CharField(blank=True, db_column='Classe', max_length=45, null=True)),
                ('divisao', models.CharField(blank=True, db_column='Divisao', max_length=45, null=True)),
                ('epiteto_especifico', models.CharField(blank=True, db_column='Epiteto_Especifico', max_length=45, null=True)),
                ('epiteto_subespecifico', models.CharField(blank=True, db_column='Epiteto_Subespecifico', max_length=45, null=True)),
                ('caracteristica', models.CharField(blank=True, db_column='Caracteristica', max_length=45, null=True)),
                ('conferir', models.IntegerField(blank=True, db_column='Conferir', null=True)),
                ('contagem', models.IntegerField(blank=True, db_column='Contagem', null=True)),
                ('vol_sedimentado', models.FloatField(blank=True, db_column='Vol_Sedimentado', null=True)),
                ('biovolume_um3', models.FloatField(blank=True, db_column='Biovolume_um3', null=True)),
                ('mm3_l', models.FloatField(blank=True, db_column='mm3_L', null=True)),
                ('ind_l', models.FloatField(blank=True, db_column='Ind_L', null=True)),
                ('a_camara', models.FloatField(blank=True, db_column='A_Camara', null=True)),
                ('a_campo', models.FloatField(blank=True, db_column='A_Campo', null=True)),
                ('n_campo', models.FloatField(blank=True, db_column='N_Campo', null=True)),
            ],
            options={
                'db_table': 'Fito',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Zoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxa', models.CharField(db_column='Taxa', max_length=60)),
                ('ordem', models.CharField(blank=True, db_column='Ordem', max_length=45, null=True)),
                ('familia', models.CharField(blank=True, db_column='Familia', max_length=45, null=True)),
                ('grupo', models.CharField(blank=True, db_column='Grupo', max_length=45, null=True)),
                ('filo', models.CharField(blank=True, db_column='Filo', max_length=45, null=True)),
                ('epiteto_especifico', models.CharField(blank=True, db_column='Epiteto_Especifico', max_length=45, null=True)),
                ('epiteto_subespecifico', models.CharField(blank=True, db_column='Epiteto_Subespecifico', max_length=45, null=True)),
                ('caracteristica', models.CharField(blank=True, db_column='Caracteristica', max_length=45, null=True)),
                ('conferir', models.IntegerField(blank=True, db_column='Conferir', null=True)),
                ('contagem', models.IntegerField(blank=True, db_column='Contagem', null=True)),
                ('vol_sedimentado', models.FloatField(blank=True, db_column='Vol_Sedimentado', null=True)),
                ('biovolume_um3', models.FloatField(blank=True, db_column='Biovolume_um3', null=True)),
                ('vol_fil_l', models.FloatField(blank=True, db_column='Vol_Fil_L', null=True)),
                ('vol_cont_l', models.FloatField(blank=True, db_column='Vol_Cont_L', null=True)),
                ('mm3', models.FloatField(blank=True, null=True)),
                ('ind_l', models.FloatField(blank=True, db_column='Ind_L', null=True)),
            ],
            options={
                'db_table': 'Zoo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LagoaInfoAmostra',
            fields=[
                ('amostra_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Biodiv.Amostra')),
                ('ph', models.FloatField(blank=True, db_column='PH', null=True)),
                ('cond_us_cm', models.FloatField(blank=True, db_column='cond_uS_cm', null=True)),
                ('turb_ntu', models.FloatField(blank=True, db_column='turb_NTU', null=True)),
                ('od_mg_l', models.FloatField(blank=True, db_column='OD_mg_L', null=True)),
                ('temp_oc', models.FloatField(blank=True, db_column='Temp_oC', null=True)),
                ('tds_mg_l', models.FloatField(blank=True, db_column='TDS_mg_L', null=True)),
                ('redoxe', models.FloatField(blank=True, db_column='Redoxe', null=True)),
                ('alc_meg_l', models.FloatField(blank=True, db_column='Alc_meg_L', null=True)),
                ('chla_ug_l', models.FloatField(blank=True, db_column='Chla_ug_L', null=True)),
                ('p_tot_ug_l', models.FloatField(blank=True, db_column='P-tot_ug_L', null=True)),
                ('po4_ug_l', models.FloatField(blank=True, db_column='PO4_ug_L', null=True)),
                ('n_tot_ug_l', models.FloatField(blank=True, db_column='N-tot_ug_L', null=True)),
                ('nh4_ug_l', models.FloatField(blank=True, db_column='NH4_ug_L', null=True)),
                ('no3_ug_l', models.FloatField(blank=True, db_column='NO3_ug_L', null=True)),
                ('no2_ug_l', models.FloatField(blank=True, db_column='NO2_ug_L', null=True)),
                ('silicato_mg_l', models.FloatField(blank=True, db_column='Silicato_mg_L', null=True)),
            ],
            options={
                'db_table': 'Lagoa_Info_Amostra',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='zoo',
            name='amostra_id',
            field=models.ForeignKey(db_column='Amostra_ID', on_delete=django.db.models.deletion.CASCADE, to='Biodiv.Amostra'),
        ),
        migrations.AddField(
            model_name='fito',
            name='amostra_id',
            field=models.ForeignKey(db_column='Amostra_ID', on_delete=django.db.models.deletion.CASCADE, to='Biodiv.Amostra'),
        ),
        migrations.AlterUniqueTogether(
            name='zoo',
            unique_together=set([('amostra_id', 'taxa')]),
        ),
        migrations.AlterUniqueTogether(
            name='fito',
            unique_together=set([('amostra_id', 'taxa')]),
        ),
    ]
