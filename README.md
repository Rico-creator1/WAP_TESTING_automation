# WAP UI TESTING automation 

TEST URL = POCO webUI (https://ecommerce-playground.lambdatest.io/)

This test automation covers important test scenarios for a mobile compatible WAP e-commerce website. 
I included end-to-end functionality testing, mobile compatibility (mobile emulation), security testing, verify unexpected pop-up. 
<br>Test cases 
  * Functionality testing (E2E)
	  * test_User_Registration_test
	  * test_LoginUser_with_proper_user_credential_test
	  * test_Verify_that_registered_user_can_perform_Complete_Checkout_Process
  * Mobile compatibility (runs in mobile size browser)
	  * test_if_browser_open_in_mobile_mode
  * Verify unexpected pop-up
     <br> * test_handling_popup_notification
  * Security test ( verify if a guest user cannot view transaction history)
     <br> * test_transactionpage_is_avalable_for_guessUser
		 
 - I used page object for organization of functions and objects. Also to make them reusable.
  folder structure:
    - wapuitesting 
      - pom 
	<br>- test (location of test files)
        <br>- pages (location of page objects)
      - Test Results - pytest.html

note: 
	- This script is working on full mobile screen on my machine (as per yesterday). However got some issue with my main desktop so I need to switch to vbox to record the video. unfortunately the vbox image has fixed resolution so the execution demo looks big (low resolution).

PYtest EXECUTION DEMO:


[![IMAGE ALT TEXT HERE]](https://github.com/Rico-creator1/WAP_TESTING_automation/assets/55780542/94f0dd18-bc7f-4838-9181-bec08e01b094)


