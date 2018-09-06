# -*-coding: gbk -*-
from __future__ import print_function
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
import yaml
import wordSegmentation_pb2_grpc
import wordSegmentation_pb2
import yufangtang_seg
from baidu_ocr import BD
from yufangtang_jbxx import Jiexi
from yufangtang_zd import ZD
from yufangtang_chufang import CF


def yaml_config():
        f=open('config.yaml_file')
        content=yaml.load(f)
        localhost=content['localhost']
        dzcf=content['dzcf']
        return dzcf

def run(text):
    conn = grpc.insecure_channel('10.100.1.145:50063')
    client = wordSegmentation_pb2_grpc.TextWordSegmentationStub(channel=conn)
    response = client.Text2WordArr(wordSegmentation_pb2.TextSource(text_s=text))
    return response


def main():
    yufangtang_seg.seg('./image/second.jpg')
    bd=BD()
    dzcf=yaml_config()

    text_1=bd.baiduocr('img1.jpg').encode('gbk')
    response_1=run(text_1)
    jbxx=Jiexi(response_1,dzcf)
    jbxx.get_text_content()

    text_2=bd.baiduocr('img2.jpg').encode('gbk')
    response_2=run(text_2)
    zd=ZD(response_2)
    zd.word()

    text_3=bd.baiduocr('img3.jpg').encode('gbk')
    response_3=run(text_3)
    cf=CF(response_3)
    cf.result_cf()

if __name__=='__main__':
    main()









