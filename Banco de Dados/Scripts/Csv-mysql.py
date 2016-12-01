import csv
import MySQLdb

# Conecta ao banco de dados
connection = MySQLdb.connect("localhost", "root", "i!touch2g", "Biodiv_IO")

cursor = connection.cursor()

#variaveis necessarias
amostras = []
ID = []

#-----------------------Funcoes de padronizacao dos dados----------------------------------------------------#

def str_to_float(number):
	
	try:
		float_nbr = float(number.replace(',','.'))
		return float_nbr
	except:
		return

def conferir_format(conferir):
	
	if(conferir == 'cf.'):
		return 1
	else:
		return 0

def blanc_to_int(number):
	
	try:
		int_nbr = int(number)
		return int_nbr
	except:
		return

#-----------------------Funcoes de identificacao dos dados e exportacao ta tabela amostras-----------------------#

#identificador utilizado para identificar cada coleta de dados da lagoa
def retira_amostras_lagoa():

	file = open('18_Lagoas_10 anos_FQ.csv')
	Planilha_lagoas = csv.DictReader(file, delimiter = ",")
	
	next(Planilha_lagoas)
	for row in Planilha_lagoas:
		concat = row['Ano'] + "_" + row["Mes.num"] + ":" + row['Prof.m'] + ":" + row['Lagoa']
		if concat not in amostras:
			amostras.append(concat)
			Id = amostras.index(concat)
			try:
				cursor.execute("""INSERT INTO Amostra VALUES (%s, %s, NULL, %s, %s, %s, %s, NULL, NULL, NULL, %s)""", (Id, row['Lagoa'], row["Mes.num"], row["Ano"], str_to_float(row["Prof.m"]), str_to_float(row["Cod.Prof"]), row['Obs']))
			except MySQLdb.Error, e:
				continue
	
	connection.commit()

#identificador utilizado para identificar cada coleta de fito
def retira_amostras_fito():

	file = open('7Lagoas_Fito_Diego_teste.csv')
	Planilha_fito = csv.DictReader(file, delimiter = ",")

	next(Planilha_fito)

	for row in (Planilha_fito):
		concat = row['Ano'] + "_" + row["Mes"] + ":" + row['Prof.m'] + ":" + row['Lagoa']
		if concat not in amostras:
			amostras.append(concat)
			Id = amostras.index(concat)
			Data = row["Mes"] + "/" + row["Ano"]
			try:
				cursor.execute("""INSERT INTO Amostra VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (Id, row['Lagoa'], blanc_to_int(row["Dia"]), row["Mes"], row["Ano"], str_to_float(row["Prof.m"]), str_to_float(row["Cod.Prof"]), row['Hora'], row['Secchi.m'], row['Resp'], row['Obs']))
			except:
				continue
		else:
			Id = amostras.index(concat)
			cursor.execute("""
				UPDATE Amostra 
				SET dia = %s, responsavel = %s
				WHERE Amostra_ID = %s""", (blanc_to_int(row['Dia']), row['Resp'], Id))

	connection.commit()

#identificador utilizado para identificar cada coleta de zoo
def retira_amostras_zoo():

	file = open('6Lagoas_Zoo_Diego_teste.csv')
	Planilha_zoo = csv.DictReader(file, delimiter = ",")

	next(Planilha_zoo)

	for row in (Planilha_zoo):
		concat = row['Ano'] + "_" + row["Mes"] + ":" + row['Prof.m'] + ":" + row['Lagoa']
		if concat not in amostras:
			amostras.append(concat)
			Id = amostras.index(concat)
			Data = row["Mes"] + "/" + row["Ano"]
			try:
				cursor.execute("""INSERT INTO Amostra VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (Id, row['Lagoa'], blanc_to_int(row["Dia"]), row["Mes"], row["Ano"], str_to_float(row["Prof.m"]), str_to_float(row["Cod.Prof"]), row['Hora'], row['Secchi.m'], row['Resp'], row['Obs']))
			except:
				continue
		else:
			Id = amostras.index(concat)
			cursor.execute("""
				UPDATE Amostra
				SET dia = %s, responsavel = %s
				WHERE Amostra_ID = %s""", ( blanc_to_int(row['Dia']), row['Resp'], Id))

	connection.commit()

#-----------------------Funcoes de exportacao dos dados para o banco-----------------------#

