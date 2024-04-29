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

# ====  variable declaration ====
global_Validation_result = True
ISPOPUPNOTIF_TRIGGERED = True
orderhistory_URL = ""

pagelogo = (By.XPATH,"*//div[@class='entry-design design-image mr-auto flex-grow-0 flex-shrink-0']/figure[@class='figure']/a[contains(@href,'https://ecommerce-playground.lambdatest.io') and (@title='Poco Theme')]/img[contains(@src,'https://ecommerce-playground.lambdatest.io/image/catalog/maza/svg/logo3.svg')]")
searchbutton = (By.XPATH, "//*[@id='search']/div[2]/button/i")
searchinput = (By.XPATH, "//html/body/div[1]/div[5]/header/div[3]/div[2]/div/div/form/div/div[1]/div[1]/div[2]/input")
productname = "HTC Touch HD"
user_cog_iconstr = "/html/body/div[1]/div[5]/header/div[2]/div[2]/div[3]/a/i"
quicklink_headerstr = "*//div/h5[contains(@class,'text-primary-inverse') and (text()='Quick Links ')]"
myaccount_linkstr = "*//div[contains(@class,'widget-navbar pixel-space gutters-x-off flex-grow-0')]/nav[contains(@class,'navbar-default bg-default vertical')]//li[4]"


