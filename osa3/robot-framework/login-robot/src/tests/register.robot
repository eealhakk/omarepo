*** Settings ***
Resource  resource.robot
Test Setup  Input New Command
Test Teardown  Run Registration



*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  validuser  ValidPass123
    Output Should Contain  Empty

Register With Already Taken Username And Valid Password
    Input Credentials  existinguser  ValidPass123
    Input New Command And Create User  existinguser  ValidPass123
    Output Should Contain  Username and password are required

Register With Too Short Username And Valid Password
    Input Credentials  aja  ValidPass1232
    Output Should Contain  Invalid username

#Register With Enough Long But Invalid Username And Valid Password
#
#
#Register With Valid Username And Too Short Password
#
#
#Register With Valid Username And Long Enough Password Containing Only Letters