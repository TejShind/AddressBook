
"""
@Author: Tejaswini Shinde
@Date: 2022-05-04 3:42
@Last Modified by: Tejaswini Shinde
@Last Modified time:2022-05-09 12:08
@Title : Create contacts in Address book.

"""

print("Welcome to Address Book")

class AddressBook:
    contact = {}
    contactLength = len(contact)
    keys_list = list(contact)
    def __init__(self):
        """
        Description:
            main constrcutor whenever we will create object then we can runn this.
        Parameter:
            passing all contact details.
        Return:
            Returning nothing but saving values in main variables.
        """
        pass

    def addContact(fName,lName,address,city,state,zip,mobileNumber,eMail):

        contactInList = []
        
        contactInList.append(fName)
        contactInList.append(lName)
        contactInList.append(address)
        contactInList.append(city)
        contactInList.append(state)
        contactInList.append(zip)
        contactInList.append(mobileNumber)
        contactInList.append(eMail)

        AddressBook.contact[AddressBook.contactLength] = contactInList
        AddressBook.contactLength += 1
        AddressBook.keys_list = list(AddressBook.contact)
        return contactInList

if __name__ == '__main__':
    fName = input("Enter First Name: ")
    lName = input("Enter Last Name: ")
    address = input("Enter Address: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    zip = int(input("Enter Zip Code: "))
    mobileNumber = int(input("Enter Mobile Number: "))
    eMail = input("Enter E mail: ")

    Contact1 = AddressBook()
    AddressBook.addContact(fName,lName,address,city,state,zip,mobileNumber,eMail)
    print("Index number: ", AddressBook.keys_list[0])
    print("First Name Is: " , AddressBook.contact[0][0])
    print("Last name Is: ", AddressBook.contact[0][1])
    print("Address Is: ", AddressBook.contact[0][2])
    print("City Is: ", AddressBook.contact[0][3])
    print("State Is: ", AddressBook.contact[0][4])
    print("Zip Code Is: ", AddressBook.contact[0][5])
    print("Mobile Number Is: ", AddressBook.contact[0][6])
    print("Email Is: ", AddressBook.contact[0][7])
