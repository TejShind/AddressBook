"""
@Author: Tejaswini Shinde
@Date: 2022-05-08 22:59
@Last Modified by: Tejaswini Shinde
@Last Modified time: 0222-05-09 14:36
@Title : Edit contacts in Address book Testing.
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
       # self.assertEqual(TestAddressBook.contact[0],["Tejaswini","Shinde","Hadpsar","Pune","Maharashtra",411028,823721985,"tej.gholap25@gmail"])

    def test_addContact_length(self):
        """
            Description:
                testing add function methods is working or not and mainly checking length of add function from AddressBookMain.py
            Parameter:
                self is as parameter
            Return:
                none
        """
        length_lst=len(AddressBookMain.AddressBook.addContact("komal","gholap","Kasba peth","Pune","maharashtra",411011,988877788,"komalghol85@gmail.com"))
        self.assertEqual(length_lst, 8)

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

if __name__ == "__main__":
    unittest.main()