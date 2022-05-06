"""
@Author: Tejaswini Shinde
@Date: 2022-05-04 4:42
@Last Modified by: Tejaswini Shinde
@Last Modified time: No
@Title : Add multiple person in Address book.
"""

print("Welcome to Address Book")

# Importing Contacts Class
from Contacts import Contacts
class AddressBook:


    def add_Contact():

        """
        Description: Adding Contact Details form Console & returning that details as an object of Contacts Class
        Parameters: None
        Returns: Returns Conatacts class object having all info
        """
        try:
         first_name = input("Enter the first name: ")
         last_name = input("Enter the last name: ")
         address = input("Enter the address: ")
         city = input("Enter city name: ")
         state = input("Enter state name: ")
         zip =int( input("Enter zip code: "))
         phone_number = int(input("Enter phone number: "))
         email = input("Enter email address: ")
         contact_obj = Contacts(first_name, last_name, address,city, state, zip, phone_number, email)
         return contact_obj
        except Exception as ex:
         print(ex)

def Storing_contacts_in_list():
    """
        Description: Adding Contact Details form Console in list
        Parameters: None
        Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
    """
    try:
        while(True):
            #contact_obj = add_Contact()
            #contacts_list.append(contact_obj)
            contacts_add_choice = input("Enter \"Y\" for adding more & \"N\" to stop adding: ")
            if (contacts_add_choice.upper() == "N"):
                break
        return contacts_list        
    except Exception as ex:
        print(ex)
        
def Editing_contacts(con_list):
    """
        Description: Editing Contact Details form Console i.e. by user choice
        Parameters: None
        Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
    """
    edited_person_name = input(
        "Enter the name of person, whom details you want to edit: ").upper()
    try:
        for item in con_list:
            if item.first_name.upper() == edited_person_name:
                choice = input(
                    "Enter choice u want to edit:\n 1 : FN,2 : LN,3 : Address,4 : City,5 : State,6 : ZIP,7 : Phone,8 : Email")
                if (choice == "1"):
                    fn = input("Enter updated first name: ")
                    item.first_name = fn
                elif (choice == "2"):
                    ln = input("Enter updated last name: ")
                    item.last_name = ln
                elif (choice == "3"):
                    addrs = input("Enter updated address: ")
                    item.address = addrs
                elif (choice == "4"):
                    city = input("Enter updated city: ")
                    item.city = city
                elif (choice == "5"):
                    state = input("Enter updated state: ")
                    item.state = state
                elif (choice == "6"):
                    zip = input("Enter updated zip: ")
                    item.zip = zip
                elif (choice == "7"):
                    phn_no = input("Enter updated phn number: ")
                    item.phone_number = phn_no
                elif (choice == "8"):
                    email = input("Enter updated email: ")
                    item.email = email
                else:
                    print("Invalid Choice")
    except Exception as ex:
        print(ex)         

if __name__=="__main__":

    contacts_list = []
    Storing_contacts_in_list()
    user_choice = input("Do u want to edit Contacts \"Y\" OR \"N\":").upper()
    if (user_choice.upper() == "Y"):
        Editing_contacts(contacts_list)
    for item in contacts_list:
        print(str(item))
    contact1 = {}
    contact1 = AddressBook()
    addressBookDict = {}
    contactIndex = 1
    contactDict = [contactIndex]

    def contactMenu():
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
                                phoneNumber = int(input("Enter Mobile Number: "))
                                eMail = input("Enter E mail: ")

                                contactListF.append(contact1.addContact(fName, lName, address,city, state, zip, phoneNumber, eMail))

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
            break