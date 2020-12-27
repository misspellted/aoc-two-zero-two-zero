

from results import example, generated
from unittest import TestCase
from two.two import TwoTwo


class TestTwoTwoExample(TestCase):
  def setUp(self):
    self.tested = TwoTwo()
    self.tested.use(self.tested.exampleData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), example(22, 1))

  def testPartTwo(self):
    self.skipTest("D22P2 not implemented")
    self.assertEqual(self.tested.two(), example(22, 2))


class TestTwoTwoGenerated(TestCase):
  def setUp(self):
    self.tested = TwoTwo()
    self.tested.use(self.tested.generatedData())

  def testPartOne(self):
    self.assertEqual(self.tested.one(), generated(22, 1))

  def testPartTwo(self):
    self.skipTest("D22P2 not implemented")
    self.assertEqual(self.tested.two(), generated(22, 2))

