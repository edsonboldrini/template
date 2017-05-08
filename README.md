# TRABALHO INTEGRADO: Título do trabalho

Trabalho desenvolvido durante as disciplinas de:
- Banco de Dados 2, 
- Engenharia de Software, 
- Programação Orientada a Objetos 2,
- Projeto de Sistemas


**INTEGRANTES DO GRUPO:** 
- Edson Simões Boldrini
- Pedro Henrique Costa<br>

        
# Sumário


# Gerência de Requisitos

## 1	Motivação e Propósito do Sistema 
Este documento contém a especificação do projeto do banco de dados "Controle de acesso por RFID" que tem como motivação oferecer uma maior segurança aos alunos do IFES Campus Serra.<br>

## 2	Personas
O diretor de ensino quer ter um controle maior sobre os alunos do ensino médio que estão no campus e assim, poder avisar aos seus respectivos responsáveis, como estes estão frequentando o Campus.<br>

## 3	Minimundo
<p align="justify">
O IFES (Instituto Federal do Espírito Santo) campus Serra está inserindo alunos do ensino médio em suas dependências disponibilizando cursos técnicos integrados ao ensino médio para adolescentes interessados em aprenderem algo a mais do que o ensino médio normal.
<br>
Esses adolescentes são, em boa parte, menores de idade, e/ou ainda moram e/ou tem alguma dependência com seus respectivos pais ou responsáveis. Com isso, deseja-se construir um sistema para controle de entrada e saída dos alunos do ensino médio do ifes campus serra.
<br>
No portão de entrada principal será instalado um leitor de RFID e todo acesso de entrada e saída ficará registado em um log. O controle de acesso de cada aluno será baseado no horário da sua turma, cada turma possui seus horários de entradas e saídas da parte da manhã e tarde, conforme os horários dos alunos pode não haver registro de logs de entrada ou saída.
<br>
Cada curso oferecido pode haver várias turmas conforme o passar dos anos. Para o curso deseja armazenar (nome e código), já para turmas deseja armazenar (nome e código) e de qual curso ela pertence. Os registro dos horários de entrada e saída de cada turma pode ser diferente conforme o dia da semana e no mesmo dia pode haver diferentes horários de entradas e saída.
<br>
Dos alunos deseja armazenar (nome, codigo, endereço, matrícula), quais turmas eles está matriculado e já foi matriculado. Os mesmo  podem ter vários responsáveis que precisa armazenar (nome, endereço, vários contatos e se deseja receber notificação caso houver atraso), e, como base de um sistema automático, será disponibilizado aos responsáveis todos os logs de acesso (data, hora) para que, eles possam fazer o acompanhamento do acesso do aluno a instituição.
<br>
A situação do aluno no log poderia indicar, se o aluno está na instituição ou não, se ele tem faltado muitas aulas e até mesmo se o aluno se encontra em educação física ou visita técnica.
<br>
Pode haver alguns eventos atípicos como visita técnica, aulas extras, palestras que também deve ser registrado de log dos alunos. Dos eventos deseja armazenar (nome, tipo do evento, data, horários conforme a turma). 
<br></p>


## 4	Requisitos de Usuários
### 4.1	Requisitos Funcionais (Histórias de Usuário)
<!--
| ID | Descrição | Prioridade | Pontos |
| --- | --- | --- | --- |
| RF01 | EU, COMO  **QUEM**, QUERO/GOSTARIA/DEVO/POSSO **O QUE**, PARA QUE/DE/PARA **PORQUE/RESULTADO**. | Must | 2 |
| RF02 | EU, COMO cliente, POSSO acessar o acerto da locadora PARA QUE consiga ver os filmes disponíveis antes de sair de casa. | Should | 3 |
-->

