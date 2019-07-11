# coding = utf-8

from socket import *

sk = socket(AF_INET, SOCK_STREAM)

sk.bind(('127.0.0.1', 33333)
sk.listen(9)
cs = sk._accept()
cs.recv()

cs.close()
sk.close()

