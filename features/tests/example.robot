*** Settings ***

Documentation   Caso de teste para CRUD do app comissoes
Suite Setup     Começar webserver
Suite Teardown  Parar webserver
Resource        ../resources/resources.robot

*** Test Cases ***

Scenario: Verificar campos obrigatórios
    Dado que estou na página ADICIONAR COMISSOES
    Quando preencho o campo id_nome com Nome da Comissão
    E clico no botão submit
    Então devo ver Este campo é obrigatório.

Scenario: Criar uma comissão (somente campos obrigatórios)
    Dado que estou na página ADICIONAR COMISSOES
    Quando preencho o campo id_nome com Teste de Criação 1
    E preencho o campo id_sigla com TdC1
    E seleciono Tipo da Comissão na lista id_tipo
    E preencho o campo id_data_criacao com 01/01/2016
    E seleciono Sim na lista id_unidade_deliberativa
    E clico no botão submit
    Então devo ver Registro criado com sucesso!
    E devo ver Teste de Criação 1
    E devo ver TdC1
    E devo ver Tipo da Comissão
    E devo ver 01/01/2016
    E devo ver Sim

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

    Então devo ver Registro criado com sucesso!
    E devo ver Teste de Criação 2
    E devo ver TdC2
    E devo ver Tipo da Comissão
    E devo ver 02/01/2016
    E devo ver Não
    E devo ver 03/01/2016
    E devo ver Sala 1
    E devo ver 12h
    E devo ver 1111-1111
    E devo ver Rua A
    E devo ver 2222-2222
    E devo ver 3333-3333
    E devo ver Nome do Secretário
    E devo ver secretario@email.com
    E devo ver Apelido da Comissão
    E devo ver 04/01/2016
    E devo ver 05/01/2016
    E devo ver 06/01/2016
    E devo ver 07/01/2016

Scenario: Excluir uma comissão
    Dado que estou na página COMISSOES
    Quando clico no link Teste de Exclusão
    E clico no link Excluir
    E clico no botão submit
    Então devo ver Registro excluído com sucesso!
    Dado que estou na página COMISSOES
    Então não devo ver Teste de Exclusão

Scenario: Editar uma Comissão
    Dado que estou na página COMISSOES
    Quando clico no link Teste de Edição
    E clico no link Editar
    E preencho o campo id_nome com Editado!
    E clico no botão submit
    Então devo ver Registro alterado com sucesso!
    Dado que estou na página COMISSOES
    Então devo ver Editado!
    E não devo ver Teste de Edição