*** Settings ***
Library   RobotFrameworkAI
Library    Collections
Library    OperatingSystem
Library    GeneralRealTestDataGenerator

*** Variables ***


*** Test Cases ***
Generate Specific Test Data
     [Documentation]    Test
     ${response}=  Generate Test Data    openai    address
     Log    ${response}


Generate Custom Test Data
    ${response}=  Generate General Test Data    openai    prompt=Generate Real Negative testdata for login google email and password like 9 scenarios 1) Missing "@", 2) Missing domain,3) Missing username, 4) Invalid characters org name,5) Spaces in email, 6) Multiple "@" symbols, 7) Exceeding character limit: An email address longer than 254 characters,8) Missing top-level domain,9) Invalid top-level domain, Consecutive dots. only keep test data.
#    Based various scenario of Negative test date, generate testdate Cases like 1.Entering an incorrect password for a valid username, 2.Entering an incorrect username for a valid password, 4.Entering a password that does not meet password strength requirements (If password should have alhnumeric,1 specialchar), 5.Testing login with excessive length usernames and passwords (Let name and pass should not more then 10char).,6.Testing login with incorrect case (uppercase/lowercase) in the username.
    Log    ${response}
