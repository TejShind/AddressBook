
"""
@Author: Tejaswini Shinde
@Date: 2022-05-04 4:42
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-05-09 20:333
@Title :Delete contacts in Address book.

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
                Returning contact dictionary
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
        return AddressBook.contact

    def editContact(contactNumber, fName, lName, address, city, state, zip, mobileNumber, eMail):
        """
            Description:
                editing in existing Values contact using editing contacts functions
            Parameter:
                self is as parameter
            Return:
                Returning contact dictionary
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

        AddressBook.contact[contactNumber] = contactInList
        return AddressBook.contact

    def deleteContact(contactNumber):
        """
            Description:
                deleting in existing Values contacts
            Parameter:
                contact number to acces the key value of dictionary as parameter
            Return:
                Returning conttact dictionary
        """
        del AddressBook.contact[contactNumber]
        return AddressBook.contact

if __name__ == '__main__':
    contact1 = AddressBook()

    while True:
        check = int(input("""
                    1. Press 1 to Add Contact
                    2. Press 2 to Show Contact
                    3. Press 3 to edit Contact
                    4. Press 4 To Delete Contact
                    5. Press 5 To Exit
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

            AddressBook.addContact(fName, lName, address,
                                   city, state, zip, mobileNumber, eMail)

        elif check == 2:
            print(AddressBook.contact)

        elif check == 3:
            checkFlag = False
            while True:
                checkName = input("Enter First Name To Check Contact!")
                for i in range(AddressBook.contactLength):

                    if checkName == AddressBook.contact[i][0]:
                        print("Now You Can Edit!")
                        fName = input("Enter First Name: ")
                        lName = input("Enter Last Name: ")
                        address = input("Enter Address: ")
                        city = input("Enter City: ")
                        state = input("Enter State: ")
                        zip = int(input("Enter Zip Code: "))
                        mobileNumber = int(input("Enter Mobile Number: "))
                        eMail = input("Enter E mail: ")

                        AddressBook.editContact(i, fName, lName, address, city, state, zip, mobileNumber, eMail)
                        checkFlag = True

                if checkFlag == False:
                    print("Enter Valid Name!")

                elif checkFlag == True:
                    break

        elif check == 4:
            checkFlag = False
            while True:
                checkName = input("Enter First Name To Check Contact!")
                for i in range(AddressBook.contactLength):

                    if checkName == AddressBook.contact[i][0]:
                        AddressBook.deleteContact(i)
                        checkFlag = True

                if checkFlag == False:
                    print("Enter Valid Name!")

                elif checkFlag == True:
                    break

        elif check == 4:
            print("BBye!")
            break

        else:
            print("Enter Valid Input")