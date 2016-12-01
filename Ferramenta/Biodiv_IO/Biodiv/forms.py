from django import forms
from .models import Amostra
from .models import Fito
from .models import Zoo
from .models import LagoaInfoAmostra

class AddAmostraForm(forms.ModelForm):
	class Meta:
		model = Amostra
		fields = '__all__'
		
class AddFitoForm(forms.ModelForm):
	class Meta:
		model = Fito
		fields = '__all__'
		
class AddZooForm(forms.ModelForm):
	class Meta:
		model = Zoo
		fields = '__all__'

class AddInfoForm(forms.ModelForm):
	class Meta:
		model = LagoaInfoAmostra
		fields = '__all__'
		
class DateQueryForm(forms.Form):

	from_dia = forms.IntegerField(label = 'Dia', min_value = 0, max_value = 31, required = False)
	to_dia = forms.IntegerField(label = 'a', min_value = 0, max_value = 31, required = False)
	from_mes = forms.IntegerField(label = 'Mes', min_value = 0, max_value = 12, required = False)
	to_mes = forms.IntegerField(label = 'a', min_value = 0, max_value = 12, required = False)
	from_ano = forms.IntegerField(label = 'Ano', min_value = 0, required = False)
	to_ano = forms.IntegerField(label = 'a', min_value = 0, required = False)

class AmostraFieldsForm(forms.Form):
	fields = (
		('Amostra id', 'Amostra id'),
		('Lagoa', 'Lagoa'),
		('Dia', 'Dia'),
		('Mes', 'Mes'),
		('Ano', 'Ano'),
		('Profundidade', 'Profundidade'),
		('Cod profundidade', 'Cod profundidade'),
		('Hora', 'Hora'),
		('Secchi', 'Secchi'),
		('Responsavel', 'Responsavel'),
		('Obs', 'Obs'),
	)
		
	Campos_Referentes_Amostra = forms.MultipleChoiceField(
		required = False,
		widget = forms.CheckboxSelectMultiple,
		choices = fields
	)
	
	
	
	
class ZooFieldsForm(forms.Form):
	fields = (
		('Amostra id', 'Amostra id'),
		('taxa', 'taxa'),
		('ordem', 'ordem'),
		('familia', 'familia'),
		('grupo', 'grupo'),
		('filo', 'filo'),
		('epiteto especifico', 'epiteto especifico'),
		('epiteto subespecifico', 'epiteto subespecifico'),
		('caracteristica', 'caracteristica'),
		('conferir', 'conferir'),
		('contagem', 'contagem'),
		('vol sedimentado', 'vol sedimentado'),
		('biovolume.um3', 'biovolume.um3'),
		('vol.fil.l', 'vol.fil.l'),
		('vol.cont.l', 'vol.cont.l'),
		('mm3', 'mm3'),
		('ind.l', 'ind.l'),
	)
		
	Campos_Referentes_Zoo = forms.MultipleChoiceField(
		required = False,
		widget = forms.CheckboxSelectMultiple,
		choices = fields
	)

class FitoFieldsForm(forms.Form):
        
	fields = (
		('Amostra id', 'Amostra id'),
		('taxa', 'taxa'),
		('ordem', 'ordem'),
		('familia', 'familia'),
		('classe', 'classe'),
		('divisao', 'divisao'),
		('epiteto especifico', 'epiteto especifico'),
		('epiteto subespecifico', 'epiteto subespecifico'),
		('caracteristica', 'caracteristica'),
		('conferir', 'conferir'),
		('contagem', 'contagem'),
		('vol sedimentado', 'vol sedimentado'),
		('biovolume.um3', 'biovolume.um3'),
		('area camara', 'area camara'),
		('area campo', 'area campo'),
		('numero campo', 'numero campo'),
		('mm3', 'mm3'),
		('ind.l', 'ind.l'),
	)
		
	Campos_Referentes_Fito = forms.MultipleChoiceField(
		required = False,
		widget = forms.CheckboxSelectMultiple,
		choices = fields
	)

class SpecificFieldsForm(forms.Form):

	lagoa = forms.CharField(label = 'Lagoa', required = False)
	taxa = forms.CharField(label = 'Taxa', required = False)
	




