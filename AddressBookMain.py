
"""
@Author: Tejaswini Shinde
@Date: 2022-05-04 3:42
@Last Modified by: Tejaswini Shinde
@Last Modified time: No
@Title : Create contacts in Address book.

"""

print("Welcome to Address Book")

class AddressBook:
    contact = {}
    contactLength = len(contact)
    contactInListLength = 0
    keysList = list(contact)

    def __init__(self):
        """
        Description:
            main constrcutor whenever we will create object then we can runn this.
        Parameter:
            passing self.
        Return:
            Returning nothing but only calling menu function.
        """
        pass

    def addContact(fName, lName, address, city, state, zip, mobileNumber, eMail):
        """
            Description:
                adding contact using add contacts functions
            Parameter:
                self is as parameter
            Return:
                Returning nothing just saving values of contact
        """

        contactInList = []

        contactInList.append(fName)
        contactInList.append(lName)
        contactInList.append(address)
        contactInList.append(city)
        contactInList.append(state)
        contactInList.append(zip)
        contactInList.append(mobileNumber)
        contactInList.append(eMail)

        AddressBook.contactInListLength = len(contactInList)
        AddressBook.contact[AddressBook.contactLength] = contactInList
        AddressBook.keysList = list(AddressBook.contact)
        AddressBook.contactLength += 1
        return contactInList


    def showContact():
        """
            Description:
                showing contacts using this function
            Parameter:
                No Parameter
            Return:
                Returning nothing just calling another switch case method
        """
        for i in range(len(AddressBook.keysList)):
            for j in range(AddressBook.contactInListLength):
                AddressBook.matching_AddressBook_To_Print(j,i,j)


if __name__ == '__main__':
    contact1 = AddressBook()

    while True:
        check = int(input("""
                    1. Press 1 to Add Contact
                    2. Press 2 to Show Contact
                    3. Press 3 To Exit
            """))

        if check == 1:
            fName = input("Enter First Name: ")
            lName = input("Enter Last Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            zip = int(input("Enter Zip Code: "))
            mobileNumber = int(input("Enter Mobile Number: "))
            eMail = input("Enter E mail: ")

            AddressBook.addContact(fName, lName, address, city, state, zip, mobileNumber, eMail)

        elif check == 2:
            AddressBook.showContact()

            break

        else:
            print("Enter Valid Input")