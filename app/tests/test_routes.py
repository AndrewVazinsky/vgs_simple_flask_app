from app import app
import unittest


class VGSFlaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self) -> None:
        pass

    def test_index_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_add_cc_info_status_code(self):
        with app.test_client() as cl:
            payload = {'cc_number': '1010202030304040', 'exp_date': '02/22', 'cvv': '123'}
            result = cl.post('https://tntfjvtrllv.sandbox.verygoodproxy.com/add_cc_info')
        yield cl
        self.assertEqual(result.status_code, 200)

    def test_forward_status_code(self):
        with app.test_client() as cl:
            payload = {'cc_number': 'tok_sandbox_frgx6dRxG17gciPbkGsdAo',
                       'exp_date': 'tok_sandbox_4iuvywUpQD4qGaKZv9UuJP',
                       'cvv': 'tok_sandbox_sFMko27Hy8zJUAEUxjDn2m'}
            result = cl.post('/forward', data=payload)
        yield cl
        self.assertEqual(result.status_code, 200)

    def test_add_cc_info_status_code_no_input(self):
        with app.test_client() as cl:
            payload = {'cc_number': None, 'exp_date': None, 'cvv': None}
            result = cl.post('https://tntfjvtrllv.sandbox.verygoodproxy.com/add_cc_info')
        yield cl
        self.assertEqual(result.status_code, 200)

    def test_forward_status_code_no_input(self):
        with app.test_client() as cl:
            payload = {'cc_number': None, 'exp_date': None, 'cvv': None}
            result = cl.post('/forward', data=payload)
        yield cl
        self.assertEqual(result.status_code, 200)
