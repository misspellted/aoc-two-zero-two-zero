

from results import example, generated
from unittest import TestCase
from zero.one import ZeroOne


class TestZeroOneExample(TestCase):
  def setUp(self):
    self.tested = ZeroOne(2020)
    self.tested.use(self.tested.exampleData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), example(1, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), example(1, 2))


class TestZeroOneGenerated(TestCase):
  def setUp(self):
    self.tested = ZeroOne(2020)
    self.tested.use(self.tested.generatedData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), generated(1, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), generated(1, 2))

