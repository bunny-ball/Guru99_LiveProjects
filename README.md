# Guru99 Live Projects
Here is my solutions for Guru99 Live Projects, using Pytest to verify results and Allure to generate test report.

**Environment**:

Python 3.10.11

Selenium 4.23.1

Pytest: 8.3.2

Allure: 2.30.0

Chrome Driver

----

###  Selenium_LiveProject1_Bank

- Day1 - Verify the login section
- Day2 - Enhancing Day1 script - Verifying Output
- Day3 - Enhancing Script - Parametrize data from Excel sheet
    - Key Point: Read data from excel file; Alert dialog handling
- Day4 - N/A
- Day5 - Enhancingscript - Verifying ManagerID, using parametrize data annotation
    - Key Point: Using two methods to parametrize data
- Day6 - Enhancing scripts - Adding Screenshot function

----

### Selenium Live Project 2 - Ecommerce
- Day 1 - Verify Mobile List can be sorted by Name
    - Key Point: "Select" function practice
- Day 2 - Verify prices are same in different pages
- Day 3 - Verify user cannot add more product in cart than the product available in store
- Day 4 - Verify popup window for comparing products
    - Key Point: Switch window/tab fundtion practice
- Day 5 - Verify account creation and wishlist share
- Day 6 - Verify user is able to purchase product using registered email id
- Day 7 - Verify user can print order as PDF 
    - Key Points: Using pyautogui to control the system window dialog
- Day 8 - Verify reordering can be done
- Day 9 - Verify Discout Coupon works correctly
    - Key Point: Automatic compare the price calculating.
- Day 10 - Emails (the export CSV function will cause an error in website, only write first three steps.)
    -- Key Point: Using ActionChains to practice cursor hover function

**NOTE**: The test cases/steps were provided by Guru99 - However I found some test cases where the steps were inconsistent with the actual website.

----

### Selenium Live Project 1 - Additional Practice
These [test case](https://clicks.aweber.com/y/ct/?l=K7I4nn&m=lPM79guQLUQLjy9&b=bQTsfzG3NlQJenF9yI2qIA) are provided through the 'Day 7: Project Closure' email of the Bank project.

Only practice the first three test scenarios, as the remaining test cases have a similar verify function.

Key Point:
- Transfer values from test case 1 to test case 2
- Use `@fixture` to run different test cases in one webdriver session

----

### Selenium Live Project 2 - Additional Practice
These [test case](https://clicks.aweber.com/y/ct/?l=6tm0&m=mjhACQKp7WFEjy9&b=x4nmnAI.0mGyaQdbD6sfGg) are provided through the 'Day 11: Project Closure' email of the Ecommerce project. 

- Test Case 1 - Verify invoice can be printed
    - Key Point: download file check/verify
- Test Case 2 - Verify the product review machanism
    - Key Point: Switch different webpage in one test case
- Test Case 3 - Verify sort is working correctly
    - Key Point: Sorting contents and verify contenst is sorted, time format change and verify
- Test Case 4 - Verify Search Functionality
    - Key Point: Select and print multi items
- Test Case 5 - Verify Disabled Fields (As the customer's details page is empty, this test case skiped.)