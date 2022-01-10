*** Setting ***
Documentation            test 
Library                  SeleniumLibrary


*** Variables ***
${Browser}               Chrome
${username}              user01
${password}              abc123
${homeurl}               https://m.twitch.tv/  

*** Test Cases ***
Open Url
     [Setup]  Run Keywords
     Open Browser       ${homeurl}        ${Browser}

search
     waitForElementPresent               xpath=//*[@id="__next"]        
     Click                               xpath=//a[@href="/search"]
     waitForElementPresent               xpath=//*[@id="__next"]
     click                               xpath=//input[@value='']
     type                                xpath=//input[@value='']                                                                Monster Hunter World
     sendKeys                            xpath=//input[@value='Monster Hunter World']                                            ENTER
     sleep                               3

searchmore 
     waitForElementPresent               xpath=//a[@href="/search?term=Monster%20Hunter%20World&type=channels"]  
     clickAndWait                        xpath=//a[@href="/search?term=Monster%20Hunter%20World&type=channels"]                                           
     sleep                               3

scroll
     # Execute JavaScript                  window.scrollTo(0, document.body.scrollHeight)
    Scroll Page To Location              0    10000

finduser
     clickAndWait                        xpath=//a[@href="/raaikken"]
     sleep                               5

click play video
     waitForElementPresent               xpath=//*[@class="Layout-sc-nxg1ff-0 eZactg" and text()='開始觀看']
     click                               xpath=//*[@class="Layout-sc-nxg1ff-0 eZactg" and text()='開始觀看']
     sleep                               3
     
close browser                  
     Close Browser


*** Keywords ***
open
    [Arguments]    ${element}
    Go To          ${element}

clickAndWait
    [Arguments]    ${element}
    Click Element  ${element}

click
    [Arguments]    ${element}
    Click Element  ${element}

sendKeys
    [Arguments]    ${element}    ${value}
    Press Keys     ${element}    ${value}

submit
    [Arguments]    ${element}
    Submit Form    ${element}

type
    [Arguments]    ${element}    ${value}
    Input Text     ${element}    ${value}

selectAndWait
    [Arguments]        ${element}  ${value}
    Select From List   ${element}  ${value}

select
    [Arguments]        ${element}  ${value}
    Select From List   ${element}  ${value}

verifyValue
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

verifyText
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

verifyElementPresent
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

verifyVisible
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

verifyTitle
    [Arguments]                  ${title}
    Title Should Be              ${title}

verifyTable
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

assertConfirmation
    [Arguments]                  ${value}
    Alert Should Be Present      ${value}

assertText
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

assertValue
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

assertElementPresent
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

assertVisible
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

assertTitle
    [Arguments]                  ${title}
    Title Should Be              ${title}

assertTable
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

waitForText
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

waitForValue
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

waitForElementPresent
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

waitForVisible
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

waitForTitle
    [Arguments]                  ${title}
    Title Should Be              ${title}

waitForTable
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

doubleClick
    [Arguments]           ${element}
    Double Click Element  ${element}

doubleClickAndWait
    [Arguments]           ${element}
    Double Click Element  ${element}

goBack
    Go Back

goBackAndWait
    Go Back

runScript
    [Arguments]         ${code}
    Execute Javascript  ${code}

runScriptAndWait
    [Arguments]         ${code}
    Execute Javascript  ${code}

setSpeed
    [Arguments]           ${value}
    Set Selenium Timeout  ${value}

setSpeedAndWait
    [Arguments]           ${value}
    Set Selenium Timeout  ${value}

verifyAlert
    [Arguments]              ${value}
    Alert Should Be Present  ${value}

Scroll Page To Location
    [Arguments]           ${x_location}    ${y_location}
    Execute JavaScript    window.scrollTo(${x_location},${y_location})
     