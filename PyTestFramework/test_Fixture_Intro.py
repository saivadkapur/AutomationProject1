#FIXTURES
#Used to execute something before the test case - setting the chrome path, maximizing the browser, connecting to the DB before
#the test case execution
#Execute after the test case - Closing DB connections, Closing the browser
#Execute only once - if you want the fixture method to execute only once while executing all the test cases then you have to
#define the scope in the fixture

from selenium.webdriver import Chrome
import pytest

#Creating Fixtures using PyTest on the top of Common Method will will get executed before each test case
#Pass the common method in the those test case where you need this fixture to get executed before executing the actual test case
#if you want to execute something after the execution of each test like closing the browser such events are to be
#written under "yield" in the fixture function

#@pytest.fixture() #This decorator will execute each time before and after each test cases
#if you want the fixture method to execute only before and after all the test cases execution then we can do it by defining the
#scope inside the fixture method
@pytest.fixture(scope="module") #This line of code will make the fixture method to execute before and after
#each test cases only once since the scope is set to the entire file. Meaning browser is gets open only once before the test cases
#are executed and will close only after all the test cases execution is completed

def set_BrowserPath():
    global driver #making driver a global a object
    path = "C:\\Users\\saina\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield #the below lines of code after yield will execute after executing the actual test case
    driver.close()

def test_userTC1_Gmail (set_BrowserPath):
    driver.get("https://www.gmail.com/")
    #Positive Assertion
    assert driver.title == "Gmail" #this line of code test the actual result meaning the title name in browser
    #while executing tjis particular test case with the title value "Gmail"

    #Negative Assertion
    #assert driver.title == "gmail" #this line of code will fail because the actual value is "Gmail" and expected value you have
    #given is "gmail"

def test_userTC1_Yahoo (set_BrowserPath):
    driver.get("https://www.yahoo.com/")
    driver.maximize_window()

def test_userTC1_Facebook (set_BrowserPath):
    driver.get("https://www.facebook.com/")
    driver.maximize_window()


#ASSERTIONS
#they are used to compare the actual result with the expected
#we use assert to make assertions in pytest
