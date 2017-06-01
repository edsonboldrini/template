CREATE FUNCTION verifica_aluno_matricula_varias_turmas() RETURNS TRIGGER AS 
$$
BEGIN

IF EXISTS (	select idaluno from matricula WHERE matriculado = 1 group by idaluno having count(*) > 1	
	) THEN
RAISE EXCEPTION 'Erro: aluno matriculado em mais de uma turma!';
END IF;
RETURN NULL;

END
$$ LANGUAGE plpgsql;

CREATE TRIGGER checkAlunoMatriculaVariasTurmasTrigger
AFTER INSERT OR UPDATE OF matriculado ON matricula
FOR EACH ROW
EXECUTE PROCEDURE verifica_aluno_matricula_varias_turmas();


CREATE FUNCTION verifica_aluno_responsavel_receber_notificacao() RETURNS TRIGGER AS 
$$
BEGIN

IF EXISTS (select idaluno from responsavel
INNER JOIN aluno_responsavel ON responsavel.idresponsavel = aluno_responsavel.idresponsavel
WHERE receber_notificacao = 1 group by idaluno having count(*) = 0) THEN
RAISE EXCEPTION 'Erro: aluno precisa ter pelo menos um responsavel para receber notificação!';
END IF;
RETURN NULL;

END
$$ LANGUAGE plpgsql;

CREATE TRIGGER checkAlunoResponsavelReceberNotificacaoTrigger
AFTER INSERT OR UPDATE OF matriculado ON matricula
FOR EACH ROW
EXECUTE PROCEDURE verifica_aluno_responsavel_receber_notificacao();


