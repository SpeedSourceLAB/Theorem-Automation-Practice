# Theorem-Automation-Practice
Automation Testing Scripts for Theorem's MyStore Application.

This project's main purpose is to automate testing of different features in MyStore Web Applicaion to achieve maximum test coverage.

Technology Stack:

1)Python

2)Selenium

3)Gherkin (behave module of python)

4)Allure (for reporting)

#Setup and Execution steps

1)Python version used: Python 3.7.9

  Download and install Python from https://www.python.org/downloads/

2)Install Git.

  https://git-scm.com/downloads

3)Open Git Bash and clone this repository in a directory.
 $ https://github.com/SpeedSourceLAB/Theorem-Automation-Practice

4)Open the cloned project in any code editor like Pycharm.

5)Activate Virtual environment 

  Open terminal, move to Theorem_Automation_Practice directory and provide following command
  
  Ex: C:\PycharmProjects\Theorem-Automation-Practice\Theorem_Automation_Practice>
  
  .\venv_new\Scripts\activate

6)Install the dependant modules with command:

  pip install -r requirements.txt

7)To Execute test suite (Theorem_Automation_Practice/features/steps/MyStore_Steps.py)
 
 In terminal, move to Theorem_Automation_Practice directory and give command "behave"

   Ex: C:\PycharmProjects\Theorem-Automation-Practice\Theorem_Automation_Practice> behave

Note: Sleep is added in some places intentionally to slow down inorder observe the flow.

Test report
============
1)HTML format available at below location:

Theorem-Automation-Practice/Theorem_Automation_Practice/allure-report/index.html

2)Json format available at below location:

Theorem_Automation_Practice/reports


Some other Scenarios that can be implemeted but not limited to:
===============================================================
Browsing Scenarios
==================
1) Check if browsing of the catalog by color,size,price,styles etc. gives appropriate results.
2) Check whether user is shown different colors of the same model when available.
3) Check when user chooses an item in the catalog the application provides him/her with similar recommendations.

Field Validations
==================
1) Perform different field validation checks w.r.to their size or formats(email etc.) in account creation etc.    

Payment scenarios
================
1) Check when any discount/coupons are activated it reflects in the final payment.
2) Clicking cancel at anypoint of transaction before confirming the order should still have the products in cart and continue to shop.
3) Check if shipping and taxes are calculated as per the rules.
4) Check if the payments are processed accurately

Database Scenarios
==================
1) Check the prices and pictures shown are approriate to the users selection.
2) Check if user details updated correclty when done.
3) Check whether right user details are displayed in check out like address, name etc.
4) Does the summary of shopping cart correclty shows the users selection and quantity.
5) New catalog added should be displayed correctly in appropriate sections

Authentication Scenarios
===========================
1) Priovide different combinations of values for username and password like valid, invalid, empty etc. and check the results.
2) Verify the sensitive information like password, credit card numbers etc should display in encrypted format.

Performance Scenarios
=============
1)Identify the application and infrastructure bottlenecks.

2)Evaluate application or hardware if it can handle projected load volumes.

Other Scenarios
======
1) Check whether mail to friend works as intended.
2) Check whether Print option works as intended
3) User preferences are saved when he/she logins


Further Enchancements
==============
1)Better use of OOPS concetps in framework to enchance resuability and flexibility.

2)Better comments, and better implmentation of  logging module.

3)Integrate with Jenkins to achieve CI/CD pipeline.

4)Write well customized xpaths/css for web elements.

5)Eliminate sleep time and use appropriate alternatives.

6)Avoid hardcoding of values( this is currently partially implemented).

7)Perform cross platform testing.

8)Add performance tests.

9)Perform Data Driven Testing for both quality and coverage with out massive number of testcases.

10)Last but not the least, early testing and testing often will add tremendous value.



