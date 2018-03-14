
import helloworld

from tornado.escape import to_unicode
from tornado.testing import AsyncHTTPTestCase, gen_test
from tornado.httpclient import HTTPError


class HelloWorldTest(AsyncHTTPTestCase):
    def setUp(self):
        super().setUp()
        print("setup")

    def get_app(self):
        return helloworld.app

    @gen_test(timeout=10)
    def test_helloworld(self):
        response = yield self.http_client.fetch(self.get_url('/'))
        self.assertEqual(to_unicode(response.body), "Hello, world")

    @gen_test
    def test_404(self):
        with self.assertRaises(HTTPError) as cm:
            yield self.http_client.fetch(self.get_url('/hogehoge'))
        self.assertEqual(cm.exception.code, 404)

    def tearDown(self):
        print("teardown")
        super().tearDown()

if __name__ == "__main__":
    tornado.testing.main()