| ID | Descrição | Prioridade | Pontos |
| --- | --- | --- | --- |
| RF01 | Eu como Diretor, quero que o sistema realize cadastro de aluno. | Must | 1 |
| RF02 | Eu como Diretor, quero que o sistema realize cadastro de responsável. | Must | 1 |
| RF03 | Eu como Diretor, quero que o sistema realize cadastro curso. | Must | 1 |
| RF04 | Eu como Diretor, quero que o sistema realize cadastro de turma. | Must | 1 |
| RF05 | Eu como Diretor, quero que o sistema realize matrícula do aluno na turma. | Must | 1 |
| RF06 | Eu como Diretor, quero que o sistema realize cadastro de eventos(palestras,aulas extras, visitas técnicas etc) visando horários atípicos de entrada/saída | Would | 2 |
| RF07 | Eu como Diretor, quero que o sistema gere relatórios de atraso de alunos. | Should | 2 |
| RF08 | Eu como Diretor, quero que o sistema gere relatórios de entrada e saída de alunos. | Should | 2 |
| RF09 | Eu como Responsável, quero que o sistema disponibilize para mim todo histórico de entrada/saída dos alunos. | Should | 2 |
| RF10 | Eu como Responsável, quero que o sistema envie notificação com horário de entrada/saída do aluno. | Must | 1 |
| RF11 | Eu como Aluno, quero que o sistema me informe quantos dias eu cheguei atrasado. | Could | 1 |
| RF12 | Eu como Aluno, quero que o sistema me informe cada vez que meu responsável for notificado. | Could | 1 |
| RF13 | Eu como Aluno, quero que o sistema me notifique para não chegar mais atrasado(estourar limite). | Should | 1 |
| RF14 | Eu como Aluno, quero que o sistema me envie um lembrete para não me atrasar mais em dias que eu sempre me atraso(recorrência). | Would | 1 |
| RF15 | Eu como Administrador, quero que o sistema possa ser usado em qualquer escola. | Would | 1 |

### 4.2	Requisitos Não Funcionais
<!--
| ID | Descrição | Prioridade | Categoria | Escopo |
| --- | --- | --- | --- | --- |
| RNF01 | A entrada de dados de efetuar locação pelo atendente deverá ser realizada em no máximo 30 segundos | Must | 2 | Facilidade de Operação | Funcionalidade |
| RNF02 | O tempo de resposta de efetuar locação dever ser de no máximo 2 segundos a partir da entrada correta de dados | Should | 3 | Eficincia de Tempo | Funcionalidade |
-->

| ID | Descrição | Prioridade | Categoria | Escopo |
| --- | --- | --- | --- | --- |
| RNF01 | O sistema deve ler log disponibilizado pelos leitores de RFID. | Must | 2 | Usabilidade |
| RNF02 | O sistema deve ser acessado de forma web para responsáveis do aluno. | Must | 2 | Portabilidade |
| RNF03 | O sistema precisa de um login para manter a segurança das informações. | Must | 2 | Segurança |
| RNF04 | O sistema deve ser capaz de exportar relatórios em formatos pdf e xls. | Should | 2 | Funcionalidade |
| RNF05 | O sistema deve ser capaz de enviar e-mail/mensagem com horário de entrada/saída do aluno. | Should | 1 | Funcionalidade |
| RNF06 | O sistema deve enviar notificação caso escolhido pelo responsável caso x minutos de atraso. | Could | 2 | Funcionalidade |

### 4.3	Regras de Negócio
<!--
| ID | Descrição | Prioridade | 
| --- | --- | --- |
| RN01 | Uma reserva expira quando passadas mais do que 24h de sua comunicação para o cliente. | Must |
| RN02 | Clientes em atraso não podem efetuar nem locações nem reservas. | Should |
-->

| ID | Descrição | Prioridade | 
| --- | --- | --- |
| RN01 | Caso aluno chegar 3 vezes atrasado mais de 15 minutos será punido e o responsável será notificado (punição a definir). | Should |
| RN02 | Qualquer saída do aluno da instituição com período muito grande (2h) deve enviar notificação. | Could |

