import unittest 
from myodule import Myclass

class TestMyclass(unittest.TestCase):
	def test_add(self):
		my_instance = Myclass()
		result = my_instance.add(2, 3)
		self.assertEqual(result, 5)

if __name__ == "__main__":
	unittest.main()

