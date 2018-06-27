from concurrencytest import ConcurrentTestSuite, fork_for_tests

from unit_test_template import test_name, unittest

class unit_test_concurrency():
    def __init__(self, processing=3):
        self.processing = processing

    def unit_test(self):
        print("unit_test")
        unittest.main()

    def multi_processing(self):
        print("multi_processing")
        runner = unittest.TextTestRunner()
        suite = unittest.TestLoader().loadTestsFromTestCase(test_name)
        concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(self.processing))
        runner.run(concurrent_suite)


def main():
    utmp = unit_test_concurrency()
    utmp.multi_processing()

if __name__ == "__main__":
    main()