def Tab_amostra_lagoa():
	
	file = open('18_Lagoas_10 anos_FQ.csv')
	Planilha_lagoas = csv.DictReader(file, delimiter = ",")

	next(Planilha_lagoas)

	for row in Planilha_lagoas:
		concat = row['Ano'] + "_" + row["Mes.num"] + ":" + row['Prof.m'] + ":" + row['Lagoa']
		Id = amostras.index(concat)
		if Id not in ID:
			ID.append(Id)
			try:
				cursor.execute("""INSERT INTO Lagoa_Info_Amostra 
					VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (Id, str_to_float(row['pH']), str_to_float(row['cond.uS.cm']), str_to_float(row['turb.NTU']), str_to_float(row['OD.mg.L']), str_to_float(row['Temp.oC']), str_to_float(row['TDS.mg.L']), str_to_float(row['Redoxe']), str_to_float(row['Alc.meq.L']), str_to_float(row['Chla.ug.L']), str_to_float(row['P-tot.ug.L']), str_to_float(row['PO4.ug.L']), str_to_float(row['N-tot.ug.L']), str_to_float(row['NH4.ug.L']), str_to_float(row['NO3.ug.L']), str_to_float(row['NO2.ug.L']), str_to_float(row['Silicato.mg.L'])))
			except MySQLdb.Error, e:
				continue

	connection.commit()

def Tab_amostra_zoo():
	
	file = open('6Lagoas_Zoo_Diego_teste.csv')
	Planilha_zoo = csv.DictReader(file, delimiter = ",")
	contagem = 0
	incr = 0

	next(Planilha_zoo)

	for row in Planilha_zoo:
		concat = row['Ano'] + "_" + row["Mes"] + ":" + row['Prof.m'] + ":" + row['Lagoa']
		ID = amostras.index(concat)
		incr = incr + 1
		try:
			cursor.execute("""INSERT INTO Zoo
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (incr, row['Taxa'], row['Ordem'], row['Familia'], row['Grupo'], row['Filo'], row['Epiteto Especifico'], row['Epiteto Subespecifico'], row['Caracteristica'], conferir_format(row['Conferir']), blanc_to_int(row['Contagem']), str_to_float(row['Vol.sed.mL']), str_to_float(row['Biovol.mm3']), str_to_float(row['Vol.Fil.L']), str_to_float(row['Vol.cont.mL']), str_to_float(row['mm3.L']), str_to_float(row['Ind.L']), ID))
			contagem = blanc_to_int(row['Contagem'])
		except MySQLdb.Error, e:
			#em caso de erro referente a entrada duplicada, a entrada com o maior valor de unidades de individuo sera considerada
			if(int(e[0]) == 1062):
				incr = incr - 1			
				if(contagem < blanc_to_int(row['Contagem'])):
					cursor.execute("""
						UPDATE Zoo 
						SET Contagem = %s, Ind_L = %s
						WHERE Amostra_ID =  %s and taxa = %s""", (blanc_to_int(row['Contagem']), str_to_float(row['Ind.L']), ID, row['Taxa']))
			continue
	
	connection.commit()		

def Tab_amostra_fito():
	
	file = open('7Lagoas_Fito_Diego_teste.csv')
	Planilha_fito = csv.DictReader(file, delimiter = ",")
	contagem = 0
	incr = 0

	next(Planilha_fito)

	for row in Planilha_fito:
		incr = incr + 1
		concat = row['Ano'] + "_" + row["Mes"] + ":" + row['Prof.m'] + ":" + row['Lagoa']
		ID = amostras.index(concat)
		try:
			cursor.execute("""INSERT INTO Fito
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (incr, row['Taxa'], row['Ordem'], row['Familia'], row['Classe'], row['Filo/Divisao'], row['Epiteto Especifico'], row['Epiteto Subespecifico'], row['Caracteristica'], conferir_format(row['Conferir']), blanc_to_int(row['Contagem']), str_to_float(row['Vol.Sed.mL']), str_to_float(row['Biovol.um3']), str_to_float(row['mm3.L']), str_to_float(row['Ind.L']), str_to_float(row['A.Camara']), str_to_float(row['A.Campo']), str_to_float(row['N.Campo']), ID))
			contagem = blanc_to_int(row['Contagem'])
		except MySQLdb.Error, e:
			#em caso de erro referente a entrada duplicada, a entrada com o maior valor de unidades de individuo sera considerada
			if(int(e[0]) == 1062):
				incr = incr - 1
				if(contagem < blanc_to_int(row['Contagem'])):
					cursor.execute("""
						UPDATE Fito 
						SET Contagem = %s, Ind_L = %s
						WHERE Amostra_ID = %s and taxa = %s""", (blanc_to_int(row['Contagem']), str_to_float(row['Ind.L']), ID, row['Taxa']))
			continue

	connection.commit()


retira_amostras_lagoa()
retira_amostras_zoo()
retira_amostras_fito()


Tab_amostra_lagoa()
Tab_amostra_zoo()
Tab_amostra_fito()
