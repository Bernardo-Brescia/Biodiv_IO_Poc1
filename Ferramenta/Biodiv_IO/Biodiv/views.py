from django.shortcuts import render
from .forms import (
	AddAmostraForm, AddZooForm, AddFitoForm, AddInfoForm, DateQueryForm, 
	AmostraFieldsForm, FitoFieldsForm, ZooFieldsForm, SpecificFieldsForm
)
from .models import Amostra
from .models import Zoo
from .models import Fito

#pagina inicial
def index(request):
	context = {}
	return render(request, 'Views/index.html', context)

#View para adicionar uma nova amostra	
def Amostra_list(request):
	if(request.method =="POST"):
		form = AddAmostraForm(request.POST)
		if form.is_valid():
			new_amostra = form.save()
	else:
		form = AddAmostraForm()
	latest_amostras = Amostra.objects.order_by('-ano', '-mes', 'dia')[:5]
	context = {
		'form': form,
		'amostras': latest_amostras,
		}
	return render(request, 'Views/amostras.html', context)

#View para adicionar um novo fito
def Fito_list(request):
	if(request.method =="POST"):
		form = AddFitoForm(request.POST)
		if form.is_valid():
			new_fito = form.save()
	else:
		form = AddFitoForm()
	#mostra apenas os ultimos 5 fitos adicionados
	latest_fitos = Fito.objects.order_by('-id')[:5]
	context = {
		'fitos': latest_fitos,
		'form': form,
		}
	return render(request, 'Views/fitos.html', context)
#View para adicionar um novo zoo
def Zoo_list(request):
	if(request.method =="POST"):
		form = AddZooForm(request.POST)
		if form.is_valid():
			new_zoo = form.save()
	else:
		form = AddZooForm()
	#mostra apenas os ultimos 5 zoos adicionados
	latest_zoos = Zoo.objects.order_by('-id')[:5]
	context = {
		'form': form,
		'zoos': latest_zoos
		}
	return render(request, 'Views/zoos.html', context)

#View para adicionar dados a uma amostra
def Info_Amostra_list(request):
	if(request.method =="POST"):
		form = AddInfoForm(request.POST)
		if form.is_valid():
			new_info = form.save()
	else:
		form = AddInfoForm()
	context = {
		'form': form,
		}
	return render(request, 'Views/info_amostra.html', context)

#View para pesquisa no banco de dados
def Query_Fields(request):
    
	if(request.method == "POST"):
		date_form = DateQueryForm(request.POST)
		amostra_fields = AmostraFieldsForm(request.POST)
		zoo_fields = ZooFieldsForm(request.POST)
		fito_fields = FitoFieldsForm(request.POST)
		specific_fields = SpecificFieldsForm(request.POST)
		search_input = request.POST
		print amostra_fields['Campos_Referentes_Amostra'][1]
		
	else:
		date_form = DateQueryForm() #formulario para definir o periodo de busca
		amostra_fields = AmostraFieldsForm() #define os SELECTS referentes a amostra
		zoo_fields = ZooFieldsForm() #define os SELECTS referentes a zoo
		fito_fields = FitoFieldsForm() #define os SELECTS referentes a fito
		specific_fields = SpecificFieldsForm() #define WHERE para busca especifica
	
	context = {
		'amostra_fields': amostra_fields,
		'date_form': date_form,
		'zoo_fields': zoo_fields,
		'fito_fields': fito_fields,
		'specific_fields': specific_fields,
		}
	return render(request, 'Views/query.html', context)
	
