*** Settings ***
Library           ../../Python27/Lib/Robot_Libraries/abacus/Abacus.py

*** Test Cases ***
connect
    connect    localhost    localhost    BBDLC_System_GR303_MGCP_Sip_PulseDial.env    bbdlc
