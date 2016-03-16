from unittest import TestCase
import LoadFeed

__author__ = 'Daniel'

class TestFLoadData(TestCase):
  def test_fLoadData(self):
    fLoadData('./feeds/EURUSD.csv')
