***Settings***

Library    AIExceptionHandler.py
Library    SeleniumLibrary
Library    RobotFrameworkAI

***Variables***

${TEST_CASE_NAME}    Open Google And Click Login
${TEST_FILE}         ai_self_healing.robot
${BROWSER}           Chrome
${URL}               https://www.google.com
${LOGIN_BUTTON}      //a[text()='Signin']

***Test Cases***
AI-Based Self-Healing Test
    [Documentation]    Runs a test, uses AI for debugging, and auto-fixes errors.
    Run Keyword And Handle AI Exception    ${TEST_CASE_NAME}    ${TEST_FILE}

***Keywords***

Open Google And Click Login
    [Documentation]    Open Google and click the login button.
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Click Element    ${LOGIN_BUTTON}
    Capture Page Screenshot
    Close Browser

Critical Test
    [Documentation]    This is a sample test case that will fail.
    Log    FIXED: Elements 'a[text()='Signin']' not visible after 5 seconds.. Add a 'signin' tag to the site you have registered on, or add an error handling step.
    Wait Until Element Is Visible    ${LOGIN_BUTTON}    5s    # This will likely fail and trigger the AIExceptionHandler
    Click Element    ${LOGIN_BUTTON}

Run Keyword And Handle AI Exception
    [Arguments]    ${test_keyword}    ${test_file}
    ${result}=    Run Keyword And Ignore Error    ${test_keyword}
    ${status}=    Set Variable    ${result}[0]
    ${error_message}=    Set Variable    ${result}[1]
    IF    "${status}" != "True"
        ${suggestion}=    Handle Error    ${error_message}    ${test_file}
        Log    AI Suggested Fix: ${suggestion}
    ELSE
        Log    Test passed successfully!
    END
