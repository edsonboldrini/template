#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gerar_dados.py

from faker import Faker;
from faker import Factory;

quantidade_cidade = 100;
quantidade_bairro = 1000;
quantidade_endereco = 2000;
quantidade_aluno = 1000;
quantidade_responsavel = 3000;
quantidade_aluno_responsavel = 5000;
quantidade_entrada_aluno = 1500000;
quantidade_curso = 10;
quantidade_turno = 6;
quantidade_disciplina = 60;
quantidade_turma = 50;
quantidade_periodo = 150;

quantidade_tipo_contato = 10;
quantidade_contato = 10000;
quantidade_contato_responsavel = 6000;
quantidade_contato_aluno = 6000;

quantidade_evento = 20;
quantidade_data_evento = 20;
quantidade_entrada_saida = 40;

quantidade_dia_semana = 6;
quantidade_aluno_evento = 3000;
quantidade_aluno_horario = 100000;
quantidade_horario = 500;


#quantidade_horario = 10000;

commit = 1000;


def gerar_commit(arquivo, query, i, quantidade, query_insert) :
	
	if ((i > 0 and (i  % commit) != 0) and i+1 != quantidade) :
		query += ",";
	#fim if...
	
	arquivo.write(query+"\n");
	
	#print(i,"===" ,quantidade)
	if ((i > 0 and (i  % commit) == 0) or i+1 == quantidade) :
		#print(str(i)+" == "+str(quantidade));
		arquivo.write(";\n");	
		if (i+1 != quantidade) :
			arquivo.write(query_insert +"\n");
		#fim if...	
	#fim if...
	
#fim def gerar_commit...	

def gerar_cidade(fake):
	arquivo = open("cidade.sql","w");
	
	query_insert = " INSERT INTO cidade(nome) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_cidade+1;
	
	for i in range(1, quantidade) :
		nome = "Cidade "+str(fake.lexify(text="??????????"));
		
		query = " ('"+str(nome)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...

def gerar_bairro(fake):
	arquivo = open("bairro.sql","w");
	
	query_insert = " INSERT INTO bairro(nome, idcidade) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_bairro+1;
	
	for i in range(1, quantidade) :
		nome = "Bairro "+str(fake.lexify(text="??????????"));
		idcidade = fake.random_int(min=1, max=quantidade_cidade);
		
		query = " ('"+str(nome)+"', '"+str(idcidade)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...

def gerar_endereco(fake):
	arquivo = open("endereco.sql","w");
	
	query_insert = "INSERT INTO endereco(endereco, cep, numero, idbairro) VALUES  "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_endereco + 1;
	for i in range(1, quantidade) :
		bairro = fake.random_int(min=1, max=quantidade_bairro);
		endereco = fake.street_name();
		numero = fake.numerify(text="####");
		cep = fake.numerify(text="#####-###");
		
		query = " ('"+endereco+"', '"+str(cep)+"', '"+str(numero)+"', '"+str(bairro)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
				
	#fim for...
	arquivo.close();
	
#fim def...
 
def gerar_aluno(fake):
	arquivo = open("aluno.sql","w");
	
	query_insert = "INSERT INTO aluno(codigo, matricula, imagem, nome, idendereco) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_aluno+1;
	for i in range(1, quantidade) :
		endereco = fake.random_int(min=1, max=quantidade_endereco);
		nome = fake.name();
		codigo = fake.numerify(text="##########");
		matricula = fake.numerify(text="############");
		imagem = fake.lexify(text="?????????");
		
		query = " ('"+str(codigo)+"', '"+str(matricula)+"' , '"+str(matricula)+".JPEG', '"+str(nome)+"', '"+str(endereco)+"')";
		
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

def gerar_log_aluno(fake):
	arquivo = open("log_aluno.sql","w");
	
	query_insert = " INSERT INTO log_aluno(hora, data, idaluno, tipo) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_entrada_aluno+1;
	for i in range(1, quantidade) :
		aluno = fake.random_int(min=1, max=quantidade_aluno);
		tipo = fake.random_int(min=0, max=1);
		data = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None);
		data = str(data)[0:10];
		hora = fake.time(pattern="%H:%M:%S");
		
		query = " ('"+str(hora)+"', '"+str(data)+"', '"+str(aluno)+"', '"+str(tipo)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...

def gerar_turno(fake):
	arquivo = open("turno.sql","w");
	
	query_insert = " INSERT INTO turno(nome) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_turno+1;
	
	for i in range(1, quantidade) :
		nome = "Turno "+str(fake.lexify(text="??????????"));
		
		query = " ('"+str(nome)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...

def gerar_disciplina(fake):
	arquivo = open("disciplina.sql","w");
	
	query_insert = " INSERT INTO disciplina(nome) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_disciplina+1;
	
	for i in range(1, quantidade) :
		nome = "Disciplina "+str(fake.lexify(text="??????????"));
		
		query = " ('"+str(nome)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...

