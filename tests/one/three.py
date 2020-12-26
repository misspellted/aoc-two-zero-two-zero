

from results import example, generated
from unittest import TestCase
from one.three import OneThree


class TestOneThreeExample(TestCase):
  def setUp(self):
    self.tested = OneThree()
    self.tested.use(self.tested.exampleData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), example(self.tested.day, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), example(self.tested.day, 2))


class TestOneThreeGenerated(TestCase):
  def setUp(self):
    self.tested = OneThree()
    self.tested.use(self.tested.generatedData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), generated(self.tested.day, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), generated(self.tested.day, 2))