# Desenvolvimento do Sistema
## 1.    Análise de Sistemas:
### 1.1  Subsistemas
inserir diagrama dos subsistemas UML<br>
![Alt text](https://github.com/edsonsb96/template/blob/master/Subsistemas.png)

### 1.2  Modelagem de Casos de uso 
inserir diagramas dos Casos de Uso (UML) e descrever brevemente.

### Caso de Uso - Enviar notificação de aluno atrasado <br>
- Selecionar Turmas;<br>
- - Para cada turma;<br>
- - - Para cada aluno da turma;<br>
- - - - Para cada log de entrada do aluno;<br>
- - - - - Verificar atraso conforme horário do dia;<br>
- - - - Caso houver atraso;<br>
- - - - - Verificar notificação habilitada responsável;<br>
- - - - - Selecionar responsável aluno;<br> 
- - - - - Sistema envia mensagem(comunicação escolhida pelo responsável) informando que o dependente está atrasado;<br>
![Alt text](https://github.com/edsonsb96/template/blob/master/UseCase1%20Diagram.png)

### Caso de Uso - Listar relatório entrada aluno
Selecionar Aluno<br>
Para cada log de entrada do aluno;<br>
Verificar atraso conforme horário do dia;<br>
Realizar cálculo de minutos de atraso;<br>
Listar usuário horários e devidos atrasos;<br>
![Alt text](https://github.com/edsonsb96/template/blob/master/UseCase2%20Diagram.png)

### 1.3  Modelagem Estrutural (Modelo Conceitual)
** ATENÇO: USAR Notação Entidade-Relacionamentos se estiver fazendo BD2 e o diagrama de classes se estiver fazendo Projeto de Sistemas**
![Alt text](https://github.com/discipbd2/topicos-trabalho/blob/master/sample_MC.png?raw=true "Modelo Conceitual")
###1.4  Modelagem Comportamental
Inserir principais diagramas comportamentais da análise (principalmente, estados)
###1.5  Dicionário de Dados
[classe/entidade]: [descrição da classe]
    
    EXEMPLO:
    CLIENTE: classe/entidade que representa as informações relativas ao cliente<br>
    CPF: atributo que representa o número de Cadastro de Pessoa Física para cada cliente da empresa.<br>
    
## 2.    Projeto de Sistemas:
### 2.1  Projeto Arquitetural 
#### 2.1.1   Plataforma de Implementação e Tecnologias
O software foram divididos em alguns subsistemas ‘controle de aluno’, ‘log de acesso’ e  ‘controle acesso responsável’  será desenvolvido utilizando linguagem de programação PHP juntamente com framework laravel com o banco de dados (PostgreSQL) para parte de back-end, o front-end alguns frameworks como Bootstrap, jquery e alguns plugins derivados do jquery, porém no subsistema ‘controle acesso responsável’ a parte mobile será desenvolvida usando framework ionic. A escolha do sistema web no subsistema ‘controle de aluno’ foi requisito descrito pelo solicitante, já o subsistema ‘controle acesso responsável’ como responsáveis precisam de ter acesso a qualquer momento será implementado duas versões uma web e outra mobile. 

#### 2.1.2   Atributos de Qualidade e Táticas
 CATEGORIAS | RNF'S | TÁTICAS | 
| --- | --- | --- |
| Facilidade de Operação | RNF03, RNF08| Prover ao usuário a capacidade de entrar com comandos que permitam operar o sistema de modo mais eficiente. Para tal, as interfaces do sistema devem permitir, sempre que possível, a entrada por meio de seleção ou leitura de código de barras ao invés da digitação de campos. | 


#### 2.1.3   Arquitetura de Software
![Alt text](https://github.com/edsonsb96/template/blob/master/Arquitetura_Sistema.png?raw=true "Arquitetura de Software")

O software foi dividido em 3 subsistemas  ‘controle de aluno’, ‘log de acesso’ e  ‘controle acesso responsável’. A arquitetura que será usada vai ser camadas juntamente com partições visto que para sistema em si ficará mais organizado e fácil para futuras alterações. Será adotado o padrão MVC para subsistema ‘controle de aluno’, ‘log de acesso’ e Camada de Serviço para ‘controle acesso responsável’ visto que pode ser tanto web quanto mobile. Toda gerência de dados será realizada pelo padrão DAO. Praticamente todo sistema terá uma camada de controle interface com usuário, lógica de negócio e gerência de dados.

### 2.2. Projeto Detalhado
OBS: repetir as seções abaixo para cada subsistema
#### 2.2.1.   Projeto da Lógica de Negócio
##### Projeto do Domínio
###### Diagrama de Classe Análise
![Alt text](https://github.com/edsonsb96/template/blob/master/DiagramaClasseAnalise.png?raw=true "Diagrama de Classe Analise")

###### Diagrama de Classe Projeto
![Alt text](https://github.com/edsonsb96/template/blob/master/DiagramaClasseProjeto.png?raw=true "Diagrama de Classe Projeto")

###### Justificativas

- Foi criado navegação de dupla entre Aluno e Responsável para que nas buscas, quanto partir do alunos encontrar os responsáveis e vice e versa. 
- Foi criado a classe “TipoContato” por motivos que podem surgir no futuro novos tipos de contatos porém terá como início os valores (Telefone, E-mail, Celular).
- Foi criado a classe “Bairro” e “Cidade” para reaproveitamento de informações que forem cadastradas nos próximos cadastros, visto que comum pessoas morarem no mesmo bairros e cidades.
- Foi criado o enum “DiaSemana” visto que dias das semanas são sempre (Segunda, Terça, Quarta, Quinta, Sexta, Sábado e Domingo), a possibilidade de mudança e praticamente mínima de acontecer.
- Todas as outras navegabilidades são justificadas por as classes serem as mais fortes nos relacionamentos.

##### Projeto da Aplicação

###### Caso de Uso Enviar Notificação
![Alt text](https://github.com/edsonsb96/template/blob/master/DiagramaSequenciaEnviarNotificacao.png?raw=true "Enviar Notificação")

###### Caso de Uso Relatório Entrada Saida Aluno
![Alt text](https://github.com/edsonsb96/template/blob/master/DiagramaSequenciaRelatorioEntradaSaidaAluno.png?raw=true "Relatório Entrada Saida Aluno")

#### 2.2.2.  Projeto da Interface com Usuário
##### Projeto da Visão
A apresentação controle de acesso completa pode ser encontrada [aqui](https://github.com/edsonsb96/template/blob/master/Modelo_Tela.pdf). <br>
A apresentação acesso responsáveis completa pode ser encontrada [aqui](https://github.com/edsonsb96/template/blob/master/Cadastro%20RFID.pdf).

#####Projeto da Interação Humana
apresentar diagrama de classes da IU com controladores e diagrama de sequências. Apresentar diagrama com estados de navegação.
#### 2.2.3.  Projeto da Persistência de Dados
apresentar classes de acesso ao banco de dados. apresentar diagramas de sequência.

#### 2.4.   Padrões
#####Padrões Arquiteturais
#####Padrões de Projeto

No diagrama abaixo é destacado o padrão de projeto método fábrica que foi utilizado para melhorar a coesão e diminiuir o acoplamento entre as clases do sistema. O pode-se notar a classe FabricaDeFormatos cria os objetos FormatoPng, FormatoJpeg e FormatoGif tirando a dependencia entre a classes Main e essas classes. Vale ressaltar que o padrão utiliza um Interface Formato para diminiuir o acoplamento entre as classes.

![Alt text](https://github.com/felipefo/poo2/blob/master/Padroes_de_Projeto/Cria%C3%A7%C3%A3o/metodo_fabrica/ImagemMetodoFabrica/padrao_metodo_fabrica_conversao_imagem.png)


O padrão foi utilizado para resolver o problema de .....

O padrão foi utilizado para resolver o problema de .....


## 3.    Banco de Dados (BD)


### 3.1 Decisões do Projeto 
    [atributo]: [descrição da decisão]
    
    EXEMPLO:
    a) Campo endereço: em nosso projeto optamos por um campo multivalorado e composto, pois a empresa 
    pode possuir para cada departamento mais de uma localização... 
    b) justifique!


### 3.2	Modelo Lógico<br>
### 3.3	MODELO FÍSICO<br>
### 3.4	INSERT APLICADO NAS TABELAS DO BANCO DE DADOS<br>
#### 3.4.1 DETALHAMENTO DAS INFORMAÇÕES
        Detalhamento sobre as informações e processo de obtenção ou geração dos dados.
        Informar/referenciar todas as fontes usadas para:
        a) obtenção dos dados
        b) obtenção de códigos reutilizados (caso tenha feito uso destes)
        c) fontes de estudo para desenvolvimento do projeto
        
####3.4.2 INCLUSÃO DO SCRIPT PARA CRIAÇÃO DE TABELAS E INSERÇÃO DOS DADOS (ARQUIVO ÚNICO COM):
        a) inclusão das instruções para criação das tabelas e estruturas de amazenamento do BD
        b) inclusão das instruções de inserção dos dados nas referidas tabelas
        c) inclusão das instruções para execução de outros procedimentos necessários

### 3.5	TABELAS E PRINCIPAIS CONSULTAS<br>
#### 3.5.1	GERACAO DE DADOS (MÍNIMO DE 1,5 MILHÃO DE REGISTROS PARA PRINCIPAL RELAÇAO)<br>
    Data de Entrega: (Data a ser definida)
<br>
OBS: Incluir para os tópicos 3.5.2 e 3.5.3 as instruções SQL + imagens (print da tela) mostrando os resultados.<br>

#### 3.5.2	SELECT DAS TABELAS COM PRIMEIROS 10 REGISTROS INSERIDOS<br> 
    Data de Entrega: (Data a ser definida)
<br>
#### 3.5.3	SELECT DAS VISÕES COM PRIMEIROS 10 REGISTROS<br>
        a) Descrição da view sobre que grupos de usuários (operacional/estratégico) <br>
        e necessidade ela contempla.
        b) Descrição das permissões de acesso e usuários correlacionados (após definição <br>
        destas características)
    Data de Entrega: (Data a ser definida)
<br>
#### 3.5.4	LISTA DE CODIGOS DAS FUNÇÕES, ASSERÇOES E TRIGGERS<br>
        Detalhamento sobre funcionalidade de cada código.
        a) Objetivo
        b) Código do objeto (função/trigger/asserção)
        c) exemplo de dados para aplicação
        d) resultados em forma de tabela/imagem
