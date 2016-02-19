*** Settings ***

Documentation   Casos de teste para CRUD do app comissoes.
Suite Setup     Começar webserver
Suite Teardown  Parar webserver
Resource        ../../resources/resources.robot

*** Test Cases ***

Scenario: Verificar campos obrigatórios
    Dado que estou na página ADICIONAR COMISSOES
    Quando seleciono Sim na lista id_unidade_deliberativa
    E clico no botão submit
    Então devo ver o texto Este campo é obrigatório.
    E não devo ver o texto Registro criado com sucesso!

Scenario: Criar uma comissão (somente campos obrigatórios)
    Dado que estou na página ADICIONAR COMISSOES
    Quando preencho o campo id_nome com Teste de Criação 1
    E preencho o campo id_sigla com TdC1
    E seleciono Tipo da Comissão na lista id_tipo
    E preencho o campo id_data_criacao com 01/01/2016
    E seleciono Sim na lista id_unidade_deliberativa
    E clico no botão submit
    Então devo ver o texto Registro criado com sucesso!
    E devo ver o texto Teste de Criação 1
    E devo ver o texto TdC1
    E devo ver o texto Tipo da Comissão
    E devo ver o texto 01/01/2016
    E devo ver o texto Sim

Scenario: Criar uma comissão (todos os campos)
    Dado que estou na página ADICIONAR COMISSOES
    Quando preencho o campo id_nome com Teste de Criação 2
    E preencho o campo id_sigla com TdC2
    E seleciono Tipo da Comissão na lista id_tipo
    E preencho o campo id_data_criacao com 02/01/2016
    E seleciono Não na lista id_unidade_deliberativa
    E preencho o campo id_data_extincao com 03/01/2016
    E preencho o campo id_local_reuniao com Sala 1
    E preencho o campo id_agenda_reuniao com 12h
    E preencho o campo id_telefone_reuniao com 1111-1111
    E preencho o campo id_endereco_secretaria com Rua A
    E preencho o campo id_telefone_secretaria com 2222-2222
    E preencho o campo id_fax_secretaria com 3333-3333
    E preencho o campo id_secretario com Nome do Secretário
    E preencho o campo id_email com secretario@email.com
    E preencho o campo id_apelido_temp com Apelido da Comissão
    E preencho o campo id_data_instalacao_temp com 04/01/2016
    E preencho o campo id_data_final_prevista_temp com 05/01/2016
    E preencho o campo id_data_prorrogada_temp com 06/01/2016
    E preencho o campo id_data_fim_comissao com 07/01/2016
    E clico no botão submit
    Então devo ver o texto Registro criado com sucesso!
    E devo ver o texto Teste de Criação 2
    E devo ver o texto TdC2
    E devo ver o texto Tipo da Comissão
    E devo ver o texto 02/01/2016
    E devo ver o texto Não
    E devo ver o texto 03/01/2016
    E devo ver o texto Sala 1
    E devo ver o texto 12h
    E devo ver o texto 1111-1111
    E devo ver o texto Rua A
    E devo ver o texto 2222-2222
    E devo ver o texto 3333-3333
    E devo ver o texto Nome do Secretário
    E devo ver o texto secretario@email.com
    E devo ver o texto Apelido da Comissão
    E devo ver o texto 04/01/2016
    E devo ver o texto 05/01/2016
    E devo ver o texto 06/01/2016
    E devo ver o texto 07/01/2016

Scenario: Excluir uma comissão
    Dado que estou na página COMISSOES
    Quando clico no link Teste de Exclusão CRUD
    E clico no link Excluir
    E espero 0.25 segundos
    E clico no botão submit
    Então devo ver o texto Registro excluído com sucesso!
    Dado que estou na página COMISSOES
    Então não devo ver o texto Teste de Exclusão CRUD

Scenario: Editar uma Comissão
    Dado que estou na página COMISSOES
    Quando clico no link Teste de Edição CRUD
    E clico no link Editar
    E espero 0.25 segundos
    E preencho o campo id_nome com Editado!
    E clico no botão submit
    Então devo ver o texto Registro alterado com sucesso!
    Dado que estou na página COMISSOES
    Então devo ver o texto Editado!
    E não devo ver o texto Teste de Edição CRUD
