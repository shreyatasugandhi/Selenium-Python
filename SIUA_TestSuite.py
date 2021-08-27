import unittest
import Unittest_Login
import Login


class SIUA_TestSuite(unittest.TestCase):

    def test_SIUA_Smoke_Suite(self):
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Unittest_Login.Unittest_Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Unittest_Login.Unittest_Login)
        ])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)



if __name__ == "__main__":
    unittest.main()
