# 必要モジュールを import
import tornado.testing
import tornado.web
import mock
import urllib
from tornado.httpclient import HTTPRequest

# ヘルパー関数
def urlencode_request_params(**params):
    return urllib.urlencode(
        dict(
            [k, v.encode("utf-8") if isinstance(v, unicode) else v]
            for k, v in params.items()
        )
    )

def prepare_kwargs(**params):
    kwargs = dict(
        body=urlencode_request_params(**params),
    )
    return kwargs

# サンプルハンドラー
class ProfileHandler(tornado.web.RequestHandler):
    """get method を試すためのもの
    """
    def get(self):
        user_id = self.get_argument("user_id")
        if user_id != "tornadoweb":
            raise tornado.web.HTTPError(404)
        self.finish("ok")

class AccountHandler(tornado.web.RequestHandler):
    """tornado.web.authenticated デコレーターを使う場合のテストを
    するためのもの
    """
    @tornado.web.authenticated
    def get(self):
        self.finish("I'm " + self.current_user)

    @tornado.web.authenticated
    def post(self):
        bio = self.get_argument("bio")
        self.finish("{error:0, msg:{bio:%s}}" % bio)

class TestSample(tornado.testing.AsyncHTTPTestCase):
    """AsyncHTTPTestCase を継承してHTTP Serverを起動
    """
    def setUp(self):
        """super クラスで空きのポートを探し get_app に登録されている
        handler を Application として Tornado を起動している

        self.http_clientが準備されていて、self.http_client.fetch()
        を使うこともできる
        """
        super(TestSample, self).setUp()

    def get_httpserver_options(self):
        """HTTPサーバー起動時のオプションを指定することもできる
        """
        return {}

    def get_app(self):
        """アプリケーションのハンドラーのルーティングの設定を行う。
        アプリケーションの設定があれば、ここで指定することができる。
        """
        application_settings = dict()
        return tornado.web.Application([
            ("/profile", ProfileHandler),
            ("/account", AccountHandler),
            ("/account/update", AccountHandler),
        ], **application_settings)

    def test_httprequest_sample(self):
        """HTTPRequestを使って直接リクエストを投げることもできるのでお試しテスト
        """
        kwargs = dict()
        test_url = 'http://snapdish.co'
        request = HTTPRequest(test_url, **kwargs)
        self.http_client.fetch(request, self.stop, **kwargs)
        response = self.wait()
        self.assertEqual(response.code, 200)

    def test_profile(self):
        """プロフィールが正常に取得できているかのテスト
        """
        kwargs = dict(
            user_id="tornadoweb"
        )
        path = "%s?%s" % ("/profile", urlencode_request_params(**kwargs))
        response = self.fetch(path)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, "ok")

    def test_profile_404(self):
        """プロフィールのリクエストが間違っている場合404を返してるかのテスト
        """
        kwargs = dict(
            user_id="tornadoweb?"
        )
        path = "%s?%s" % ("/profile", urlencode_request_params(**kwargs))
        response = self.fetch(path)
        self.assertEqual(response.code, 404)

    def test_account(self):
        """authenticatedのデコレーターが使われている時、mock を使って
        current_user に修正を加える必要がある"""
        with mock.patch.object(AccountHandler, 'get_current_user') as m:
            m.return_value = "tornadoweb"
            path = "/account"
            response = self.fetch(path)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, "I'm tornadoweb")

    def test_account_update(self):
        """authenticatedのデコレーターが使われている時、mock を使って
        current_user に修正を加える必要がある"""
        with mock.patch.object(AccountHandler, 'get_current_user') as m:
            m.return_value = "tornadoweb"
            bio = "tornadoweb bio"
            params = dict(bio=bio)
            response = self.fetch("/account/update",
                                  method="POST",
                                  follow_redirects=False,
                                  body=urlencode_request_params(**params))
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, "{error:0, msg:{bio:%s}}" % bio)

if __name__ == "__main__":
    tornado.testing.main()