<br>
#### 3.5.5	Administração do banco de dados<br>
        Descrição detalhada sobre como serão executadas no banco de dados as <br>
        seguintes atividades.
        a) Segurança e autorização de acesso:
        b) Estimativas de aquisição de recursos para armazenamento e processamento da informação
        c) Planejamento de rotinas de manutenção e monitoramento do banco
        d) Plano com frequencia de análises visando otimização de performance
<br>
#### 3.5.6	Backup do Banco de Dados<br>
        Detalhamento do backup.
        a) Tempo
        b) Tamanho
        c) Teste de restauração (backup)
        d) Tempo para restauração
        e) Teste de restauração (script sql)
        f) Tempo para restauração (script sql)
<br>

#### 3.5.7	APLICAÇAO DE ÍNDICES E TESTES DE PERFORMANCE<br>
    a) Lista de índices, tipos de índices com explicação de porque foram implementados
    b) Performance esperada VS Resultados obtidos
    c) Tabela de resultados comparando velocidades antes e depois da aplicação dos índices.
<br>
    Data de Entrega: (Data a ser definida)
<br>   
#### 3.5.8	ANÁLISE DOS DADOS COM ORANGE<br>    
    a) aplicação de algoritmos e interpretação dos resultados
<br>
    Data de Entrega: (Data a ser definida)
