*** Settings ***

Documentation   Arquivo de recursos para serem usados em testes.
Library         Selenium2Library


*** Variables ***

${SERVER}                       localhost:8081
${BROWSER}                      firefox
${DELAY}                        0
${HOME URL}                     http://${SERVER}/
${COMISSOES URL}                http://${SERVER}/comissoes/
${ADICIONAR COMISSOES URL}      http://${SERVER}/comissoes/create
${name}                         Nome da Comissão
@{model list}
@{lista das models}


*** Keywords ***

Dado que ${keyword}
    Run Keyword  ${keyword}
Quando ${keyword}
    Run Keyword  ${keyword}
E ${keyword}
    Run Keyword  ${keyword}
Então ${keyword}
    Run Keyword  ${keyword}

Começar webserver
    Open Browser  ${HOME URL}  ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Title Should Be  SAPL - Sistema de Apoio ao Processo Legislativo

Parar webserver
    Close Browser

estou na página ${nome da página}
    Go To  ${${nome da página} URL}

preencho o campo ${nome do campo} com ${informação}
    Input Text  ${nome do campo}  ${informação}

seleciono ${info} na lista ${lista}
    Select From List  ${lista}  ${info}

clico no botão ${nome do botão}
    Click Button  name=${nome do botão}

clico no link ${nome do link}
    Click Link  ${nome do link}

clico no elemento ${nome do elemento}
    Click Element  ${nome do elemento}

devo ver ${texto}
    Page Should Contain  ${texto}

não devo ver ${texto}
    Page Should Not Contain  ${texto}