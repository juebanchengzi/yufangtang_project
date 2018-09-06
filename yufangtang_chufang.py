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


class CF(object):
    def __init__(self,response):
        self.response=response

    def jiexi(self):
        automic_list_len = len(self.response.arr_atomic.infoarr)
        compound_list_len = len(self.response.arr_compound.infoarr)
        automic_g=self.response.arr_atomic
        automic_g_list = []
        automic_chufang_list = []
        jiliang_list_1 = []
        jiliang_list = []
        jl = []
        for i in range(automic_list_len):
            if automic_g.infoarr[i].wordContent == '剂':
                jl.append(automic_g.infoarr[i-1].wordContent)
                break
        for m in range(automic_list_len):
            if automic_g.infoarr[m].wordContent == 'g':
                automic_g_list.append(automic_g.infoarr[m].pos_)
                jiliang_list_1.append(automic_g.infoarr[m].pos_-1)
        for i in range(automic_list_len):
            for j in jiliang_list_1:
                if automic_g.infoarr[i].pos_ == j:
                    jiliang_list.append(automic_g.infoarr[i].wordContent)
        automic_chufang_list.append([0,automic_g_list[0]-2])
        for i in range(len(automic_g_list)):
            list_1 = []
            if i<len(automic_g_list)-1:
                list_1.append(automic_g_list[i])
                list_1.append(automic_g_list[i+1]-2)
                automic_chufang_list.append(list_1)
        list_new = []
        for k in range(len(automic_chufang_list)):
            list_new.append('str' + str(k))
        return automic_chufang_list,list_new,jiliang_list,jl

    def result_cf(self):
        list_all,list_new,jiliang_list,jl=self.jiexi()
        cont = 0
        for item in list_all:
            space = item[1] - item[0]
            first = item[0]
            list_new[cont] = ''
            for i in range(space):
                list_new[cont] = list_new[cont] + str(self.response.arr_atomic.infoarr[first].wordContent).strip()
                first = first + 1
            cont = cont + 1
        for item in list_new:
            if 'R' in item:
                list_new[list_new.index(item)]=item.replace('R','')
        list_compound = []
        for i in range(len(self.response.arr_compound.infoarr)):
            list_compound.append(self.response.arr_compound.infoarr[i].wordContent)
        cfy_no_list = []   #库中没有的药品
        for j in list_new:
            # print(j)
            if j in list_compound:
                continue
            else:
                cfy_no_list.append(j)
        dict_total = {}
        yf = []
        id = []
        for i in range(len(list_new)):
            id.append(i+1)
        for i in range(len(list_new)):
            dict_little = {}
            dict_little['id'] = id[i]
            dict_little['name'] = list_new[i]
            dict_little['jl'] = jiliang_list[i]
            yf.append(dict_little)
        dict_total['yf'] = yf
        dict_total['jl'] = jl
        dict_json = json.dumps(dict_total, ensure_ascii=False)
        f = open('test_3.txt', 'w')
        f.write(dict_json)























