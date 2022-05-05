
"""
@Author: Tejaswini Shinde
@Date: 2022-05-04 4:42
@Last Modified by: Tejaswini Shinde
@Last Modified time: No
@Title :Add contacts in Address book.

"""

print("Welcome to Address Book")

class Contacts:

    def __init__(self, first_name, last_name, address, city, state, zip, phone_number, email):
        """
            Description:
                Function is used getting values for object of AddressBook
            Parameter:
                Object with their specific data type
            Return:
                Updated Object as per our arguments
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email


    def __str__(self):
        """
            Description: To return textual content of the Contacts class Object
            Parameters: Takes Instance (Object) of class as arguments
            Returns: Returns String Representation of object, understandable by User
        """
        return "First Name is " + str(self.first_name)  +  " , Last name is "+ str(self.last_name)  +  " , Address is "+str(self.address) + " , City is "+str(self.city) + " , State is "+ str(self.state) + ", Zip code is "+ str(self.zip)+", Phone no is "+str(self.phone_number) + ", Email is "+ str(self.email)


def add_Contact():

        """
        Description: Adding Contact Details form Console & returning that details as an object of Contacts Class
        Parameters: None
        Returns: Returns Conatacts class object having all info
        """
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        address = input("Enter the address: ")
        city = input("Enter city name: ")
        state = input("Enter state name: ")
        zip = input("Enter zip code: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact_obj = Contacts(first_name, last_name, address,city, state, zip, phone_number, email)
        return contact_obj

def Storing_contacts_in_list():
    """
        Description: Adding Contact Details form Console in list
        Parameters: None
        Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
    """
    while(True):
        contact_obj = add_Contact()
        contacts_list.append(contact_obj)
        contacts_add_choice = input("Enter \"Y\" for adding more & \"N\" to stop adding: ")
        if (contacts_add_choice.upper() == "N"):
            break
    return contacts_list        

if __name__=="__main__":

 contacts_list = []
Storing_contacts_in_list()
for item in contacts_list:
        print(str(item))