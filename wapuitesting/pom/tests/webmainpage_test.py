import pytest
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import string
from pom.pages.Login_Page import LoginPage


global pocouimainpage


#setup variables
pagelogo = (By.XPATH, "*//div[@class='entry-design design-image mr-auto flex-grow-0 flex-shrink-0']/figure[@class='figure']/a[contains(@href,'https://ecommerce-playground.lambdatest.io') and (@title='Poco Theme')]/img[contains(@src,'https://ecommerce-playground.lambdatest.io/image/catalog/maza/svg/logo3.svg')]")
searchbutton = (By.XPATH, "//*[@id='search']/div[2]/button/i")
#searchinput = (By.XPATH, "//*[@id='search']/div[1]/div[1]/div[2]/input")
searchinput = (By.XPATH, "//html/body/div[1]/div[5]/header/div[3]/div[2]/div/div/form/div/div[1]/div[1]/div[2]/input")
#searchinput = (By.CSS_SELECTOR, "#search > div.search-input-group.flex-fill > div.search-input.d-flex > div.flex-fill > input[type=text]")
searchinput = (By.XPATH, "//html/body/div[1]/div[5]//*[@id='search']/div[1]/div[1]/div[2]/input")
productname= "HTC Touch HD"
# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
metrics = ""
@pytest.fixture()

def Driver():
    # Set device name to emulate

    device_name = "iPhone X"
    """device_name = {
       "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
       "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.118 Mobile Safari/537.361",
       "clientHints": {"platform": "Android", "mobile": True} }"""
    #chrome_options.add_argument("--window-size=360,640")
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": device_name})

    # Setup WebDriver
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    metrics = driver.execute_cdp_cmd('Page.getLayoutMetrics', {})

    # Print device metrics in this setup
    chrome_options.add_argument("--window-size=" + str((metrics['layoutViewport']['clientWidth'])-1000) + "," + str(metrics['layoutViewport']['clientHeight']))
    #driver.get('https://ecommerce-playground.lambdatest.io/')
    #driver.quit()

    yield driver

def test_if_browser_open_in_mobile_mode(Driver):
    try:
        #Driver.get('https://ecommerce-playground.lambdatest.io/')
        metrics = Driver.execute_cdp_cmd('Page.getLayoutMetrics', {})
        chrome_options.add_argument(
            "--window-size=" + str((metrics['layoutViewport']['clientWidth']) - 1000) + "," + str(
                metrics['layoutViewport']['clientHeight']))
        print(f"Width: {metrics['layoutViewport']['clientWidth']}, Height: {metrics['layoutViewport']['clientHeight']}")
        Driver.get('https://ecommerce-playground.lambdatest.io/')
        # =========== NOTES: browser sizes (in pixel) ===============
        # Desktop : 1920 x 1080 px and 1024 x 768 px      => width > height
        # Mobile : 375 x 667px , 414 x 896px, 360 x 640px  => width < height
        # ============================================================
        #print(f"Width: {metrics['layoutViewport']['clientWidth']}, Height: {metrics['layoutViewport']['clientHeight']}")
        assert ({metrics['layoutViewport']['clientWidth']}) < {metrics['layoutViewport']['clientHeight']}, logging.info("web application is not running is a mobile screen size, Please verify manually.")
        time.sleep(10)
        Driver.close()
        #Driver.quit()
    except AssertionError as ex:
        print(f"An error occurred: {ex}")
    Driver.quit()


#testcase: Verify User Registration for new user
#          Verify that a new user can successfully register by providing valid details.
def test_User_Registration_test(Driver):
    try:
        Driver.get('https://ecommerce-playground.lambdatest.io/')
        pocouimainpage = LoginPage(Driver)
        #productsearchpage.user_registration(Driver)
        assert pocouimainpage.user_registration(Driver), logging.info("The user was not able to perform user registration, Please verify manually.")
        Driver.close()
        Driver.quit()
    except AssertionError as ex:
        print(f"An error occurred: {ex}")



#testcase: Validate that users can login with proper user credentials.
def test_LoginUser_with_proper_user_credential_test(Driver):
    try:
        username = "enuser.usertester007@gmail.com"
        password = "T3$TUS3R147"
        Driver.get('https://ecommerce-playground.lambdatest.io/')
        pocouimainpage = LoginPage(Driver)
        assert pocouimainpage.user_login(Driver, username, password), logging.info("The user was not able to perform user Login, Please verify manually.")
        Driver.close()
        Driver.quit()
    except AssertionError as ex:
        print(f"An error occurred: {ex}")


#testcase: Verify that registered user can perform Complete Checkout Process
#  cover features /functionalities:  Login user, search user, add to cart, checkout
def test_Verify_that_registered_user_can_perform_Complete_Checkout_Process(Driver):
    try:
        username = "enuser.usertester007@gmail.com"
        password = "T3$TUS3R147"
        productname = "HTC Touch HD"
        Driver.get('https://ecommerce-playground.lambdatest.io/')
        pocouimainpage = LoginPage(Driver)
        pocouimainpage.user_login(Driver, username, password)
        ###assert productsearchpage.useraddtocart(Driver, productname), logging.info("The user was not able to perform Checkout, Please verify manually.")###
        assert pocouimainpage.checkoutpage(Driver, productname), logging.info("The user was not able to perform Checkout, Please verify manually.")
        Driver.close()

    except AssertionError as ex:
        print(f"An error occurred: {ex}")
    Driver.quit()

def test_handling_popup_notification(Driver):
    try:
        username = "enuser.usertester007@gmail.com"
        password = "T3$TUS3R147"
        productname = "HTC Touch HD"
        Driver.get('https://ecommerce-playground.lambdatest.io/')
        pocouimainpage = LoginPage(Driver)
        pocouimainpage.user_login(Driver, username, password)
        #this assert test if the multiple pop-up notification appears and flag 'false' using assert not.
        assert not pocouimainpage.Verify_popup_notification(Driver, productname), logging.info("The multi popup notification appears. Report to confirm if this is an issue")
        time.sleep(8)
        Driver.close()
        Driver.quit()
    except AssertionError as ex:
        print(f"An error occurred: {ex}")


def test_transactionpage_is_avalable_for_guessUser(Driver):
        try:
            productname = "HTC Touch HD"
            Driver.get('https://ecommerce-playground.lambdatest.io/')
            pocouimainpage = LoginPage(Driver)

            time.sleep(3)
            current_url = Driver.current_url
            # this verify if a guest user can redirect to '... ?route=account/order' even if he is not register
            #if current URL does not contain '... ?route=account/order', it means he cannot access
            # the transaction history which is correct. Validation "assert not" will mark as 'PASS'

            assert pocouimainpage.IS_transactionhuistory_available(Driver) != current_url, logging.info(
                "Guess user should not be able to access order history page")
            #print (pocouimainpage.IS_transactionhuistory_available(Driver))
            #print(current_url)
            Driver.close()

        except AssertionError as ex:
            print(f"An error occurred: {ex}")

        Driver.quit()

# Close the driver
#Driver.quit()
