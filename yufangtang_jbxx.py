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
import yaml
import wordSegmentation_pb2_grpc
import wordSegmentation_pb2

class Jiexi(object):
    def __init__(self,response,dzcf):
        self.dzcf=dzcf
        self.response=response

    # def yaml_config(self):
    #     f=open('config.yaml_file')
    #     content=yaml_file.load(f)
    #     localhost=content['localhost']
    #     dzcf=content['dzcf']
    #     return localhost,dzcf


    def len_word(self):
        compound_len=len(self.response.arr_compound.infoarr)
        atomic_len=len(self.response.arr_atomic.infoarr)
        return atomic_len,compound_len

    def get_compound_pos(self):
        automic_len,compound_len=self.len_word()  # return zhe length of compound_word
        for i in range(compound_len):
            if self.response.arr_compound.infoarr[i].finger_key==self.dzcf[3]:
                year_pos=self.response.arr_compound.infoarr[i].pos_-1
            elif self.response.arr_compound.infoarr[i].finger_key==self.dzcf[5]:
                day_pos=self.response.arr_compound.infoarr[i].pos_+1
            elif self.response.arr_compound.infoarr[i].finger_key==self.dzcf[6]:
                feiyong_pos=self.response.arr_compound.infoarr[i].pos_
        compound_pos=[]
        for i in range(compound_len):
            compound_pos.append(self.response.arr_compound.infoarr[i].pos_)
        for i in range(len(compound_pos)):
            if year_pos>compound_pos[i] and year_pos<compound_pos[i+1]:
                compound_pos.insert(i+1,year_pos)
                y_index=i+2
            elif day_pos>compound_pos[i] and day_pos<compound_pos[i+1]:
                compound_pos.insert(i+1,day_pos)
                d_index=i+1
        compound_o=compound_pos[y_index:d_index]
        for i in compound_o:
            compound_pos.remove(i)
        compound_pos.remove(feiyong_pos)
        return compound_pos

    def get_pos_atomic_content(self):
        list=self.get_compound_pos()
        automic_len, compound_len = self.len_word()
        list_all=[]
        M=0
        while M<len(list)-1:
            list_all.append(list[M:M+2])
            M=M+1
        list_new=[]
        automic_last=list_all[-1][-1]
        list_all.append([automic_last,automic_len])
        for k in range(len(list)):
            list_new.append('str'+str(k))
        return list_all,list_new

    '''
    return the result
    '''
    def get_text_content(self):
        list_all,list_new=self.get_pos_atomic_content()
        cont=0
        for item in list_all:
            space=item[1]-item[0]
            first=item[0]
            list_new[cont]=''
            for i in range(space):
                list_new[cont]=list_new[cont]+str(self.response.arr_atomic.infoarr[first].wordContent).strip()
                first=first+1
            cont=cont+1
        list_new[0]=list_new[0].replace('处方','')
        list_key=['mzh','bh','kb','date','fb','name','sex','age','jkdah','blh']
        dict_total=dict(zip(list_key,list_new))
        dict_json = json.dumps(dict_total, ensure_ascii=False)
        f = open('test_1.txt', 'w')
        f.write(dict_json)


