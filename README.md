# asymmetrikProgrammingChallenge
Problem: Business Card OCR
Language: Python 3.7

Assumptions made:
1. First and last names contain more than 1 letter and contain only alphabets
2. Phone numbers are american phone number format (10 digits or 11 with extension)
3. Email addresses contain '@' and end in '.com' and no other special characters(only digits and alphabets)

Note: Python regular expression module 're' is used

Note: The function that extracts the name from a business card is primitive and works off of a finite set of 
keywords presented in the problem description. This function specifically could be improved using machine learning
to increase the size of the set of keywords ('findNames(name)') for more accurate extraction of names from cards. Currently
the function would perform poorly given a business card with keywords that the function has not seen.

Note: Program accurately solves all example problems provided in problem description.

Build and run python file

ContactInfo: class that encapsulates name, email and phone number
BusinessCardParser: static class that parses a card, getContactInfo(document) returns a ContactInfo given a card

How to test:
An example of a test:
card = #some string with card info (new line is specified using '\n')
contactInfo = BusinessCardParser.getContactInfo(card)
name, phone, email = contactInfo.getName(), contactInfo.getPhoneNumber(), contactInfo.getEmailAddress()
print(name, phone, email)
