*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
#Input Login Command
#    Input  login
    
Run Registration
    Run Application

Input Login Command
    Input  login

Input New Command
    Input  new
    Run Application
    
Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input  new
    Input  ${username}
    Input  ${password}

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
