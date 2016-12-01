from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Amostra
from .models import Fito
from .models import Zoo
from .models import LagoaInfoAmostra

class ZooInline(admin.TabularInline):
	model = Zoo

class FitoInline(admin.TabularInline):
	model = Fito

class AmostraInline(admin.TabularInline):
	model = LagoaInfoAmostra

class ZooAdmin(admin.ModelAdmin):
	list_display = ('id', '__unicode__', 'taxa', 'contagem', 'Data')
	class meta:
		model = Zoo

class AmostraAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'lagoa', 'profundidade', 'dia', 'mes', 'ano')
	filter_list = ('__unicode__',)
	class meta:
		model = Amostra
	inlines = [
		AmostraInline,
		ZooInline,
		FitoInline,
	]


class FitoAdmin(admin.ModelAdmin):
	list_display = ['id', '__unicode__', 'taxa', 'contagem', 'Data']
	class meta:
		model = Fito

class LagoaAdmin(admin.ModelAdmin):
	list_display = ('pk', 'Lagoa', 'Profundidade', 'Data', )
	class meta:
		model = LagoaInfoAmostra

# Register your models here.

admin.site.register(Amostra, AmostraAdmin)
admin.site.register(Fito, FitoAdmin)
admin.site.register(LagoaInfoAmostra, LagoaAdmin)
admin.site.register(Zoo, ZooAdmin)

