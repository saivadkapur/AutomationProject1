from selenium.webdriver import Chrome
import pytest

#GROUP BY EXECUTION
#Step-1 use below pytest decorator '@pytest.mark.tag_name' and place it on top of the test cases on all those test cases
#you want them under one group here the group name will be the '.tag_name'
#Step-2 to execute the test cases by group name you have to use below commant in the terminal
#'pytest -m tag_name -v'
#if you want a specific group not to execute while rest other group test cases are executed you have to use below command
#'pytest -m "not tag_name" -v' ---> this command will not execute the 'not tag_name' group and rest everything will be executed

#@pytest.mark.Smoke
#def test_userTC1_Gmail ():
    #path = "C:\\Users\\saina\\Downloads\\chromedriver_win32\\chromedriver.exe"
    #driver = Chrome(executable_path=path)
    #driver.get("https://www.gmail.com/")
    #driver.close()

#@pytest.mark.Sanity
#def test_userTC1_Yahoo ():
    #path = "C:\\Users\\saina\\Downloads\\chromedriver_win32\\chromedriver.exe"
    #driver = Chrome(executable_path=path)
    #driver.get("https://www.yahoo.com/")
    #driver.maximize_window()
    #driver.close()

#@pytest.mark.Smoke
#def test_userTC1_Facebook ():
    #path = "C:\\Users\\saina\\Downloads\\chromedriver_win32\\chromedriver.exe"
    #driver = Chrome(executable_path=path)
    #driver.get("https://www.facebook.com/")
    #driver.maximize_window()