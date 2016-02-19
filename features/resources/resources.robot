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

# Obs.: a keyword 'espero x segundo(s)' é preciso ser usada em alguns casos
#       para evitar erros. O erro ocorre quando o robot framework tenta
#       encontrar um elemento antes da página ser carregada.
espero 1 segundo
    Sleep  1

espero ${segundos} segundos
    Sleep  ${segundos}

estou na página ${página}
    Go To  ${${página} URL}

preencho o campo ${campo} com ${informação}
    Input Text  ${campo}  ${informação}

seleciono ${info} na lista ${lista}
    Select From List  ${lista}  ${info}

clico no botão ${botão}
    Click Button  name=${botão}

clico no link ${link}
    Click Link  ${link}

clico no elemento ${elemento}
    Click Element  ${elemento}

devo ver o texto ${texto}
    Page Should Contain  ${texto}

não devo ver o texto ${texto}
    Page Should Not Contain  ${texto}

devo ver o link ${link}
    Page Should Contain Link  ${link}

seleciono o checkbox ${checkbox}
    Select Checkbox  ${checkbox}