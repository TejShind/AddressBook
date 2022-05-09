"""
@Author: Tejaswini Shinde
@Date: 2022-05-08 22:59
@Last Modified by: Tejaswini Shinde
@Last Modified time: No
@Title : Add contacts in Address book Testing.
"""
import unittest
import AddressBookMain

class TestAddressBook(unittest.TestCase):
    def test_addition(self):
        get_lst=AddressBookMain.AddressBook.addContact("Tejaswini","Shinde","Hadpsar","Pune","Maharashtra",411028,823721985,"tej.gholap25@gmail")
        self.assertEqual(get_lst, ["Tejaswini","Shinde","Hadpsar","Pune","Maharashtra",411028,823721985,"tej.gholap25@gmail"])
    
    def test_check(self):
        length_lst=len(AddressBookMain.AddressBook.addContact("Tejaswini","Shinde","Hadpsar","Pune","Maharashtra",411028,823721985,"tej.gholap25@gmail"))
        self.assertEqual(length_lst, 8)

if __name__ == "__main__":
    unittest.main()