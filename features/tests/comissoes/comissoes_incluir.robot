*** Settings ***

Documentation   Casos de teste para incluir parlamentares em comissoes.
Suite Setup     Começar webserver
Suite Teardown  Parar webserver
Resource        ../../resources/resources.robot

*** Test Cases ***

Scenario: Incluir parlamentar
    Dado que estou na página COMISSOES
    Quando clico no link Teste de Inclusão Parlamentar
    E clico no link Composição
    E clico no link Incluir Parlamentar
    E espero 0.5 segundos
    E seleciono Nome Completo - NdP - Nome do Partido na lista id_parlamentar_id
    E seleciono Cargo Comissão na lista id_cargo
    E preencho o campo id_data_designacao com 08/01/2016
    E seleciono o checkbox id_titular
    E clico no botão submit
    Então devo ver o link Nome Parlamentar
    E devo ver o texto Cargo Comissão
    E devo ver o texto Sim
    E devo ver o texto 08/01/2016

Scenario: Editar a inclusão de parlamentar
    Dado que estou na página COMISSOES
    Quando clico no link Teste de Edição Parlamentar
    E clico no link Composição
    E clico no link Edição Nome Parlamentar
    E espero 0.5 segundos
    E preencho o campo id_motivo_desligamento com Editado!
    E clico no botão submit
    Então devo ver o texto Editado!
