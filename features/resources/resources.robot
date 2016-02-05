*** Settings ***

Documentation   A simple exemple test that open a page and
...             fill an input text box. This is the resource file
...             wich contains the keywords and variables used in the tests.
Library         Selenium2Library
Library         ModelMommyStubs

*** Variables ***

${SERVER}                       localhost:8081
${BROWSER}                      firefox
${DELAY}                        0
${HOME URL}                     http://${SERVER}/
${ADICIONAR COMISSOES URL}      http://${SERVER}/comissoes/create
${name}                         Nome da Comissão

*** Keywords ***

Start the webserver
    Open Browser  ${HOME URL}  ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Title Should Be  SAPL - Sistema de Apoio ao Processo Legislativo

Stop the webserver
    Close Browser

I have the stubs to ${model name} app
    Create Stub  ${model name}

I fill ${field name} with ${info}
    Input Text  ${field name}  ${info}

I click the ${submit} button
    Click Button  name=${submit}

I should see ${text}
    Page Should Contain  ${text}

I am in ${page name} page
    Go To  ${${page name} URL}

I select value ${value} in ${field name} list
    Select From List by Index  ${field name}  ${value}