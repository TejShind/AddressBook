"""
@Author: Tejaswini Shinde
@Date: 2022-05-08 22:59
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-05-09 21:36
@Title : Delete contacts in Address book Testing.
"""
import unittest
import AddressBookMain

class TestAddressBook(unittest.TestCase):
    contact = {}
    contactLength = len(contact)
    contactInListLength = 0
    contactList = []

    def test_addContact(self):
        """
            Description:
                testing add function methods is working or not from AddressBookMain.py
            Parameter:
                self is as parameter
            Return:
                none
        """

        TestAddressBook.contact = AddressBookMain.AddressBook.addContact("Tejaswini","Shinde","Hadpsar","Pune","Maharashtra",411028,823721985,"tej.gholap25@gmail")
        self.assertEqual(TestAddressBook.contact[0],["Tejaswini","Shinde","Hadpsar","Pune","Maharashtra",411028,823721985,"tej.gholap25@gmail"])

    def test_multipleAddContact_length(self):
        """
            Description:
                testing add function methods is working or not and mainly checking length of add function from AddressBookMain.py
            Parameter:
                self is as parameter
            Return:
                none
        """
        TestAddressBook.contact=AddressBookMain.AddressBook.addContact("komal","gholap","Pimpri","Pune","Maharashtra",411021,8888555511,"komalgholap17@gmail.com")
        contactLength = len(TestAddressBook.contact)
        self.assertEqual(contactLength,2) 

    def test_editContact(self):
        """
            Description:
                Testing edit function methods is working or not from AddressBookMain.py
            Parameter:
                Self is as parameter
            Return:
                None
        """
        TestAddressBook.contact = AddressBookMain.AddressBook.editContact(0,"tejaswini","shinde","Hadpsar","Pune"," Maharashtra",411028,8237219888,"tej.gholap25@gmail.com")
        self.assertEqual(TestAddressBook.contact[0],["tejaswini","shinde","Hadpsar","Pune"," Maharashtra",411028,8237219888,"tej.gholap25@gmail.com"])


    def test_deleteContact(self):
        """
            Description:
                Testing delete methods is working or not from AddressBookMain.py
            Parameter:
                self is as parameter
            Return:
                none
        """
        contactLengthCheck = len(TestAddressBook.contact)
        TestAddressBook.contact = AddressBookMain.AddressBook.deleteContact(0)
        self.assertEqual(len(TestAddressBook.contact),contactLengthCheck-1)

if __name__ == "__main__":
    unittest.main()