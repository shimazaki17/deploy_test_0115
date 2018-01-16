def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = 'Hello World'
    yield response_body.encode()

    from flask import Flask
    from view import api, 0113_input
    application = Flask(__name__)
    modules_define = [api.app, 0113_input.app]
    for app in modules_define:
        application.register_blueprint(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
