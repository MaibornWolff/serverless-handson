#!/usr/bin/env python3
import argparse
from urllib.parse import parse_qs
import json
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys
from multiprocessing import Process

sys.path.insert(0, ".")
from monolith_app import MyApp

HOST_NAME = 'localhost'
PORT_NUMBER = 9000


class Server(BaseHTTPRequestHandler):

    def do_GET(self):

        paths = {
            '/brightness':   {'func': MyApp.brightness, 'data': {}},
            '/wind':         {'func': MyApp.wind, 'data': {}}
        }

        if self.get_path_only() in paths:
            self.respond(paths[self.get_path_only()])
        else:
            self.respond({'statusCode': 500})

    def get_path_only(self):
        path_parts = self.path.split("?")
        return path_parts[0]

    def get_query_only(self):
        path_parts = self.path.split("?")
        if len(path_parts) > 1:
            return path_parts[1]
        else:
            return {}

    def parse_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        postvars = self.rfile.read(content_length)
        res = postvars.decode("utf-8")
        if res == "":
            return {}
        else:
            return json.loads(res)

    def handle_http(self, content):
        self.send_response(content['statusCode'])
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        return bytes(content['body'], 'UTF-8')

    def handle_error(self):
        self.send_response(500)
        self.end_headers()
        content = "ERROR!"
        return bytes(content, 'UTF-8')

    def respond(self, opts):
        if opts.get('statusCode') != 500:
            request = {
                'request_version': self.request_version,
                'request_line': self.requestline,
                'path': self.get_path_only(),
                'query': parse_qs(self.get_query_only()),
                'command': self.command,
                'data': opts.get('data')
            }

            handler_response = opts['func'](MyApp(), request)
            response = self.handle_http(handler_response)

        else:
            response = self.handle_error()

        self.wfile.write(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start a monolith http server')
    parser.add_argument("--test-mode", action='store_true', help="starting only for 2 secs")
    args = parser.parse_args()

    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), Server)
    print('Server Started - %s:%s' % (HOST_NAME, PORT_NUMBER))
    print('APIs available:')
    print('http://%s:%s/brightness' % (HOST_NAME, PORT_NUMBER))
    print('http://%s:%s/wind' % (HOST_NAME, PORT_NUMBER))

    action_process = Process(target=httpd.serve_forever)

    try:
        action_process.start()

        if args.test_mode:
            action_process.join(timeout=2)
        else:
            httpd.serve_forever()

    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server Stoped - %s:%s' % (HOST_NAME, PORT_NUMBER))
    action_process.terminate()
