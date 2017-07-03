-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE aluno (
codigo VARCHAR(20),
imagem VARCHAR(200),
matricula VARCHAR(20),
nome VARCHAR(100),
idaluno SERIAL PRIMARY KEY,
idendereco INTEGER
);

CREATE TABLE responsavel (
nome VARCHAR(200),
receber_notificacao INTEGER,
idresponsavel SERIAL PRIMARY KEY,
idendereco INTEGER
);

CREATE TABLE tipo_contato (
idtipo_contato SERIAL PRIMARY KEY,
descricao VARCHAR(60)
);

CREATE TABLE endereco (
cep VARCHAR(9),
numero VARCHAR(20),
endereco VARCHAR(200),
idendereco SERIAL PRIMARY KEY,
idbairro INTEGER
);

CREATE TABLE log_justificativa (
log_justificativa SERIAL PRIMARY KEY,
descricao VARCHAR(200),
idresponsavel INTEGER,
idlog_aluno INTEGER,
FOREIGN KEY(idresponsavel) REFERENCES responsavel (idresponsavel)
);

CREATE TABLE contato (
principal INTEGER,
contato VARCHAR(200),
idcontato SERIAL PRIMARY KEY,
idtipo_contato INTEGER,
FOREIGN KEY(idtipo_contato) REFERENCES tipo_contato (idtipo_contato)
);

CREATE TABLE log_aluno (
data DATE,
tipo INTEGER,
hora VARCHAR(8),
idlog_aluno SERIAL PRIMARY KEY,
idaluno INTEGER,
FOREIGN KEY(idaluno) REFERENCES aluno (idaluno)
);

CREATE TABLE dia_semana (
iddia_semana SERIAL PRIMARY KEY,
nome VARCHAR(40)
);

CREATE TABLE disciplina (
nome VARCHAR(200),
iddisciplina SERIAL PRIMARY KEY
);

CREATE TABLE horario (
hora_inicio VARCHAR(10),
hora_final VARCHAR(10),
idhorario SERIAL PRIMARY KEY,
iddia_semana INTEGER,
iddisciplina INTEGER,
idperiodo INTEGER,
FOREIGN KEY(iddia_semana) REFERENCES dia_semana (iddia_semana),
FOREIGN KEY(iddisciplina) REFERENCES disciplina (iddisciplina)
);

CREATE TABLE periodo (
periodo VARCHAR(10),
idperiodo SERIAl PRIMARY KEY,
ano INTEGER,
idturma INTEGER
);

CREATE TABLE turma (
idturma SERIAL PRIMARY KEY,
nome VARCHAR(100),
idcurso INTEGER,
idturno INTEGER
);

CREATE TABLE curso (
idcurso SERIAL PRIMARY KEY,
nome VARCHAR(100)
);

CREATE TABLE turno (
idturno SERIAL PRIMARY KEY,
nome VARCHAR(30)
);

CREATE TABLE data_evento (
data DATE,
iddata_evento SERIAL PRIMARY KEY,
idevento INTEGER
);

CREATE TABLE evento (
idevento SERIAL PRIMARY KEY,
nome VARCHAR(100)
);

CREATE TABLE entrada_saida (
horario_saida VARCHAR(8),
horario_entrada VARCHAR(8),
identrada_saida SERIAL PRIMARY KEY,
iddata_evento INTEGER,
FOREIGN KEY(iddata_evento) REFERENCES data_evento (iddata_evento)
);

CREATE TABLE bairro (
idbairro SERIAL PRIMARY KEY,
nome VARCHAR(100),
idcidade INTEGER
);

CREATE TABLE cidade (
nome VARCHAR(100),
idcidade SERIAL PRIMARY KEY
);

CREATE TABLE responsavel_contato (
idresponsavel INTEGER,
idcontato INTEGER,
FOREIGN KEY(idresponsavel) REFERENCES responsavel (idresponsavel),
FOREIGN KEY(idcontato) REFERENCES contato (idcontato)
);

CREATE TABLE aluno_matriculado (
idhorario INTEGER,
idaluno INTEGER,
data DATE,
matriculado INTEGER,
FOREIGN KEY(idhorario) REFERENCES horario (idhorario),
FOREIGN KEY(idaluno) REFERENCES aluno (idaluno)
);

CREATE TABLE aluno_contato (
idcontato INTEGER,
idaluno INTEGER,
FOREIGN KEY(idcontato) REFERENCES contato (idcontato),
FOREIGN KEY(idaluno) REFERENCES aluno (idaluno)
);

CREATE TABLE aluno_evento (
idevento INTEGER,
idaluno INTEGER,
FOREIGN KEY(idevento) REFERENCES evento (idevento),
FOREIGN KEY(idaluno) REFERENCES aluno (idaluno)
);

CREATE TABLE aluno_responsavel (
idaluno INTEGER,
idresponsavel INTEGER,
FOREIGN KEY(idaluno) REFERENCES aluno (idaluno),
FOREIGN KEY(idresponsavel) REFERENCES responsavel (idresponsavel)
);

ALTER TABLE aluno ADD FOREIGN KEY(idendereco) REFERENCES endereco (idendereco);
ALTER TABLE responsavel ADD FOREIGN KEY(idendereco) REFERENCES endereco (idendereco);
ALTER TABLE endereco ADD FOREIGN KEY(idbairro) REFERENCES bairro (idbairro);
ALTER TABLE log_justificativa ADD FOREIGN KEY(idlog_aluno) REFERENCES log_aluno (idlog_aluno);
ALTER TABLE horario ADD FOREIGN KEY(idperiodo) REFERENCES periodo (idperiodo);
ALTER TABLE periodo ADD FOREIGN KEY(idturma) REFERENCES turma (idturma);
ALTER TABLE turma ADD FOREIGN KEY(idcurso) REFERENCES curso (idcurso);
ALTER TABLE turma ADD FOREIGN KEY(idturno) REFERENCES turno (idturno);
ALTER TABLE data_evento ADD FOREIGN KEY(idevento) REFERENCES evento (idevento);
ALTER TABLE bairro ADD FOREIGN KEY(idcidade) REFERENCES cidade (idcidade);