<br>
### 3.6	ATUALIZAÇÃO DA DOCUMENTAÇÃO/ SLIDES E ENTREGA FINAL<br>
<br>
    Data de Entrega: (Data a ser definida)
<br>
### 3.7	DIFICULDADES ENCONTRADAS PELO GRUPO<br>  




# Gestão de Configuração
## 1.    Metodologia
descrever metodologias e políticas que serão usadas para realizar a gestão de configuração como, por exemplo, Gitflow, rastreabilidade de requisitos e mudanças. É necessário descrever em detalhes os procedimentos.
## 2.    Arquitetura
descrever ferramentas e a integração dessas para a arquitetura. 
## 3.    Integração Contínua e Delivery Contínua
Descrever como será aplicado esses conceitos.

# Gestão de Projetos
## 1.    Project Model Canvas (PMC)
Visão geral do projeto.
## 2.    Cronograma macro de sprints 
datas dos sprints.
## 3.    Backlog de histórias de Usuário 
lista de histórias de usuário categorizadas, priorizadas e com o esforço. A categorização deve utilizar a técnica MoSCoW. 
Acompanhamento do projeto: o grupo deve apresentar histórico, por sprint,  do acompanhamento do projeto da seguinte forma:
- Apresentando o Burndown do projeto.
- Apresentando a velocidade do time.
- Modificações do backlog.
## 4.    Burn down dos sprints
acompanhamento dos sprints. Cada Sprint deve ter uma seção descrevendo o que foi realizado e o planejado (por meio do  o gráfico e Burndown do Sprint).
## 5.    Retrospectiva 
Apresentar a retrospectiva da equipe do sprint realizado.

# Gerência de Qualidade
## 1.    Métricas de qualidade 
definir métricas de qualidade para cada artefato do projeto como, por exemplo, quantidade de codesmell, complexidade ciclomática e outras. 
## 2.    Classes de equivalência e particionamento de equivalência 
defina as classes de equivalências para as métricas de qualidade. 

## 3.    Medição 
seção que escreve como as métricas estão sendo atingidas. Essa seção deve ser atualizada por sprint. 
## 4.    Testes
Técnicas utilizadas para os testes: apresentar as técnicas utilizadas para o planejamento e execução de testes como, por exemplo, teste funcional sistemático e testes estruturais. 
## 5.    Cenário de Teste
apresentar todos os cenários de teste sucesso e falhas das histórias de usuário.  
## 6.    Histórico  
O grupo deve apresentar a evolução da qualidade dos itens ao longo das entregas, ou seja, em outras palavras, o grupo deve apresentar o histórico de evolução da qualidade dos artefatos de software e discursar o motivo da evolução.

# Diário de Bordo

o grupo deve apresentar semanalmente um relato da atividade do grupo. O relato pode conter qualquer tipo de informação (fotos, vídeos) que possam auxiliar no entendimento das atividades do grupo. 

OBS: organize o diário para que não se misture com a documentação. de preferência, coloque-o em outra página.

**FORMATACAO NO GIT:** https://help.github.com/articles/basic-writing-and-formatting-syntax/
