import task10
import unittest

class TestTask10(unittest.TestCase):

    def test_sentence_case(self):
        self.assertEqual(task10.sentence_case("WELCOME, TEST AUTOMATION ENGINEER"), "Welcome, test automation engineer")



if __name__ == '__main__':
    unittest.main()