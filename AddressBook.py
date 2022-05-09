
"""
@Author: Tejaswini Shinde
@Date: 2022-05-04 3:42
@Last Modified by: Tejaswini Shinde
@Last Modified time: No
@Title : Add contacts in Address book.

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


def __str__(self):
        """
            Description: To return textual content of the Contacts class Object
            Parameters: Takes Instance (Object) of class as arguments
            Returns: Returns String Representation of object, understandable by User
        """
        return "First Name is " + str(self.first_name)  +  " , Last name is "+ str(self.last_name)  +  " , Address is "+str(self.address) + " , City is "+str(self.city) + " , State is "+ str(self.state) + ", Zip code is "+ str(self.zip)+", Phone no is "+str(self.phone) + ", Email is "+ str(self.email)

if __name__=="__main__":

    contact1=Contacts("Tejaswini","Gholap","Hadpsar","Pune","Maharashtra",411028,823721985,"tej.gholap25@gmail")
    print(contact1.__str__())        