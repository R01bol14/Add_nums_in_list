import unittest

from . import app


class BasicTests(unittest.TestCase):

    ###########################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        self.app = app.cal()

    # executed after each test
    def tearDown(self):
        pass

    def total_cal(self):
        return self.app.post(
            '/total',
            data=dict(list_item=range(10000001)),
            follow_redirects=True
        )

    ###############
    #### tests ####
    ###############

    def test_cal_completes_successfully(self):
        response = self.total_cal()
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
