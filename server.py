
import requests
import http.server

patterns = ["uis", "lus", "lys"]
address='https://api.telegram.org/bot234875332:AAEtMhP4y8s4MhD68iCbznBTdRqYbo8rroI'

   
class MyHandler(http.server.BaseHTTPRequestHandler):
   def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
   def do_POST(self):
        self.send_response(200)
        print('got_it')
        print(self.headers)
        get_body = self.rfile.read(int(self.headers['Content-Length']))
        for i in get_body:
            print(i)
        #sendReq(); 


def serve():
    server =http.server.HTTPServer(('', 5000), MyHandler)
    print('serviiing')
    server.serve_forever()

def sendReq(data):
    payload = {'text': data, 'chat_id': 246571056}
    req = requests.get(address + '/' + 'sendMessage', params=payload)
