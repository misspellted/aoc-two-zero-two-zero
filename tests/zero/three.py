

from results import example, generated
from unittest import TestCase
from zero.three import ZeroThree


class TestZeroThreeExample(TestCase):
  def setUp(self):
    self.tested = ZeroThree()
    self.tested.use(self.tested.exampleData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), example(3, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), example(3, 2))


class TestZeroThreeGenerated(TestCase):
  def setUp(self):
    self.tested = ZeroThree()
    self.tested.use(self.tested.generatedData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), generated(3, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), generated(3, 2))

