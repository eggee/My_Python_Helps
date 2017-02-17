*** Settings ***
Library           ../../../Workspace/TautCore/Libraries/Communication/Telnet/TautTelnet.py
Library           ../../../Workspace/TautCore/Libraries/Platform/TA5K/Ta5k.py


*** Variables ***
${LoginUserName}    ADMIN
${LoginPassword}    PASSWORD
${IP_Address}     10.13.138.101
${scalar}         ${EMPTY}
@{nodes}          1    16    17    18

*** Test Cases ***
login
    [Documentation]    *TestCase* User should be able to login to a Telnet Session
    Open Connection    ${IP_Address}
    Login    ${LoginUserName}    ${LoginPassword}    Username:    Password
    Set Prompt    B
    execute command    term len 0

show_auto_shelf
    execute command    sho auto shelf

logout
    Close Connection

New

*** Keywords ***
prompt
