
"""
@Author: Tejaswini Shinde
@Date: 2022-05-04 3:42
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-05-09 14:20
@Title : Edit contacts in Address book.

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

    def editContact(contactNumber,fName, lName, address,city, state, zip, mobileNumber, eMail):
        """
            Description:
                editing in existing Values contact using editing contacts functions
            Parameter:
                self is as parameter
            Return:
                Returning nothing just saving values (updating) of contact
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

    def matching_AddressBook_To_Print(matchNum, i, j):
        """
            Description:
                showing contacts using this function
            Parameter:
                taking parametrs from another method index
            Return:
                Returning nothing but printing switch methods
        """
        match matchNum:
            case 0:
                print("\n Index number: ", AddressBook.keysList[i])
                Value = AddressBook.keysList[i]
                return Value
            case 1:
                print("First Name Is: ", AddressBook.contact[i][j])
                Value = AddressBook.keysList[i]
                return Value
            case 2:
                print("Last name Is: ", AddressBook.contact[i][j])
                Value = AddressBook.keysList[i]
                return Value
            case 3:
                print("Address Is: ", AddressBook.contact[i][j])
                Value = AddressBook.keysList[i]
                return Value
            case 4:
                print("City Is: ", AddressBook.contact[i][j])
                Value = AddressBook.keysList[i]
                return Value
            case 5:
                print("State Is: ", AddressBook.contact[i][j])
                Value = AddressBook.keysList[i]
                return Value
            case 6:
                print("Zip Code Is: ", AddressBook.contact[i][j])
                Value = AddressBook.keysList[i]
                return Value
            case 7:
                print("Mobile Number Is: ", AddressBook.contact[i][j])
                Value = AddressBook.keysList[i]
                return Value
            case 8:
                print("Email Is: ", AddressBook.contact[i][j])
                Value = AddressBook.keysList[i]
                return Value    


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
                    3. Press 3 to Edit Contact
                    3. Press 4 To Exit
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



