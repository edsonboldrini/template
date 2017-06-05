#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gerar_dados.py

from faker import Faker;
from faker import Factory;

quantidade_endereco = 1000;
quantidade_aluno = 100000;
quantidade_responsavel = 10000;
quantidade_aluno_responsavel = 500000;
quantidade_entrada_aluno = 1500000;
quantidade_curso = 227;
quantidade_turma = 1000;

quantidade_tipo_contato = 1000;
quantidade_contato = 100000;
quantidade_matricula = 500000;
quantidade_horario = 10000;

commit = 1000;


def gerar_commit(arquivo, query, i, quantidade, query_insert) :
	
	if (i > 0 and (i  % commit) != 0) :
		query += ",";
	#fim if...
	
	arquivo.write(query+"\n");
	
	if ((i > 0 and (i  % commit) == 0) or i == quantidade) :
		#print(str(i)+" == "+str(quantidade));
		arquivo.write(";\n");	
		if (i+1 != quantidade) :
			arquivo.write(query_insert +"\n");
		#fim if...	
	#fim if...
	
#fim def gerar_commit...	


def gerar_endereco(fake):
	arquivo = open("endereco.sql","w");
	
	query_insert = "INSERT INTO endereco(endereco, cep, numero, idbairro, idcidade) VALUES  "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_endereco + 1;
	for i in range(1, quantidade) :
		cidade = fake.random_int(min=1, max=148);
		bairro = fake.random_int(min=1, max=700);
		endereco = fake.street_name();
		numero = fake.numerify(text="####");
		cep = fake.numerify(text="#####-###");
		
		query = " ('"+endereco+"', '"+str(cep)+"', '"+str(numero)+"', '"+str(bairro)+"', '"+str(cidade)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
				
	#fim for...
	arquivo.close();
	
#fim def...
 
def gerar_aluno(fake):
	arquivo = open("aluno.sql","w");
	
	query_insert = "INSERT INTO aluno(codigo, matricula, nome, idendereco) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_aluno+1;
	for i in range(1, quantidade) :
		endereco = fake.random_int(min=1, max=quantidade_endereco);
		nome = fake.name();
		codigo = fake.numerify(text="##########");
		matricula = fake.numerify(text="############");
		
		query = " ('"+str(codigo)+"', '"+str(matricula)+"', '"+str(nome)+"', '"+str(endereco)+"')";
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
					
	#fim for...
	arquivo.close();
	
#fim def...

def gerar_responsavel(fake):
	
	arquivo = open("responsavel.sql","w");
	
	query_insert = "INSERT INTO responsavel(nome, receber_notificacao, idendereco) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_responsavel+1;
	
	for i in range(1, quantidade) :
		endereco = fake.random_int(min=1, max=quantidade_endereco);
		receber_notificacao = fake.random_int(min=0, max=1);
		nome = fake.name();
		
		query = " ('"+str(nome)+"', '"+str(receber_notificacao)+"', '"+str(endereco)+"')"
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
	
#fim def...

def gerar_aluno_responsavel(fake):
	arquivo = open("aluno_responsavel.sql","w");
	
	query_insert = "INSERT INTO aluno_responsavel(idaluno, idresponsavel) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_aluno_responsavel+1;
	
	for i in range(1, quantidade) :
		aluno = fake.random_int(min=1, max=quantidade_aluno);
		responsavel = fake.random_int(min=1, max=quantidade_responsavel);
		
		query = " ('"+str(aluno)+"', '"+str(responsavel)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...

def gerar_entrada_aluno(fake):
	arquivo = open("entrada_aluno.sql","w");
	
	query_insert = " INSERT INTO entrada_aluno(hora, data, idaluno) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_entrada_aluno+1;
	for i in range(1, quantidade) :
		aluno = fake.random_int(min=1, max=quantidade_aluno);
		data = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None);
		data = str(data)[0:10];
		hora = fake.time(pattern="%H:%M:%S");
		
		query = " ('"+str(hora)+"', '"+str(data)+"', '"+str(aluno)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...

def gerar_curso(fake):
	arquivo = open("curso.txt","w");
	for i in range(500000) :
		nome = "Técnico em "+str(fake.lexify(text="????????"));
		
		query = "INSERT INTO curso(nome) VALUES ('"+str(nome)+"');"
		arquivo.write(query+"\n");
	#fim for...
	arquivo.close();	
#fim def...

def gerar_turma(fake):
	arquivo = open("turma.sql","w");
	
	query_insert = " INSERT INTO turma(nome, idcurso) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_turma+1;
	
	for i in range(1, quantidade) :
		nome = "Turma "+str(fake.lexify(text="??????????"))+" "+str(fake.year());
		idcurso = fake.random_int(min=1, max=quantidade_curso);
		
		query = " ('"+str(nome)+"', '"+str(idcurso)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...

