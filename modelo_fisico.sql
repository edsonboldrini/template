-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE tipo_contato (
descricao VARCHAR(60),
idtipo_contato SERIAL PRIMARY KEY
)

CREATE TABLE aluno (
codigo VARCHAR(20),
matricula VARCHAR(20),
nome VARCHAR(100),
idaluno SERIAL PRIMARY KEY,
idendereco INTEGER
)

CREATE TABLE responsavel (
nome VARCHAR(100),
receber_notificacao INT,
idresponsavel SERIAL PRIMARY KEY,
idendereco INTEGER
)

CREATE TABLE entrada_aluno (
hora VARCHAR(8),
data DATE,
identrada_aluno SERIAL PRIMARY KEY,
idaluno INTEGER,
FOREIGN KEY(idaluno) REFERENCES aluno (idaluno)
)

CREATE TABLE cidade (
idcidade SERIAL PRIMARY KEY,
nome VARCHAR(100)
)

CREATE TABLE curso (
idcurso SERIAL PRIMARY KEY,
nome VARCHAR(100),
descricao VARCHAR(200)
)

CREATE TABLE turma (
idturma SERIAL PRIMARY KEY,
nome VARCHAR(100),
descricao VARCHAR(200),
idcurso INTEGER,
FOREIGN KEY(idcurso) REFERENCES curso (idcurso)
)

CREATE TABLE horario (
idhorario SERIAL PRIMARY KEY,
dia_semana INTEGER,
idturma INTEGER,
FOREIGN KEY(idturma) REFERENCES turma (idturma)
)

CREATE TABLE matricula (
data DATE,
matriculado INTEGER,
idmatricula SERIAL PRIMARY KEY,
idturma INTEGER,
idaluno INTEGER,
FOREIGN KEY(idturma) REFERENCES turma (idturma),
FOREIGN KEY(idaluno) REFERENCES aluno (idaluno)
)

CREATE TABLE contato (
contato VARCHAR(200),
principal INTEGER,
idcontato SERIAL PRIMARY KEY,
idtipo_contato INTEGER,
idresponsavel INTEGER,
FOREIGN KEY(idtipo_contato) REFERENCES tipo_contato (idtipo_contato),
FOREIGN KEY(idresponsavel) REFERENCES responsavel (idresponsavel)
)

CREATE TABLE data_evento (
data DATE,
iddata_evento SERIAL PRIMARY KEY,
idevento INTEGER
)

CREATE TABLE entrada_saida (
horario_saida VARCHAR(6),
horario_entrada VARCHAR(6),
identrada_saida INTEGER PRIMARY KEY,
idhorario INTEGER,
iddata_evento INTEGER,
FOREIGN KEY(idhorario) REFERENCES horario (idhorario),
FOREIGN KEY(iddata_evento) REFERENCES data_evento (iddata_evento)
)

CREATE TABLE evento (
idevento SERIAL PRIMARY KEY,
nome VARCHAR(100)
)

CREATE TABLE bairro (
idbairro INTEGER PRIMARY KEY,
nome VARCHAR(100)
)

CREATE TABLE endereco (
endereco VARCHAR(200),
cep VARCHAR(9),
numero VARCHAR(20),
idendereco SERIAL PRIMARY KEY,
idbairro INTEGER,
idcidade INTEGER,
FOREIGN KEY(idbairro) REFERENCES bairro (idbairro),
FOREIGN KEY(idcidade) REFERENCES cidade (idcidade)
)

CREATE TABLE aluno_responsavel (
idaluno INTEGER,
idresponsavel INTEGER,
FOREIGN KEY(idaluno) REFERENCES aluno (idaluno),
FOREIGN KEY(idresponsavel) REFERENCES responsavel (idresponsavel)
)

ALTER TABLE aluno ADD FOREIGN KEY(idendereco) REFERENCES endereco (idendereco)
ALTER TABLE responsavel ADD FOREIGN KEY(idendereco) REFERENCES endereco (idendereco)
ALTER TABLE data_evento ADD FOREIGN KEY(idevento) REFERENCES evento (idevento)
