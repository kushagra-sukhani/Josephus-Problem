import unittest
import josephus_problem

class TestJosephusProblem(unittest.TestCase):
	"""
        This class is Unit test class for josephus_problem.py.
	"""

	def test_find_person_alive(self):
		self.assertEqual(josephus_problem.find_person_alive(10),5)
		self.assertEqual(josephus_problem.find_person_alive(100),73)
		self.assertEqual(josephus_problem.find_person_alive(41),19)
		self.assertEqual(josephus_problem.find_person_alive(10),5)


if __name__ == '__main__':
	unittest.main()