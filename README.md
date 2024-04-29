# WAP UI TESTING automation

URL = [http://uitestingplayground.com/](https://ecommerce-playground.lambdatest.io/)

This test automation covers important test scenario for a WAP e-commerce UI
 this includes end-to-end functionality testing, mobile compatibility (mobile emulator), security testing, verify unexpected pop-up. 
  Test cases 
  * Functionality testing (E2E)
	  * test_User_Registration_test
	  * test_LoginUser_with_proper_user_credential_test
	  * test_Verify_that_registered_user_can_perform_Complete_Checkout_Process
	* Mobile compatibility (runs in mobile size browser)
    * test_if_browser_open_in_mobile_mode
  * verify unexpected pop-up
    * test_handling_popup_notification
	* negative test ( verify if the guest user cannot view transaction history)
   * test_transactionpage_is_avalable_for_guessUser
		 
 - I used page object for organization of functions and objects. Also to make them reusable.
  wapuitesting
    |
     - pom
        |
          - test (location of test files)
        |
          - pages (location of page objects)
        |
    - Test Results - pytest.html

note: this script is working on full mobile screen (as per yesterday). however got some issue with my main desktop so I need to switch to vbox. unfortunately the vbox image has fix resolution so the execution demo looks big.

PYtest EXECUTION DEMO:





