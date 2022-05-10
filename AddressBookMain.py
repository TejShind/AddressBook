
"""
@Author: Tejaswini Shinde
@Date: 2022-05-04 4:42
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-05-09 21:48
@Title :Add multiple AddressBook in Address book.

"""

print("Welcome to Address Book")


class AddressBook:
    

    def __init__(self):
        """
        Description:
            main constrcutor whenever we will create object then we can runn this.
        Parameter:
            passing self.
        Return:
            Returning nothing but only calling menu function.
        """
        self.contact = {}
        self.contactLength = len(self.contact)
        self.contactInListLength = 0
        self.keysList = list(self.contact)

    def addContact(self,fName, lName, address, city, state, zip, mobileNumber, eMail):
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

        self.contactInListLength = len(contactInList)
        self.contact[self.contactLength] = contactInList
        self.keysList = list(self.contact)
        self.contactLength += 1
        return contactInList

    def editContact(self,contactNumber, fName, lName, address, city, state, zip, mobileNumber, eMail):
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

        self.contact[contactNumber] = contactInList
        return self.contact

    def deleteContact(self,contactNumber):
        """
            Description:
                deleting in existing Values contacts
            Parameter:
                contact number to acces the key value of dictionary as parameter
            Return:
                Returning conttact dictionary
        """
        del self.contact[contactNumber]
        return self.contact

if __name__ == '__main__':
    contact1 = {}
    contact1 = AddressBook()
    addressBookDict = {}
    contactIndex = 1
    contactDict = [contactIndex]

    def contactMenu():
    #     while True:
    #         check = int(input("""
    #                     1. Press 1 to Add Contact
    #                     2. Press 2 to Show Contact
    #                     3. Press 3 to edit Contact
    #                     4. Press 4 To Delete Contact
    #                     5. Press 5 To Exit
    #             """))

    #         if check == 1:
    #             fName = input("Enter First Name: ")
    #             lName = input("Enter Last Name: ")
    #             address = input("Enter Address: ")
    #             city = input("Enter City: ")
    #             state = input("Enter State: ")
    #             zip = int(input("Enter Zip Code: "))
    #             mobileNumber = int(input("Enter Mobile Number: "))
    #             eMail = input("Enter E mail: ")

    #             contact1.addContact(fName, lName, address,
    #                                 city, state, zip, mobileNumber, eMail)

    #         elif check == 2:
    #             print(contact1.contact)

    #         elif check == 3:
    #             checkFlag = False
    #             while True:
    #                 checkName = input("Enter First Name To Check Contact!")
    #                 for i in range(contact1.contactLength):

    #                     if checkName == contact1.contact[i][0]:
    #                         print("Now You Can Edit!")
    #                         fName = input("Enter First Name: ")
    #                         lName = input("Enter Last Name: ")
    #                         address = input("Enter Address: ")
    #                         city = input("Enter City: ")
    #                         state = input("Enter State: ")
    #                         zip = int(input("Enter Zip Code: "))
    #                         mobileNumber = int(input("Enter Mobile Number: "))
    #                         eMail = input("Enter E mail: ")

    #                         contact1.editContact(i, fName, lName, address, city, state, zip, mobileNumber, eMail)
    #                         checkFlag = True

    #                 if checkFlag == False:
    #                     print("Enter Valid Name!")

    #                 elif checkFlag == True:
    #                     break

    #         elif check == 4:
    #             checkFlag = False
    #             while True:
    #                 checkName = input("Enter First Name To Check Contact!")
    #                 for i in range(contact1.contactLength):

    #                     if checkName == AddressBook.contact[i][0]:
    #                         contact1.deleteContact(i)
    #                         checkFlag = True

    #                 if checkFlag == False:
    #                     print("Enter Valid Name!")

    #                 elif checkFlag == True:
    #                     break

    #         elif check == 4:
    #             print("BBye!")
    #             break

    #         else:
    #             print("Enter Valid Input")
            pass




    while True:
        addressbookCheck = int(input("""
                    1. Press 1 to Add AddressBook
                    2. Press 2 to Show AddressBook
                    3. Press 3 to Add Contacts in AddressBook
                    4. Press 4 To Exit
            """))
        
        if addressbookCheck == 1:
            addressBookName = input("Enter Name Of AddressBook!")
            addressBookDict.update({addressBookName:""})
            contactIndex += 1
            contactDict = {}

        elif addressbookCheck == 2:
            print(addressBookDict)

        elif addressbookCheck == 3:
            print("All AddressBook Names: ",addressBookDict.keys())
            checkFlag = False
            while True:
                checkName = input("Enter Name Of Address Book!")
                for i in addressBookDict.keys():
                    contactListF = []
                    if checkName == i:

                        while True:  
                            checkValue = int(input("""
                                    1. Enter 1 To Add Contacts Details
                                    2. Enter 2 To Exit
                            """))

                            if checkValue == 1:
                                fName = input("Enter First Name: ")
                                lName = input("Enter Last Name: ")
                                address = input("Enter Address: ")
                                city = input("Enter City: ")
                                state = input("Enter State: ")
                                zip = int(input("Enter Zip Code: "))
                                mobileNumber = int(input("Enter Mobile Number: "))
                                eMail = input("Enter E mail: ")

                                contactListF.append(contact1.addContact(fName, lName, address,city, state, zip, mobileNumber, eMail))

                            elif checkValue == 2:
                                addressBookDict.update({checkName:contactListF})
                                break

                            else:
                                print("Enter Valid Option")
                        
                        checkFlag = True

                    elif checkFlag == True:
                        break

                if checkFlag == True:
                    break
                
                elif checkFlag == False:
                    print("Enter valid AddressBook Name!")

            
        elif addressbookCheck == 4:
            print("Exit")
            break