def wsgi_app(environ, start_response):

    from view import api, hello
    application = Flask(__name__)
    modules_define = [api.app, hello.app]
    for app in modules_define:
        application.register_blueprint(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
