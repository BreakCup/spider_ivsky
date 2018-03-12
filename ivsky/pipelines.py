# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib
import os

class IvskyPipeline(object):
    #图片保存目录
    basePath = '.\jpg\\'
    def process_item(self, item, spider):
        #header参数
        user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36"
        referer = item['referer']
        header = {
            'user_agent':user_agent,
            'Referer':referer
        }
        #图片地址
        url = item['url']
        #图片名字
        name = item['name']
        #图片保存地址
        path = self.basePath + item['pos']
        
        
        if not os.path.exists( path = path + '\\{name}.jpg'.format(name=name) ):
            #如果不存在图片文件
            if not os.path.exists(path):
                #如果不存在图片位置的目录，则创建目录
                os.makedirs(path)
            print('\n### 正在保存{name} ###\n'.format(name=name))
            jpg = open(path+'\\{name}.jpg'.format(name=name),'wb')
            request = urllib.request.Request(url,headers=header)
            response = urllib.request.urlopen(request)
            jpg.write(response.read())
            jpg.close()
        else:
            #如果已经存在图片文件
            print('\n### {name} 已经存在  ###\n'.format(name=name))
        
        return item
