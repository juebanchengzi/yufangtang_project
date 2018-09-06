# -*- coding:utf-8 -*-
from concurrent import futures
import collections
import cv2
import numpy as np
import math
import os
from aip import AipOcr
import chardet
import re
import json
import chardet
import grpc
import time
import scmddzcf_pb2
import scmddzcf_pb2_grpc

_ONE_DAY_IN_SECONDS=60*60*24


class BaiduOCR(object):
    def __init__(self,image_path):
        self.image_path=image_path

    def get_file_content(self,filepath):
        with open(filepath, 'rb') as fp:
            return fp.read()
    def baiduocr(self):
        APP_ID = '10073324'
        API_KEY = 'zapROApDpKIY2xGF4LXwUTj4'
        SECRET_KEY = 'Zx3S7lMIqaU3nl4b7X59A1FXGCQYdS8G'

        aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        options = {}
        options["recognize_granularity"] = "big"
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["vertexes_location"] = "true"
        options["probability"] = "true"

        content = ''
        result = aipOcr.basicAccurate(self.get_file_content(self.image_path), options)
        if result.get('words_result_num', 0) > 0:
            for obj in result['words_result']:
                content += obj['words']
                content += '\n'
        return content

class Dzcf(scmddzcf_pb2_grpc.DataServicer):
    def TextDzcf(self, request, context):
        bd=BaiduOCR(request.path)
        return scmddzcf_pb2.Jsondata(data_json=bd.baiduocr())

def server():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    scmddzcf_pb2_grpc.add_DataServicer_to_server(Dzcf(),server)
    server.add_insecure_port('[::]:50059')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

if __name__=='__main__':
    server()

