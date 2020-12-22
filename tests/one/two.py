

from results import example, generated
from unittest import TestCase
from one.two import OneTwo


class TestOneTwoExample(TestCase):
  def setUp(self):
    self.tested = OneTwo()
    self.tested.use(self.tested.exampleData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), example(12, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), example(12, 2))


class TestOneTwoGenerated(TestCase):
  def setUp(self):
    self.tested = OneTwo()
    self.tested.use(self.tested.generatedData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), generated(12, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), generated(12, 2))

