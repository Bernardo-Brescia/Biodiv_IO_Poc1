from __future__ import unicode_literals
from django.db import models

class Amostra(models.Model):

	amostra_id = models.IntegerField(db_column='Amostra_ID', primary_key=True)  # Field name made lowercase.
	lagoa = models.CharField(max_length=45, blank=True, null=True)
	dia = models.IntegerField(blank=True, null=True)
	mes = models.IntegerField(blank=True, null=True)
	ano = models.IntegerField(blank=True, null=True)
	profundidade = models.FloatField(blank=True, null=True)
	cod_profundidade = models.FloatField(blank=True, null=True)
	hora = models.CharField(max_length=45, blank=True, null=True)
	secchi = models.CharField(max_length=45, blank=True, null=True)
	responsavel = models.CharField(max_length=45, blank=True, null=True)
	obs = models.CharField(max_length=120, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'Amostra'
	
	def __unicode__(self):
		return str(self.amostra_id)


class Fito(models.Model):

	amostra_id = models.ForeignKey(Amostra, on_delete=models.CASCADE, db_column='Amostra_ID')  # Field name made lowercase.
	taxa = models.CharField(db_column='Taxa', max_length=60)  # Field name made lowercase.
	ordem = models.CharField(db_column='Ordem', max_length=45, blank=True, null=True)  # Field name made lowercase.
	familia = models.CharField(db_column='Familia', max_length=45, blank=True, null=True)  # Field name made lowercase.
	classe = models.CharField(db_column='Classe', max_length=45, blank=True, null=True)  # Field name made lowercase.
	divisao = models.CharField(db_column='Divisao', max_length=45, blank=True, null=True)  # Field name made lowercase.
	epiteto_especifico = models.CharField(db_column='Epiteto_Especifico', max_length=45, blank=True, null=True)  # Field name made lowercase.
	epiteto_subespecifico = models.CharField(db_column='Epiteto_Subespecifico', max_length=45, blank=True, null=True)
	caracteristica = models.CharField(db_column='Caracteristica', max_length=45, blank=True, null=True)  # Field name made lowercase.
	conferir = models.IntegerField(db_column='Conferir', blank=True, null=True)  # Field name made lowercase.
	contagem = models.IntegerField(db_column='Contagem', blank=True, null=True)  # Field name made lowercase.
	vol_sedimentado = models.FloatField(db_column='Vol_Sedimentado', blank=True, null=True)  # Field name made lowercase.
	biovolume_um3 = models.FloatField(db_column='Biovolume_um3', blank=True, null=True)  # Field name made lowercase.
	mm3_l = models.FloatField(db_column='mm3_L', blank=True, null=True)  # Field name made lowercase.
	ind_l = models.FloatField(db_column='Ind_L', blank=True, null=True)  # Field name made lowercase.
	a_camara = models.FloatField(db_column='A_Camara', blank=True, null=True)  # Field name made lowercase.
	a_campo = models.FloatField(db_column='A_Campo', blank=True, null=True)  # Field name made lowercase.
	n_campo = models.FloatField(db_column='N_Campo', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = True
		db_table = 'Fito'
		unique_together = (('amostra_id', 'taxa'),)

	def Data(self):
		data = (str(self.amostra_id.dia), str(self.amostra_id.mes), str(self.amostra_id.ano))
		return '/'.join(data)
		
	def __unicode__(self):
		return str(self.amostra_id.amostra_id)



class LagoaInfoAmostra(models.Model):

	amostra_id = models.OneToOneField(Amostra, on_delete=models.CASCADE, primary_key=True)  # Field name made lowercase.
	ph = models.FloatField(db_column='PH', blank=True, null=True)  # Field name made lowercase.
	cond_us_cm = models.FloatField(db_column='cond_uS_cm', blank=True, null=True)  # Field name made lowercase.
	turb_ntu = models.FloatField(db_column='turb_NTU', blank=True, null=True)  # Field name made lowercase.
	od_mg_l = models.FloatField(db_column='OD_mg_L', blank=True, null=True)  # Field name made lowercase.
	temp_oc = models.FloatField(db_column='Temp_oC', blank=True, null=True)  # Field name made lowercase.
	tds_mg_l = models.FloatField(db_column='TDS_mg_L', blank=True, null=True)  # Field name made lowercase.
	redoxe = models.FloatField(db_column='Redoxe', blank=True, null=True)  # Field name made lowercase.
	alc_meg_l = models.FloatField(db_column='Alc_meg_L', blank=True, null=True)  # Field name made lowercase.
	chla_ug_l = models.FloatField(db_column='Chla_ug_L', blank=True, null=True)  # Field name made lowercase.
	p_tot_ug_l = models.FloatField(db_column='P-tot_ug_L', blank=True, null=True)  # Field name made lowercase. 
	po4_ug_l = models.FloatField(db_column='PO4_ug_L', blank=True, null=True)  # Field name made lowercase.
	n_tot_ug_l = models.FloatField(db_column='N-tot_ug_L', blank=True, null=True)  # Field name made lowercase.
	nh4_ug_l = models.FloatField(db_column='NH4_ug_L', blank=True, null=True)  # Field name made lowercase.
	no3_ug_l = models.FloatField(db_column='NO3_ug_L', blank=True, null=True)  # Field name made lowercase.
	no2_ug_l = models.FloatField(db_column='NO2_ug_L', blank=True, null=True)  # Field name made lowercase.
	silicato_mg_l = models.FloatField(db_column='Silicato_mg_L', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = True
		db_table = 'Lagoa_Info_Amostra'

	def Data(self):
		data = (str(self.amostra_id.dia), str(self.amostra_id.mes), str(self.amostra_id.ano))
		return '/'.join(data)

	def Lagoa(self):
		return str(self.amostra_id.lagoa)

	def Profundidade(self):
		return str(self.amostra_id.profundidade)

class Zoo(models.Model):
	amostra_id = models.ForeignKey(Amostra, on_delete=models.CASCADE, db_column='Amostra_ID')  # Field name made lowercase.
	taxa = models.CharField(db_column='Taxa', max_length=60)  # Field name made lowercase.
	ordem = models.CharField(db_column='Ordem', max_length=45, blank=True, null=True)  # Field name made lowercase.
	familia = models.CharField(db_column='Familia', max_length=45, blank=True, null=True)  # Field name made lowercase.
	grupo = models.CharField(db_column='Grupo', max_length=45, blank=True, null=True)  # Field name made lowercase.
	filo = models.CharField(db_column='Filo', max_length=45, blank=True, null=True)  # Field name made lowercase.
	epiteto_especifico = models.CharField(db_column='Epiteto_Especifico', max_length=45, blank=True, null=True)  # Field name made lowercase.
	epiteto_subespecifico = models.CharField(db_column='Epiteto_Subespecifico', max_length=45, blank=True, null=True)  # Field name made lowercase.
	caracteristica = models.CharField(db_column='Caracteristica', max_length=45, blank=True, null=True)  # Field name made lowercase.
	conferir = models.IntegerField(db_column='Conferir', blank=True, null=True)  # Field name made lowercase.
	contagem = models.IntegerField(db_column='Contagem', blank=True, null=True)  # Field name made lowercase.
	vol_sedimentado = models.FloatField(db_column='Vol_Sedimentado', blank=True, null=True)  # Field name made lowercase.
	biovolume_um3 = models.FloatField(db_column='Biovolume_um3', blank=True, null=True)  # Field name made lowercase.
	vol_fil_l = models.FloatField(db_column='Vol_Fil_L', blank=True, null=True)  # Field name made lowercase.
	vol_cont_l = models.FloatField(db_column='Vol_Cont_L', blank=True, null=True)  # Field name made lowercase.
	mm3 = models.FloatField(blank=True, null=True)
	ind_l = models.FloatField(db_column='Ind_L', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = True
		db_table = 'Zoo'
		unique_together = (('amostra_id', 'taxa'),)

	def __unicode__(self):
		return str(self.amostra_id.amostra_id)

	def Data(self):
		data = (str(self.amostra_id.dia), str(self.amostra_id.mes), str(self.amostra_id.ano))
		return '/'.join(data)	

