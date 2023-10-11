# portfolio-test
Title: Automated E-commerce Website Testing Framework

Description:

This GitHub repository contains a comprehensive suite of automated tests developed using Python, the Pytest testing framework, Selenium WebDriver, and Allure reporting. My testing framework follows the proven Page Object Model (POM) pattern to ensure maintainability and efficiency in testing e-commerce website.

Key Features:

**Python & Pytest**: My test suite is built using Python, a popular and versatile programming language, and the Pytest framework, renowned for its simplicity and scalability. These tools make writing and running test cases easy, managing test data, and performing assertions.

**Selenium WebDriver**: I leverage the Selenium WebDriver for browser automation. This allows us to interact with e-commerce websites just like a real user, performing actions like clicking buttons, filling out forms, and navigating through pages. Selenium supports various browsers, ensuring compatibility across different platforms.

**Allure Reporting**: My test suite integrates with Allure reporting, a powerful tool for generating detailed and visually appealing test reports. With Allure, you can track test execution, view test history, and analyze test results with insightful graphs and charts.

**Page Object Model (POM)**: I've structured my tests using the Page Object Model pattern. This architectural approach separates the test logic from the UI, making maintenance more straightforward. Each page of e-commerce website has a corresponding Page Object, encapsulating the page's elements and actions. This way, changes to the UI are isolated and don't impact the entire test suite.

Conftest Configuration:

My conftest.py file is configured to offer the flexibility to test e-commerce website on different environments. This configuration allows you to seamlessly switch between development, staging, and production environments, adapting tests to various scenarios.

Additional Test Scenarios:

**Order Tests**: Validate the end-to-end order process, from product selection to payment confirmation, ensuring a seamless customer experience.

**Account Creation**: Verify that users can successfully create accounts on the website. This includes form validation and email confirmation steps.

**Account Login**: Ensure that users can log in with their credentials and access their accounts. Test scenarios cover login functionality and security.

**Password Change**: Test the functionality for users to change their passwords securely. Verify that the process works without issues and adheres to security best practices.

**Search Input**: Ensure that users can effectively search for products on the website using the search input. Test various search queries and verify search results.

**Add Product to Cart**: Validate the product selection and cart functionality. Confirm that products can be added to the cart and that the cart accurately reflects the selected items.

**Contact Form**: Test the contact form feature to ensure users can contact support or sales teams. Verify that the form submissions are processed correctly.

**Choose Product Extra Options**: Verify that users can customize their product selections by choosing extra options. Test these options to ensure accurate product customization.
