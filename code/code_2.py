<<<<<<< HEAD
import socket
import ssl

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

# ruleid:ssl-wrap-socket-is-deprecated
ssock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1)

# ruleid:ssl-wrap-socket-is-deprecated
ssock2 = ssl.wrap_socket(sock)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ok:ssl-wrap-socket-is-deprecated
ssl_sock = context.wrap_socket(s, server_hostname='www.verisign.com')
=======
import socket
import ssl

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

# ruleid:ssl-wrap-socket-is-deprecated
ssock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1)

# ruleid:ssl-wrap-socket-is-deprecated
ssock2 = ssl.wrap_socket(sock)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ok:ssl-wrap-socket-is-deprecated
ssl_sock = context.wrap_socket(s, server_hostname='www.verisign.com')
>>>>>>> 4568c2435b8367fca9bbe02afc2078287c266144
ssl_sock.connect(('www.verisign.com', 443))