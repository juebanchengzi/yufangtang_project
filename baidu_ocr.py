# -*- coding:gbk -*-
from aip import AipOcr

class BD(object):
    def __init__(self):
        pass
    def get_file_content(self,filepath):
        with open(filepath, 'rb') as fp:
            return fp.read()

    def baiduocr(self,image_path):
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
        result = aipOcr.basicAccurate(self.get_file_content(image_path), options)
        if result.get('words_result_num', 0) > 0:
            for obj in result['words_result']:
                content += obj['words']
                content += '\n'
        return content