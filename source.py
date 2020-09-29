import re

class ContactInfo:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def getName(self) -> str:
        return self.name

    def getPhoneNumber(self) -> str:
        return self.number

    def getEmailAddress(self) -> str:
        return self.email

class BusinessCardParser:
    namePattern = "^[A-Z][a-z]*\s[A-Z][a-z]*[a-z]$"
    phonePattern = "((Fax:\s)?\+?\s?\d?\s?\(?\d+\)?\s?-?\s?\d+\s?-\s?\d+$)"
    emailPattern = "\s?[a-zA-Z\d]+@[a-zA-Z\d]+\.com"
    keyWords = ["Tech", "Analytic", "Develop", "Software", "Engineer"]

    def getContactInfo(document:str) -> ContactInfo:
        names = re.findall(BusinessCardParser.namePattern, document, re.MULTILINE)
        name = BusinessCardParser.findName(names)
        phones = re.findall(BusinessCardParser.phonePattern, document, re.MULTILINE)
        phone = BusinessCardParser.findPhone(phones)
        phone = BusinessCardParser.formatPhone(phone)
        email = re.search(BusinessCardParser.emailPattern, document, re.MULTILINE).group(0)
        email = BusinessCardParser.formatEmail(email)
        return ContactInfo(name, phone, email)

    def formatEmail(email):
        start = 0;
        if email[0].isspace():
            start += 1
        return email[start:]

    def findPhone(phones):
        result = ""
        for phone in phones:
            for group in phone:
                if "fax" not in group.lower():
                    result += group
        return result

    def formatPhone(phone):
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        result = ""
        for character in phone:
            if character in nums:
                result += character
        return result

    def findName(names):
        if len(names) < 1:
            print("could not find name")
            return None
        if len(names)==1:
            return names[0]
        name = names[0]
        for keyword in BusinessCardParser.keyWords:
            if keyword.lower() in name.lower():
                names.pop(0)
                return BusinessCardParser.findName(names)
        return name
# TEST
#card1 = "ASYMMETRIK LTD\nMike Smith\nSenior Software Engineer\n(410)555-1234\nmsmith@asymmetrik.com"
#ci1 = BusinessCardParser.getContactInfo(card1)
#card2 = "Foobar Technologies\nAnalytic Developer\nLisa Haung\n1234 Sentry Road\nColumbia, MD 12345\nPhone: 410-555-1234\nFax: 410-555-4321\nlisa.haung@foobartech.com"
#ci2 = BusinessCardParser.getContactInfo(card2)
#card3 = "Arthur Wilson\nSoftware Engineer\nDecision & Security Technologies\nABC Technologies\n123 North 11th Street\nSuite 229\nArlington, VA 22209\nTel: +1 (703) 555-1259\nFax: +1 (703) 555-1200\nawilson@abctech.com"
#ci3 = BusinessCardParser.getContactInfo(card3)

#print(ci1.getName())
#print(ci1.getPhoneNumber())
#print(ci1.getEmailAddress())
#print(ci2.getName())
#print(ci2.getPhoneNumber())
#print(ci2.getEmailAddress())
#print(ci3.getName())
#print(ci3.getPhoneNumber())
#print(ci3.getEmailAddress())