# -*- coding:utf-8 -*-
from __future__ import print_function
import grpc
import time
import scmddzcf_pb2
import scmddzcf_pb2_grpc

def run():
    channel=grpc.insecure_channel('localhost:50059')
    client=scmddzcf_pb2_grpc.DataStub(channel)
    response=client.TextDzcf(scmddzcf_pb2.ImagePath(path='./img1.jpg'))
    print('return the text'+response.data_json)

if __name__=='__main__':
    run()




