def gerar_curso(fake):
	arquivo = open("curso.sql","w");
	
	query_insert = " INSERT INTO curso(nome) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_curso+1;
	
	for i in range(1, quantidade) :
		nome = "Curso "+str(fake.lexify(text="??????????"));
		
		query = " ('"+str(nome)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...

def gerar_turma(fake):
	arquivo = open("turma.sql","w");
	
	query_insert = " INSERT INTO turma(nome, idcurso, idturno) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_turma+1;
	
	for i in range(1, quantidade) :
		nome = "Turma "+str(fake.lexify(text="??????????"))+" "+str(fake.year());
		idcurso = fake.random_int(min=1, max=quantidade_curso);
		idturno = fake.random_int(min=1, max=quantidade_turno);
		
		
		query = " ('"+str(nome)+"', '"+str(idcurso)+"', '"+str(idturno)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...

def gerar_periodo(fake):
	arquivo = open("periodo.sql","w");
	
	query_insert = " INSERT INTO periodo (periodo, ano, idturma) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_turma+1;
	
	for i in range(1, quantidade) :
		periodo = fake.random_int(min=1, max=3);
		idturma = fake.random_int(min=1, max=quantidade_turma);
		ano = fake.random_int(min=2000, max=2017);
		
		
		query = " ('"+str(periodo)+"', '"+str(ano)+"', '"+str(idturma)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...


def gerar_tipo_contato(fake):
	arquivo = open("tipo_contato.sql","w");
	
	query_insert = " INSERT INTO tipo_contato(descricao) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_tipo_contato+1;
	
	for i in range(1, quantidade) :
		nome = "Tipo Contato "+str(fake.lexify(text="??????????"));
		
		query = " ('"+str(nome)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...


def gerar_contato(fake):
	arquivo = open("contato.sql","w");
	
	query_insert = " INSERT INTO contato(contato, principal, idtipo_contato) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_contato+1;
	
	for i in range(1, quantidade) :
		nome = fake.first_name();
		principal = fake.random_int(min=0, max=1);
		idtipo_contato = fake.random_int(min=1, max=quantidade_tipo_contato);
		
		query = " ('"+str(nome)+"', '"+str(principal)+"', '"+str(idtipo_contato)+"')";
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
	#fim for...
	arquivo.close();	
#fim def...

def gerar_contato_responsavel(fake):
	arquivo = open("contato_responsavel.sql","w");
	
	query_insert = " INSERT INTO responsavel_contato(idresponsavel, idcontato) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_contato_responsavel+1;
	
	for i in range(1, quantidade) :
		idcontato = fake.random_int(min=1, max=quantidade_contato);
		idresponsavel = fake.random_int(min=1, max=quantidade_responsavel);
		
		query = " ('"+str(idresponsavel)+"', '"+str(idcontato)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...

def gerar_contato_aluno(fake):
	arquivo = open("contato_aluno.sql","w");
	
	query_insert = " INSERT INTO aluno_contato(idaluno, idcontato) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_contato_responsavel+1;
	
	for i in range(1, quantidade) :
		idcontato = fake.random_int(min=1, max=quantidade_contato);
		idaluno = fake.random_int(min=1, max=quantidade_aluno);
		
		query = " ('"+str(idaluno)+"', '"+str(idcontato)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...



def gerar_evento(fake):
	arquivo = open("evento.sql","w");
	
	query_insert = " INSERT INTO evento(nome) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_evento+1;
	
	for i in range(1, quantidade) :
		nome = "Evento "+str(fake.lexify(text="??????????"));
		
		query = " ('"+str(nome)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...

def gerar_data_evento(fake):
	arquivo = open("data_evento.sql","w");
	
	query_insert = " INSERT INTO data_evento(idevento, data) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_data_evento+1;
	
	for i in range(1, quantidade) :
		idevento = fake.random_int(min=1, max=quantidade_evento);
		
		
		data = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None);
		data = str(data)[0:10];
		
		query = " ('"+str(idevento)+"', '"+str(data)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...
        
def gerar_entrada_saida(fake):
	arquivo = open("entrada_saida.sql","w");
	
	query_insert = " INSERT INTO entrada_saida (horario_saida, horario_entrada, iddata_evento) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_entrada_saida+1;
	
	for i in range(1, quantidade) :
		iddata_evento = fake.random_int(min=1, max=quantidade_data_evento);
		hora_entrada = fake.time(pattern="%H:%M:%S");
		hora_saida = fake.time(pattern="%H:%M:%S");
		
		
		query = " ('"+str(hora_saida)+"', '"+str(hora_entrada)+"' , '"+str(iddata_evento)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();
#fim def...
     
