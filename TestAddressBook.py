
"""
@Author: Tejaswini Shinde
@Date: 2022-05-08 22:59
@Last Modified by: Tejaswini Shinde
@Last Modified time: No
@Title : Add contacts in Address book Testing.

"""
import unittest

import AddressBook


class TestAddressBook(unittest.TestCase):

    def test_addContact(self):
        
        self.AddressBook.Contacts("Tejaswini","Shinde","Hadpsar","Pune","Maharashtra",411028,823721985,"tej.gholap25@gmail")
        self.AddressBook.Contacts("Tej","Gho","Pune","Pune","Maharashtra",411011,8889997774,"tej.df5@gmail")
        self.assertEquals(len(AddressBook.Contacts.addContact),2)

if __name__ == "__main__":
    unittest.main()