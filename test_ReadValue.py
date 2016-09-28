__author__ = 'Daniel'

import unittest
from ReadValue import *

class test_ReadValue(unittest.TestCase):
  def test_upper(self):
      print("Test running")
      print("Test 110 years ReadValue('EURUSD', 60*60*24*365*110):", ReadValue('EURUSD', 60*60*24*365*115 + 60*60*24*40))
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())
