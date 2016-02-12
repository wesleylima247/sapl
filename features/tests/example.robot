*** Settings ***

Documentation   Este é um exemplo de teste.
Suite Setup     Começar webserver
Suite Teardown  Parar webserver
Resource        ../resources/resources.robot

*** Test Cases ***

Scenario: Preencher id_nome verificar se aparece mensagem de erro
    Dado que eu estou na página ADICIONAR COMISSOES
    Quando eu preencho o campo id_nome com Nome da Comissão
    E eu clico no botão submit
    Então eu devo ver Este campo é obrigatório.

Scenario: Criar uma comissão valida
    Dado que eu estou na página ADICIONAR COMISSOES
    Quando eu preencho o campo id_nome com Nome da Comissão
    E eu preencho o campo id_sigla com NdC
    E eu seleciono Tipo da comissão na lista id_tipo
    E eu preencho o campo id_data_criacao com 01/01/2016
    E eu seleciono Sim na lista id_unidade_deliberativa
    E eu preencho o campo id_data_extincao com 02/01/2016
    E eu clico no botão submit
    Então eu devo ver Registro criado com sucesso!