

from results import example, generated
from unittest import TestCase
from zero.two import ZeroTwo


class TestZeroTwoExample(TestCase):
  def setUp(self):
    self.tested = ZeroTwo()
    self.tested.use(self.tested.exampleData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), example(2, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), example(2, 2))


class TestZeroTwoGenerated(TestCase):
  def setUp(self):
    self.tested = ZeroTwo()
    self.tested.use(self.tested.generatedData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), generated(2, 1))

  def testPartTwo(self):
    self.assertEqual(self.tested.two(), generated(2, 2))

