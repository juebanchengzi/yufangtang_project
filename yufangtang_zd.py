# -*- coding: gbk -*-
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
import wordSegmentation_pb2_grpc
import wordSegmentation_pb2


class ZD(object):
    def __init__(self,response):
        self.response=response

    def word(self):
        atomic_len = len(self.response.arr_atomic.infoarr)
        compound_len = len(self.response.arr_compound.infoarr)
        response_atomic = self.response.arr_atomic
        response_compound = self.response.arr_compound
        compound_pos_list = []
        dict_compound = {}
        for i in range(compound_len):
            compound_pos_list.append(response_compound.infoarr[i].pos_)
        zfc=''
        if len(compound_pos_list) == 0:
            zfc=zfc
        else:
            try:
                for i in range(compound_pos_list[0],compound_pos_list[1]):
                    zfc = zfc+str(response_atomic.infoarr[i].wordContent).strip()
                zfc=zfc.replace(':','').replace('临床诊断','')
            except IndexError:
                for i in range(compound_pos_list[0],atomic_len):
                    zfc = zfc+str(response_atomic.infoarr[i].wordContent).strip()
                zfc = zfc.replace(':', '').replace('临床诊断', '')
        dict_compound['zd'] = zfc
        dict_json = json.dumps(dict_compound, ensure_ascii=False)
        f = open('test_2.txt', 'w')
        f.write(dict_json)





