*** Settings ***

Documentation   This an example test.
Suite Setup     Start the webserver
Suite Teardown  Stop the webserver
Resource        ../resources/resources.robot

*** Test Cases ***

Scenario: Fill id_nome and check if the page contains a text
    Given I am in ADICIONAR COMISSOES page
    When I fill id_nome with Nome da Comissão
    And I click the submit button
    Then I should see Este campo é obrigatório.

# This test scenario is incomplete.
Scenario: Create a comissão
    Given I have the stubs to comissoes app
    And I am in ADICIONAR COMISSOES page
    When I fill id_nome with Nome da Comissão
    And I fill id_sigla with NdC
    # And I select value 1 in id_tipo list
    And I fill id_data_criacao with 01/01/2016
    And I select value 1 in id_unidade_deliberativa list
    And I fill id_data_extincao with 01/01/2016
    And I click the submit button
    Then I should see Este campo é obrigatório.
