from selenium.webdriver import Chrome
#Import Pytest module to skip the specific execution using decorator
import pytest

#SKIP THE SPECIFIC TEST CASE EXECUTION
#Use below decorator annotation to skip specific test case from execution by including a note for not executig the test case
@pytest.mark.skip("This particular test case is not need at this moment")
def test_User_Registration_Validate():
    path = "C:\\Users\\saina\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()
#command 'pytest -v' will give more information in terminal about which test cases are executed and which are not

#CONDITIONALY SKIPING SPECIFIC TEST CASE EXECUTION
#Use below decorator annotation to skip specific test case from execution by placing an condition and a reason in it
a = 103
@pytest.mark.skipif(a>100, reason="Skip the below test case if a is greater than 100")
def test_User_Gmail_Validate():
    path = "C:\\Users\\saina\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.gmail.com/")
    driver.maximize_window()

@pytest.mark.skip("Running only Smoke or Sanity test cases")
def test_User_Url():
    path = "C:\\Users\\saina\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.google.com/")
    driver.close()

#HOW TO EXECUTE ANY SPECIFIC TEST CASE
#To execute specific test use in the terminal you test have to run below command
#pytest -k testcasename
#example: pytest -k test_User_Url ---> this only execute def test_User_url() function