class LoginPage:
#class ProductSearchPage:
    global orderhistory_URL
    def __init__(self, Driver:webdriver):  # check this later if webdriver or Webdriver
        self.driver = Driver
        Driver.implicitly_wait(10)

    def user_registration(self,Driver):
        global global_Validation_result
        try:
            # ======= Quick Links modal ===========
            registration_headerstr = "//*[@id='account-login']//h2[text()='New Customer']"
            registration_continuebtnstr = "//*[@id='account-login']//div[@class='card-body p-4']//a[(@class='btn btn-primary') and (text()='Continue')]"

            # =========Registration page ==============
            register_headerstr = "//*[@id='account-register']//h1[text()='Register Account']"
            register_Fnamestr = "//*[@id='account-register']//div[@class='col-sm-10']/input[(@type='text') and (@name='firstname')]"
            register_Lnamestr = "//*[@id='account-register']//div[@class='col-sm-10']/input[(@type='text') and (@name='lastname')]"
            register_Emailstr = "//*[@id='account-register']//div[@class='col-sm-10']/input[(@type='email') and (@name='email')]"
            register_Telstr = "//*[@id='account-register']//div[@class='col-sm-10']/input[(@type='tel') and (@name='telephone')]"
            register_Pwdstr = "//*[@id='account-register']//div[@class='col-sm-10']/input[(@type='password') and (@name='password')]"
            register_Pwd2str = "//*[@id='account-register']//div[@class='col-sm-10']/input[(@type='password') and (@name='confirm')]"
            # register_chkpolicystr = "//*[@id='account-register']//div[@class='buttons clearfix']//input[@type='checkbox']"
            register_chkpolicystr = "#content > form > div > div > div > label"
            register_submitbtnstr = "//*[@id='account-register']//div[@class='buttons clearfix']//input[@type='submit']"

            username_length = 5
            characters = string.ascii_letters + string.digits
            username = ''.join(random.choice(characters) for i in range(username_length))
            newuserename = "dummytest" + username + "@gmail.com"

            time.sleep(10)
            WebDriverWait(Driver, 10).until(EC.presence_of_element_located(pagelogo))
            WebDriverWait(Driver, 10).until(EC.presence_of_element_located(searchbutton))
            productIsearchinput = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(searchinput))
            user_cog_icon = WebDriverWait(Driver, 10).until(EC.element_to_be_clickable((By.XPATH, user_cog_iconstr)))
            user_cog_icon.click()

            # ======= Quick Links modal ===========
            time.sleep(5)
            quicklink_header = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, quicklink_headerstr)))
            registration_header = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, myaccount_linkstr)))
            registration_header.click()
            time.sleep(5)
            registration_continuebtn = WebDriverWait(Driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, registration_continuebtnstr)))
            registration_continuebtn.click()

            time.sleep(5)

            # =========Registration page ==============
            register_header = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_headerstr)))
            register_Fname = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Fnamestr)))
            register_Lname = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Lnamestr)))
            register_Email = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Emailstr)))
            register_Tel = WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, register_Telstr)))
            register_Pwd = WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, register_Pwdstr)))
            register_Pwd2 = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Pwd2str)))
            register_chkpolicy = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, register_chkpolicystr)))
            register_submitbtn = WebDriverWait(Driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, register_submitbtnstr)))

            register_Fname.send_keys("dummy Fname")
            register_Fname.send_keys(Keys.TAB)
            register_Lname.send_keys("dummy Lname")
            register_Lname.send_keys(Keys.TAB)
            register_Email.send_keys(newuserename)
            register_Email.send_keys(Keys.TAB)
            register_Tel.send_keys("886971434437")
            register_Tel.send_keys(Keys.TAB)
            register_Pwd.send_keys("T3st!ngPWD")
            register_Pwd.send_keys(Keys.TAB)
            register_Pwd2.send_keys("T3st!ngPWD")
            register_Pwd2.send_keys(Keys.TAB)
            register_chkpolicy.click()
            Driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(2)
            # input text validation after user input. should not empty
            is_Fname_notempty = len(WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Fnamestr))).get_attribute("value")) > 0
            is_Lname_notempty = len(WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Lnamestr))).get_attribute("value")) > 0
            is_Email_notempty = len(WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Emailstr))).get_attribute("value")) > 0
            is_Tel_notempty = len(WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Telstr))).get_attribute("value")) > 0
            is_Pwd_notempty = len(WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Pwdstr))).get_attribute("value")) > 0
            is_Pwd2_notempty = len(WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, register_Pwd2str))).get_attribute("value")) > 0

            # this will reverify that the check policy instance. however in this UI, the element checkbox policy does not have attribute = 'checked'. will skip for now
            is_chkpolicy = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, register_chkpolicystr))).is_selected()

            testinput_boolcount = [is_Fname_notempty, is_Lname_notempty, is_Email_notempty, is_Tel_notempty,
                                   is_Pwd_notempty, is_Pwd2_notempty]

            # check if the value is not an empty string
            if testinput_boolcount.count(True) == 6:
                register_submitbtn.click()
                Driver.execute_script("window.scrollBy(0, 0);")
                # Success page validation. check if URL contains ?route=account/success
                time.sleep(10)
                current_url = Driver.current_url
                if "?route=account/success" in current_url:

                    regis_successiconstr = "//*[@id='content']/h1/i"
                    regis_successheaderstr = "//*[@id='content']/h1"
                    regis_sucsssubhrdstr1 = "//*[@id='content']/p[2]"
                    regis_successsubhrdstr2 = "//*[@id='content']/p[3]"
                    regis_successsubhrdstr3 = "//*[@id='content']/p[4]"
                    regis_successsubhrdstr4 = "//*[@id='content']/p[5]"
                    regis_successcontinuestr = "//*[@id='content']/div/a[(@class='btn btn-primary') and (text()='Continue')]"

                    regis_successheadertxt = "Your Account Has Been Created!"
                    regis_successsubhrdtxt1 = "Congratulations! Your new account has been successfully created!"
                    regis_successsubhrdtxt2 = "You can now take advantage of member privileges to enhance your online shopping experience with us."
                    regis_successsubhrdtxt3 = "If you have ANY questions about the operation of this online shop, please e-mail the store owner."
                    regis_successsubhrdtxt4 = "A confirmation has been sent to the provided e-mail address. If you have not received it within the hour, please\ncontact us\n."

                    reg_successicon = ("fas fa-check-circle text-success" in WebDriverWait(Driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, regis_successiconstr))).get_attribute("class"))
                    reg_successheader = WebDriverWait(Driver, 10).until(
                        EC.text_to_be_present_in_element((By.XPATH, regis_successheaderstr),
                                                         "Your Account Has Been Created!"))
                    reg_successsubhrd1 = WebDriverWait(Driver, 10).until(
                        EC.text_to_be_present_in_element((By.XPATH, regis_sucsssubhrdstr1), regis_successsubhrdtxt1))
                    reg_successsubhrd2 = WebDriverWait(Driver, 10).until(
                        EC.text_to_be_present_in_element((By.XPATH, regis_successsubhrdstr2), regis_successsubhrdtxt2))
                    reg_successsubhrd3 = WebDriverWait(Driver, 10).until(
                        EC.text_to_be_present_in_element((By.XPATH, regis_successsubhrdstr3), regis_successsubhrdtxt3))
                    reg_successsubhrd4 = WebDriverWait(Driver, 10).until(
                        EC.text_to_be_present_in_element((By.XPATH, regis_successsubhrdstr4), regis_successsubhrdtxt4))

                    reg_successcontinue = WebDriverWait(Driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, regis_successcontinuestr)))

                    # parsing structured validation
                    successmessage_boolcount = [reg_successicon, reg_successheader, reg_successsubhrd1,
                                                reg_successsubhrd2, reg_successsubhrd3,
                                                reg_successsubhrd4]  # count of all success message that match.
                    # check if the value is not an empty string
                    if successmessage_boolcount.count(True) == 6:
                        #print("success message was sent successfully.")
                        reg_successcontinue.click()

                        time.sleep(10)
                        current_url = Driver.current_url
                        if "?route=account/account" in current_url:
                            user_myaccountstr = "//*[@id='content']/div[1]/h2"
                            user_edituserstr = "//*[@id='content']/div[1]/div/div/div[1]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/edit')]"
                            user_passworduserstr = "//*[@id='content']/div[1]/div/div/div[2]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/password')]"
                            user_editaddressbookstr = "//*[@id='content']/div[1]/div/div/div[3]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/address')]"
                            user_editwishliststr = "//*[@id='content']/div[1]/div/div/div[4]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/wishlist')]"
                            user_usersubscriptionstr = "//*[@id='content']/div[1]/div/div/div[5]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/newsletter')]"

                            user_myaccountpage = WebDriverWait(Driver, 10).until(
                                EC.text_to_be_present_in_element((By.XPATH, user_myaccountstr), "My Account"))
                            time.sleep(5)
                            """user_edituser = Driver.find_element(By.XPATH, user_edituserstr).text
                            user_passworduser = Driver.find_element(By.XPATH, user_passworduserstr).text
                            user_editaddressbook = Driver.find_element(By.XPATH, user_editaddressbookstr).text
                            user_editwishlist = Driver.find_element(By.XPATH, user_editwishliststr).text
                            user_usersubscription = Driver.find_element(By.XPATH, user_usersubscriptionstr).text"""
                            Driver.execute_script("window.scrollBy(0, -200);")
                            time.sleep(2)
                            #time.sleep(10)
                            user_edituser = WebDriverWait(Driver, 10).until(
                                EC.text_to_be_present_in_element((By.XPATH, user_edituserstr),
                                                                 "Edit your account information"))
                            user_passworduser = WebDriverWait(Driver, 10).until(
                                EC.text_to_be_present_in_element((By.XPATH, user_passworduserstr),
                                                                 "Change your password"))
                            user_editaddressbook = WebDriverWait(Driver, 10).until(
                                EC.text_to_be_present_in_element((By.XPATH, user_editaddressbookstr),
                                                                 "Modify your address book entries"))
                            user_editwishlist = WebDriverWait(Driver, 10).until(
                                EC.text_to_be_present_in_element((By.XPATH, user_editwishliststr),
                                                                 "Modify your wish list"))
                            user_usersubscription = WebDriverWait(Driver, 10).until(
                                EC.text_to_be_present_in_element((By.XPATH, user_usersubscriptionstr),
                                                                 "Subscribe / unsubscribe to newsletter"))
                            myaccountelements_boolcount = [user_edituser, user_passworduser, user_editaddressbook,
                                                        user_editwishlist, user_usersubscription]  # count of all important element of my account page.
                            if myaccountelements_boolcount.count(True) == 5:
                                #print("user 'My account' is successfully loaded after user registration.")
                                global_Validation_result = True
                            else:
                                print("user's 'My account' page does not show after successful user registration.")
                                global_Validation_result = False
                        else:
                            print("Success page did not load properly.")
                            #global_Validation_result = False

                    else:
                        print("Success page did not load properly.")
                        #global_Validation_result = False
                else:
                    print("Success page did not load properly.")
                    #global_Validation_result = False
            else:
                #print("Some input fields are empty.")
                global_Validation_result = False
        except Exception as ex:
            print(f"An error occurred: {ex}")
            #global_Validation_result = False

        return global_Validation_result

    def user_login(self,Driver,username,password):
        global global_Validation_result
        try:
            #Driver.get('https://ecommerce-playground.lambdatest.io/')
            # ======= Quick Links modal ===========
            time.sleep(10)
            WebDriverWait(Driver, 20).until(EC.presence_of_element_located(pagelogo))
            WebDriverWait(Driver, 20).until(EC.presence_of_element_located(searchbutton))
            productIsearchinput = WebDriverWait(Driver, 20).until(EC.presence_of_element_located(searchinput))
            user_cog_icon = WebDriverWait(Driver, 20).until(EC.element_to_be_clickable((By.XPATH, user_cog_iconstr)))
            user_cog_icon.click()

            # ======= Quick Links modal ===========
            time.sleep(10)
            quicklink_header = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((By.XPATH, quicklink_headerstr)))
            registration_header = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((By.XPATH, myaccount_linkstr)))
            registration_header.click()
            time.sleep(10)

            # =========Login page ==============

            userlogin_headerstr = "//*[@id='content']/div/div[2]/div/div/h2"
            userlogin_subheaderstr = "//*[@id='content']/div/div[2]/div/div/p/strong"
            userlogin_emailinputstr = "*//input[(@id='input-email') and (@type='text')]"
            userlogin_passwordinputstr = "*//input[(@id='input-password') and (@type='password')]"
            userlogin_forgotstr = "//*[@id='content']/div/div[2]/div/div/form/div[2]/a"
            userlogin_loginbtnstr = "//*[@id='content']/div/div[2]/div/div/form/input[(@type='submit') and (@class='btn btn-primary')]"

            register_Fnamestr = "//*[@id='account-register']//div[@class='col-sm-10']/input[(@type='text') and (@name='firstname')]"

            current_url = Driver.current_url
            if "?route=account/login" in current_url:
                # user_edituserstr = "//*[@id='content']/div[1]/div/div/div[1]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/edit')]"

                # userlogin_header = Driver.find_element(By.XPATH, userlogin_headerstr).text
                # userlogin_subheader = Driver.find_element(By.XPATH, userlogin_subheaderstr).text
                # userlogin_forgot = Driver.find_element(By.XPATH, userlogin_forgotstr).text

                userlogin_header = WebDriverWait(Driver, 20).until(
                    EC.text_to_be_present_in_element((By.XPATH, userlogin_headerstr), "Returning Customer"))
                userlogin_subheader = WebDriverWait(Driver, 20).until(
                    EC.text_to_be_present_in_element((By.XPATH, userlogin_subheaderstr), "I am a returning customer"))
                userlogin_forgot = WebDriverWait(Driver, 20).until(
                    EC.text_to_be_present_in_element((By.XPATH, userlogin_forgotstr), "Forgotten Password"))

                userlogin_emailinput = WebDriverWait(Driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, userlogin_emailinputstr)))
                userlogin_passwordinput = WebDriverWait(Driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, userlogin_passwordinputstr)))
                userlogin_loginbtn = WebDriverWait(Driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, userlogin_loginbtnstr)))

                userlogin_emailinput.send_keys(username)
                userlogin_emailinput.send_keys(Keys.TAB)
                userlogin_passwordinput.send_keys(password)
                userlogin_passwordinput.send_keys(Keys.TAB)
                Driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
                time.sleep(2)
                Driver.execute_script("window.scrollBy(0, 10);")
                # Verify if userlogin inputs are not empty
                is_username_notempty = len(WebDriverWait(Driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, userlogin_emailinputstr))).get_attribute("value")) > 0
                is_userpwd_notempty = len(WebDriverWait(Driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, userlogin_passwordinputstr))).get_attribute("value")) > 0

                logininput_boolcount = [is_username_notempty, is_userpwd_notempty]

                # check if the value is not an empty string
                if logininput_boolcount.count(True) == 2:
                    #print("login Input text field is not empty.")
                    userlogin_loginbtn.click()

                    # Success page validation. check if URL contains ?route=account/success
                    time.sleep(10)
                    current_url = Driver.current_url
                    if "?route=account/account" in current_url:
                        user_myaccountstr = "//*[@id='content']/div[1]/h2"
                        user_edituserstr = "//*[@id='content']/div[1]/div/div/div[1]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/edit')]"
                        user_passworduserstr = "//*[@id='content']/div[1]/div/div/div[2]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/password')]"
                        user_editaddressbookstr = "//*[@id='content']/div[1]/div/div/div[3]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/address')]"
                        user_editwishliststr = "//*[@id='content']/div[1]/div/div/div[4]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/wishlist')]"
                        user_usersubscriptionstr = "//*[@id='content']/div[1]/div/div/div[5]/a[contains(@href,'https://ecommerce-playground.lambdatest.io/index.php?route=account/newsletter')]"

                        user_myaccountpage = WebDriverWait(Driver, 10).until(
                            EC.text_to_be_present_in_element((By.XPATH, user_myaccountstr), "My Account"))
                        time.sleep(5)
                        """user_edituser = Driver.find_element(By.XPATH, user_edituserstr).text
                        user_passworduser = Driver.find_element(By.XPATH, user_passworduserstr).text
                        user_editaddressbook = Driver.find_element(By.XPATH, user_editaddressbookstr).text
                        user_editwishlist = Driver.find_element(By.XPATH, user_editwishliststr).text
                        user_usersubscription = Driver.find_element(By.XPATH, user_usersubscriptionstr).text"""
                        Driver.execute_script("window.scrollBy(0, 700);")
                        time.sleep(2)
                        # time.sleep(10)
                        user_edituser = WebDriverWait(Driver, 10).until(
                            EC.text_to_be_present_in_element((By.XPATH, user_edituserstr),
                                                             "Edit your account information"))
                        user_passworduser = WebDriverWait(Driver, 10).until(
                            EC.text_to_be_present_in_element((By.XPATH, user_passworduserstr),
                                                             "Change your password"))
                        user_editaddressbook = WebDriverWait(Driver, 10).until(
                            EC.text_to_be_present_in_element((By.XPATH, user_editaddressbookstr),
                                                             "Modify your address book entries"))
                        user_editwishlist = WebDriverWait(Driver, 10).until(
                            EC.text_to_be_present_in_element((By.XPATH, user_editwishliststr),
                                                             "Modify your wish list"))
                        user_usersubscription = WebDriverWait(Driver, 10).until(
                            EC.text_to_be_present_in_element((By.XPATH, user_usersubscriptionstr),
                                                             "Subscribe / unsubscribe to newsletter"))
                        myaccountelements_boolcount = [user_edituser, user_passworduser, user_editaddressbook,
                                                       user_editwishlist,
                                                       user_usersubscription]  # count of all important element of my account page.
                        if myaccountelements_boolcount.count(True) == 5:
                            #print("user 'My account' is successfully loaded after Login.")
                            global_Validation_result = True
                        else:
                            print("user's 'My account' page does not show after successful user Login.")
                            global_Validation_result = False
                    else:
                        print("Login page did not load properly.")
            else:
                print("Login page did not load properly.")


        except Exception as ex:
            print(f"An error occurred: {ex}")

        return global_Validation_result


    def useraddtocart(self, Driver, productname):
        global global_Validation_result
        try:
            time.sleep(10)
            # ======= Main ecommerce main page ===========
            WebDriverWait(Driver, 20).until(EC.presence_of_element_located(pagelogo))
            WebDriverWait(Driver, 20).until(EC.presence_of_element_located(searchbutton))
            productIsearchinput = WebDriverWait(Driver, 20).until(EC.presence_of_element_located(searchinput))
            user_cog_icon = WebDriverWait(Driver, 20).until(EC.element_to_be_clickable((By.XPATH, user_cog_iconstr)))

            # ===== Search product ======
            productIsearchinput.send_keys(productname)
            productIsearchinput.send_keys(Keys.ENTER)

            resultlabel = WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='entry_212456']/h1"))).text
            selected_productstr = "*//div[contains(@class,'entry-content content-products order')]/div/div[1]/div/div[2]/h4/a[contains(@href,'&search=HTC+Touch+HD')]"
            assert productname in resultlabel

            # ==== handling screen view limitation ===
            # Scroll down using execute_script method
            Driver.execute_script("window.scrollBy(0, 100);")

            selected_product = WebDriverWait(Driver, 20).until(EC.presence_of_element_located((By.XPATH, selected_productstr)))
            selected_product.click()
            time.sleep(6)

            product_headerstr = "//*[@class='entry-content content-breadcrumbs ']/nav/ol/li[@class='breadcrumb-item active']"  # HTC Touch HD
            product_addtocartstr = "//*[@class='entry-content content-button d-md-none d-lg-block']/button[contains(@type,'button')and (@title='Add to Cart')]" #Add to Cart


            #product_header = Driver.find_element(By.XPATH, product_headerstr).text
            #product_addtocarttxt = Driver.find_element(By.XPATH, product_addtocartstr).text
            product_header = WebDriverWait(Driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, product_headerstr), "HTC Touch HD"))
            product_addtocarttxt = WebDriverWait(Driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, product_addtocartstr), "ADD TO CART"))
            product_addtocartbtn = WebDriverWait(Driver, 10).until(EC.element_to_be_clickable((By.XPATH, product_addtocartstr)))
            Driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(2)
            Driver.execute_script("window.scrollBy(0, 10);")
            elementpresend_count = [product_header,product_addtocarttxt]
            if elementpresend_count.count(True) == 2:
                product_addtocartbtn.click()

                #==== multiple notif ======
                #multiple_notifstr = "//*[@id='notification-box-top']/div[1]/div[1]"
                multiple_notif_arraystr = "//*[@id='notification-box-top']/div"
                #viewcartstr = "//*[@id='notification-box-top']/div/div[2]/div[2]/div[1]/a/i"
                viewcartstr = "//*[@id='notification-box-top']/div/div[2]/div[2]/div[1]/a[contains(@class,'btn btn-primary btn-block') and contains(@href,'?route=checkout/cart')]"


                checkmultiple_notif = Driver.find_elements(By.XPATH, viewcartstr)
                checkmultiple_notif_count = len(checkmultiple_notif)

                viewcarttxt = WebDriverWait(Driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, viewcartstr), "View Cart"))
                viewcartbtn = WebDriverWait(Driver, 10).until(EC.element_to_be_clickable((By.XPATH, viewcartstr)))

                if (checkmultiple_notif_count < 2) and (viewcarttxt == True):
                    print(f'Total count of elements notif popup: {checkmultiple_notif_count}')
                    viewcartbtn.click()
                else:
                    print(f'Multiple notif triggered. Total count of elements: {checkmultiple_notif_count}')

            # ======= Cart page =======
                #time.sleep(6)

            else:
                print("Product not found. product page does not load properly")
                global_Validation_result = False

        except Exception as ex:
            print(f"An error occurred: {ex}")

    def checkoutpage(self, Driver, productname):
        global global_Validation_result
        try:
            self.useraddtocart(Driver, productname)

            # ======= Cart page =======
            time.sleep(6)
            current_url = Driver.current_url
            if "?route=checkout/cart" in current_url:
                editcarttablestr ="//*[@id='content']/form[contains(@action,'?route=checkout/cart')]/div/table/tbody"
                user_cart_headertagstr = "//*[@id='checkout-cart']/nav/ol/li[@class='breadcrumb-item active']"
                user_cart_headerstr = "//*[@id='content']/h1[@class='page-title mb-3 h4']"
                user_checkoutbtnstr = "//*[@id='content']/div[2]/a[contains(@href,'?route=checkout/checkout')]"

                user_checkoutbtn = WebDriverWait(Driver, 5).until(EC.element_to_be_clickable((By.XPATH, user_checkoutbtnstr)))
                editcarttable = Driver.find_element(By.XPATH, editcarttablestr)
                #Get all rows
                cartitems_row = editcarttable.find_elements(By.TAG_NAME, 'tr')
                cartitems_row1 = editcarttable.find_elements(By.TAG_NAME, 'tr')
                cartitems_row_count = len(cartitems_row)
                #print(f'Number of rows: {cartitems_row_count}')
                #print(f'Number of rows: {cartitems_row_count}')
                user_cart_headertag = WebDriverWait(Driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, user_cart_headertagstr), "Shopping Cart"))
                user_cart_header = WebDriverWait(Driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, user_cart_headerstr), "Shopping Cart"))
                # Parse the table
                #for i in enumerate(cartitems_row):
                array_counter = 0
                for i in cartitems_row:

                    editcarttabletd = Driver.find_elements(By.XPATH, editcarttablestr+'/tr/td[2]')
                    productname1 = editcarttabletd[array_counter].text  # assuming the phone name is in the 2nd column
                    #if 'HTC Touch HD' in productname1:
                    if productname in productname1:
                    # ========= order row cell element validation ===========
                        product_image_incart = WebDriverWait(Driver, 10).until(EC.text_to_be_present_in_element_attribute((By.XPATH, editcarttablestr+"/tr/td[1]/a/img"), "title", productname))
                        product_name_incart = WebDriverWait(Driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, editcarttablestr+"/tr/td[2]"), productname))
                        product_model_incart = WebDriverWait(Driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, editcarttablestr+"/tr/td[3]"), "Product 1"))
                        product_quantity_incart = len(WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, editcarttablestr+"/tr/td[4]/div/input"))).get_attribute("value")) > 0
                        product_unitprice_incart = WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, editcarttablestr+"/tr/td[5]"))).text != 0
                        product_totalprice_incart = WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, editcarttablestr+"/tr/td[6]"))).text != 0

                    # ======= count how many expected element matched = True =======
                    cartelement_boolcount = [product_image_incart,product_name_incart, product_model_incart, product_quantity_incart,product_unitprice_incart,product_totalprice_incart]
                    Driver.execute_script("window.scrollBy(0, 700);")
                    time.sleep(2)
                    # check if all expected element in cart is not empty
                    if cartelement_boolcount.count(True) == 6:
                        user_checkoutbtn.click()
                        time.sleep(6)
                        Checkout_pagestr = "//*[@id='maza-checkout']/nav/ol/li[3]"
                        checkout_userTelstr = "//*[@id='account-edit']/h4"
                        checkout_billingaddrstr = "//*[@id='payment-address']/h4"
                        checkout_paymentmethodCODstr = "//*[@id='payment-method']/div/label"
                        checkout_shippingstr = "//*[@id='shipping-method']/div/label"
                        checkout_couponstr = "//*[@id='accordion']/div[1]/h5"
                        checkout_policystr = "#input-account-agree"
                        checkout_Termconditionstr = "#form-checkout > div.row > div.col-lg-7.mb-5.mb-lg-0 > div > div:nth-child(6) > label"

                        checkout_submitbtnstr = "//*[@id='button-save']"
                        Driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
                        time.sleep(2)
                        Driver.execute_script("window.scrollBy(0, 10);")


                        #note. In this demo, I only covers some important part of a checkout page (page titles/header only) to amke it quick
                        Checkout_page_tag = ("Checkout" in WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, Checkout_pagestr))).text)
                        checkout_userTel = ("Telephone" in WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, checkout_userTelstr))).text)
                        checkout_billingaddr = ("Billing Address" in WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, checkout_billingaddrstr))).text)
                        checkout_paymentmethodCOD = ("Cash On Delivery" in WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, checkout_paymentmethodCODstr))).text)
                        checkout_shipping = ("Flat Shipping Rate - $8.00" in WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, checkout_shippingstr))).text)
                        checkout_coupon = ("Use Coupon Code" in WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, checkout_couponstr))).text)
                        checkout_policy = WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, checkout_policystr)))
                        checkout_Termcondition = WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, checkout_Termconditionstr)))
                        checkout_submitbtn = WebDriverWait(Driver, 5).until(EC.element_to_be_clickable((By.XPATH, checkout_submitbtnstr)))
                        checkout_commentsecstr = WebDriverWait(Driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='input-comment']")))
                        Driver.execute_script("window.scrollBy(0, 700);")
                        time.sleep(2)
                        checkoutelement_boolcount = [Checkout_page_tag,checkout_userTel,checkout_billingaddr,checkout_paymentmethodCOD, checkout_shipping, checkout_coupon, checkout_policy,checkout_Termcondition,checkout_submitbtn]


                        current_url = Driver.current_url
                        if ("?route=checkout/checkout" in current_url) and (checkoutelement_boolcount.count(True) == 6):
                            print("checkout page loads properly")
                            #checkout_policy.click()
                            checkout_commentsecstr.click()
                            checkout_commentsecstr.send_keys(Keys.TAB)
                            checkout_Termcondition.click()
                            #checkout_submitbtn.click()
                            global_Validation_result = True


                        else:
                            print("checkout page is not loading properly")
                        break

                    else:
                        print("HTC Touch HD not found")
                    array_counter = array_counter + 1

        except Exception as ex:
                print(f"An error occurred: {ex}")
                global_Validation_result = False
        return global_Validation_result
    def Verify_popup_notification(self, Driver, productname):
        global ISPOPUPNOTIF_TRIGGERED
        try:
            time.sleep(10)
            # ======= Main ecommerce main page ===========
            WebDriverWait(Driver, 20).until(EC.presence_of_element_located(pagelogo))
            WebDriverWait(Driver, 20).until(EC.presence_of_element_located(searchbutton))
            productIsearchinput = WebDriverWait(Driver, 20).until(EC.presence_of_element_located(searchinput))
            user_cog_icon = WebDriverWait(Driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, user_cog_iconstr)))

            # ===== Search product ======
            productIsearchinput.send_keys(productname)
            productIsearchinput.send_keys(Keys.ENTER)

            resultlabel = WebDriverWait(Driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='entry_212456']/h1"))).text
            selected_productstr = "*//div[contains(@class,'entry-content content-products order')]/div/div[1]/div/div[2]/h4/a[contains(@href,'&search=HTC+Touch+HD')]"
            assert productname in resultlabel

            # ==== handling screen view limitation ===
            # Scroll down using execute_script method
            Driver.execute_script("window.scrollBy(0, 100);")

            selected_product = WebDriverWait(Driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, selected_productstr)))
            selected_product.click()
            time.sleep(6)

            product_headerstr = "//*[@class='entry-content content-breadcrumbs ']/nav/ol/li[@class='breadcrumb-item active']"  # HTC Touch HD
            product_addtocartstr = "//*[@class='entry-content content-button d-md-none d-lg-block']/button[contains(@type,'button')and (@title='Add to Cart')]"  # Add to Cart

            product_header = WebDriverWait(Driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, product_headerstr), "HTC Touch HD"))
            product_addtocarttxt = WebDriverWait(Driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, product_addtocartstr), "ADD TO CART"))
            product_addtocartbtn = WebDriverWait(Driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, product_addtocartstr)))
            Driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            elementpresend_count = [product_header, product_addtocarttxt]
            if elementpresend_count.count(True) == 2:
                # === trigger multiple notification ===
                product_addtocartbtn.click()
                product_addtocartbtn.click()
                product_addtocartbtn.click()
                product_addtocartbtn.click()
                product_addtocartbtn.click()

                # ==== verify multiple notif ======
                multiple_notif_arraystr = "//*[@id='notification-box-top']/div"
                viewcartstr = "//*[@id='notification-box-top']/div/div[2]/div[2]/div[1]/a[contains(@class,'btn btn-primary btn-block') and contains(@href,'?route=checkout/cart')]"

                checkmultiple_notif = Driver.find_elements(By.XPATH, viewcartstr)
                checkmultiple_notif_count = len(checkmultiple_notif)

                viewcarttxt = WebDriverWait(Driver, 10).until(
                        EC.text_to_be_present_in_element((By.XPATH, viewcartstr), "View Cart"))
                viewcartbtn = WebDriverWait(Driver, 10).until(EC.element_to_be_clickable((By.XPATH, viewcartstr)))

                if (checkmultiple_notif_count < 2) and (viewcarttxt == True):
                    print(f'Total count of elements notif popup: {checkmultiple_notif_count}')
                    ISPOPUPNOTIF_TRIGGERED = False
                else:
                    print(f'Multiple notif triggered. Total count of elements: {checkmultiple_notif_count}')
                    ISPOPUPNOTIF_TRIGGERED = True
            else:
                print("Product not found. product page does not load properly")

        except Exception as ex:
            print(f"An error occurred: {ex}")
        return ISPOPUPNOTIF_TRIGGERED


    def IS_transactionhuistory_available(self,Driver):

        try:
            time.sleep(10)
            WebDriverWait(Driver, 10).until(EC.presence_of_element_located(pagelogo))
            WebDriverWait(Driver, 10).until(EC.presence_of_element_located(searchbutton))
            productIsearchinput = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(searchinput))
            user_cog_icon = WebDriverWait(Driver, 10).until(EC.element_to_be_clickable((By.XPATH, user_cog_iconstr)))
            user_cog_icon.click()

            # ======= Quick Links modal ===========
            time.sleep(5)
            quicklink_header = WebDriverWait(Driver, 5).until(
                EC.presence_of_element_located((By.XPATH, quicklink_headerstr)))
            registration_header = WebDriverWait(Driver, 5).until(
                EC.presence_of_element_located((By.XPATH, myaccount_linkstr)))
            registration_header.click()
            time.sleep(5)
            Driver.execute_script("window.scrollBy(0, 700);")
            order_historystr = "//*[@id='column-right']/div/a[7]"
            Driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(2)
            Driver.execute_script("window.scrollBy(0, 10);")
            get_orderhistory_redirlink = (WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, order_historystr))).get_attribute("href"))
            orderhistory_btn = WebDriverWait(Driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, order_historystr)))
            orderhistory_URL = get_orderhistory_redirlink

            orderhistory_btn.click()
            time.sleep(4)
            Driver.execute_script("window.scrollBy(0, 0);")
            time.sleep(4)

        except Exception as ex:
            print(f"An error occurred: {ex}")
        return orderhistory_URL