def gerar_aluno_evento(fake):
	arquivo = open("aluno_evento.sql","w");
	
	query_insert = " INSERT INTO aluno_evento (idevento, idaluno) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_aluno_evento+1;
	for i in range(1, quantidade) :
		
		idevento = fake.random_int(min=1, max=quantidade_evento);
		idaluno = fake.random_int(min=1, max=quantidade_aluno);
		
		query = " ('"+str(idevento)+"', '"+str(idaluno)+"') ";
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
		
	#fim for...
	arquivo.close();	
#fim def...  


def gerar_aluno_matriculado(fake):
	arquivo = open("aluno_matriculado.sql","w");
	
	query_insert = " INSERT INTO aluno_matriculado (data, matriculado, idhorario, idaluno) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_aluno_horario+1;
	for i in range(1, quantidade) :
		
		data = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None);
		data = str(data)[0:10];
		matriculado = fake.random_int(min=0, max=1);
		
		idhorario = fake.random_int(min=1501, max=4000);
		idaluno = fake.random_int(min=1, max=quantidade_aluno);
		
		query = " ('"+str(data)+"', '"+str(matriculado)+"', '"+str(idhorario)+"', '"+str(idaluno)+"') ";
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
		
	#fim for...
	arquivo.close();	
#fim def...              

def gerar_dia_semana(fake):
	arquivo = open("dia_semana.sql","w");
	
	query_insert = " INSERT INTO dia_semana(nome) VALUES "
	arquivo.write(query_insert+"\n");
	
	quantidade = quantidade_dia_semana+1;
	
	for i in range(1, quantidade) :
		nome = " "+str(fake.lexify(text="??????????"))+"-Feira";
		
		query = " ('"+str(nome)+"') "
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);

	#fim for...
	arquivo.close();	
#fim def...

def gerar_horario(fake):
	arquivo = open("horario.sql","w");
	
	query_insert = " INSERT INTO horario( hora_inicio, hora_final, iddia_semana, iddisciplina, idperiodo) VALUES "
	arquivo.write(query_insert+"\n");
	
	
	quantidade = quantidade_horario+1;
	for i in range(1, quantidade) :
		
		hora_inicio = fake.time(pattern="%H:%M:%S");
		hora_final = fake.time(pattern="%H:%M:%S");
	
		iddia_semana = fake.random_int(min=1, max=quantidade_dia_semana);
		iddisciplina = fake.random_int(min=1, max=quantidade_disciplina);
		idperiodo = fake.random_int(min=1, max=quantidade_periodo);
		
		query = " ('"+str(hora_inicio)+"', '"+str(hora_final)+"', '"+str(iddia_semana)+"', '"+str(iddisciplina)+"', '"+str(idperiodo)+"') ";
		
		gerar_commit(arquivo, query, i, quantidade, query_insert);
		
	#fim for...
	arquivo.close();	
#fim def... 
    
def main():
	
	
	#from faker import Factory
	fake = Factory.create('pt_BR');
	#print(fake);
	
	
	
	gerar_cidade(fake);
	print("Cidade gerado com sucesso.");
	
	gerar_bairro(fake);
	print("Bairro gerado com sucesso.");
	
	gerar_endereco(fake);
	print("Endereco gerado com sucesso.");
	
	gerar_aluno(fake);
	print("Aluno gerado com sucesso.");
	
	gerar_responsavel(fake);
	print("Responsavel gerado com sucesso.");
	
	gerar_aluno_responsavel(fake);
	print("Aluno Responsavel gerado com sucesso.");
	
	gerar_log_aluno(fake); #log_aluno
	print("log_aluno gerado com sucesso.");
	
	gerar_curso(fake);
	print("Curso gerado com sucesso.");
	
	gerar_turno(fake);
	print("Turno gerado com sucesso.");
		
	gerar_turma(fake);
	print("Turma gerado com sucesso.");
	
	gerar_disciplina(fake);
	print("Disciplina gerado com sucesso.");
	
	gerar_tipo_contato(fake);
	print("Tipo Contato gerado com sucesso.");
	
	gerar_contato(fake);
	print("Contato gerado com sucesso.");
	
	gerar_contato_responsavel(fake);
	print("Contato responsavel gerado com sucesso.");
	
	gerar_contato_aluno(fake);
	print("Contato aluno gerado com sucesso.");
	
	gerar_periodo(fake);
	print("Periodo gerado com sucesso.");
	
	gerar_evento(fake);
	print("Evento gerado com sucesso.");
	
	gerar_data_evento(fake);
	print("Data Evento gerado com sucesso.");
	
	gerar_entrada_saida(fake);
	print("Entrada Saida gerado com sucesso.");
	
	gerar_dia_semana(fake);
	print("Dia Semana gerado com sucesso.");
	
	gerar_aluno_evento(fake);
	print("Aluno Evento gerado com sucesso.");
	
	gerar_horario(fake);
	print("Horario gerado com sucesso.");
	
	gerar_aluno_matriculado(fake);
	print("Aluno matriculado gerado com sucesso.");
	
	
	
	return 0

if __name__ == '__main__':
	main()