def gerar_tipo_contato(fake):
	arquivo = open("tipo_contato.txt","w");
	for i in range(1000) :
		nome = fake.lexify(text="??????????");
		
		query = "INSERT INTO tipo_contato(nome) VALUES ('"+str(nome)+"');"
		arquivo.write(query+"\n");
	#fim for...
	arquivo.close();	
#fim def...

def gerar_tipo_contato(fake):
	arquivo = open("tipo_contato.txt","w");
	for i in range(1000) :
		nome = fake.lexify(text="??????????");
		
		query = "INSERT INTO tipo_contato(descricao) VALUES ('"+str(nome)+"');"
		arquivo.write(query+"\n");
	#fim for...
	arquivo.close();	
#fim def...

def gerar_contato(fake):
	arquivo = open("contato.sql","w");
	
	query_insert = " INSERT INTO contato(contato, principal, idtipo_contato, idresponsavel) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_contato+1;
	
	for i in range(1, quantidade) :
		nome = fake.first_name();
		principal = fake.random_int(min=0, max=1);
		idtipo_contato = fake.random_int(min=1, max=quantidade_tipo_contato);
		idresponsavel = fake.random_int(min=1, max=quantidade_responsavel);
		
		query = " ('"+str(nome)+"', '"+str(principal)+"', '"+str(idtipo_contato)+"', '"+str(idresponsavel)+"')";
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
	#fim for...
	arquivo.close();	
#fim def...

def gerar_matricula(fake):
	arquivo = open("matricula.sql","w");
	
	query_insert = " INSERT INTO matricula(data, matriculado, idturma, idaluno) VALUES "
	arquivo.write(query_insert+"\n");
	
	
	quantidade = quantidade_matricula+1;
	for i in range(1, quantidade) :
		
		data = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None);
		data = str(data)[0:10];
		matriculado = fake.random_int(min=0, max=1);
		
		idturma = fake.random_int(min=1, max=quantidade_turma);
		idaluno = fake.random_int(min=1, max=quantidade_aluno);
		
		query = " ('"+str(data)+"', '"+str(matriculado)+"', '"+str(idturma)+"', '"+str(idaluno)+"') ";
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
		
	#fim for...
	arquivo.close();	
#fim def...

def gerar_horario(fake):
	arquivo = open("horario.sql","w");
	
	query_insert = " INSERT INTO horario(dia_semana, idturma) VALUES "
	arquivo.write(query_insert+"\n");
		
	quantidade = quantidade_horario+1;
	
	for i in range(1, quantidade) :
		
		idturma = fake.random_int(min=1, max=quantidade_turma);
		dia_semana = fake.random_int(min=1, max=6);
		
		query = " ('"+str(dia_semana)+"', '"+str(idturma)+"') ";
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
	#fim for...
	arquivo.close();	
#fim def...
    
def main():
	
	
	#from faker import Factory
	fake = Factory.create('pt_BR');
	#print(fake);
	
	'''gerar_tipo_contato(fake);
	print("Tipo contato gerado com sucesso.");
	'''
	
	#gerar_endereco(fake);
	#print("Endereco gerado com sucesso.");
	
	#gerar_aluno(fake);
	#print("Aluno gerado com sucesso.");
	
	#gerar_responsavel(fake);
	#print("Responsavel gerado com sucesso.");
	
	#gerar_aluno_responsavel(fake);
	#print("Aluno Responsavel gerado com sucesso.");
	
	#gerar_entrada_aluno(fake);
	#print("Entrada Aluno gerado com sucesso.");
	
	#print(fake.lexify(text="??????"));
	#gerar_curso(fake);
	#print("Curso gerado com sucesso.");
	
	#gerar_turma(fake);
	#print("Turma gerado com sucesso.");
	
	
	#gerar_contato(fake);
	#print("Contato gerado com sucesso.");
	
	#gerar_matricula(fake);
	#print("Matricula gerada com sucesso.");
	
	gerar_horario(fake);
	print("Horário gerado com sucesso.");
	
	
	#print(fake.numerify(text="#####-###"));
	
	#fake = Faker()
	'''for i in range(30) :
		print(fake.random_element(elements=('a', 'b', 'c')))
	#fim for...'''
	'''from faker import Faker
	fake = Faker();
	fake.name()
	fake.name_male()
	fake.first_name()
	'''
#	print(names.get_full_name())
	
	'''names.get_full_name(gender='male')
	names.get_first_name()
	names.get_first_name(gender='female')
	names.get_last_name()
	'''
	return 0

if __name__ == '__main__':
	main()

