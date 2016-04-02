#_*_coding:utf-8_*_

import socket
import StringIO
import sys

class WSGIServer(object):
    address_family = socket.AF_INET  #协议族AF_INET代表使用ipv4
    socket_type = socket.SOCK_STREAM  #socket类型
    request_queue_size = 1
    
    def __init__(self, server_address):
        #Create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        #Allow to reuse the same address
        listen_socket.setsocktop(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #bind
        listen_socket.bind(server_address)
        #Activate
        listen_socket.listen(self.request_queue_size)
        #Get server host port and name
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        #Return headers set by Web framework/Web application
        self.headers_set = []
        
    def set_app(self, appliacation):
        self.application = application