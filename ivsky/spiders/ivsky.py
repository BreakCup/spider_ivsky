# -*- encoding: utf-8 -*-
from ivsky.items import IvskyItem
import scrapy

class ivsky(scrapy.Spider):
    name = 'ivsky'

    start_urls = ['http://www.ivsky.com/bizhi/fengjing','http://www.ivsky.com/bizhi/dongman']
    baseUrl = 'http://www.ivsky.com'
    

    def parse(self,response):
        #获取图片地址
        pics = response.xpath('//ul[@class="ali"]/li/div/a')
        #下一页地址
        pageUrl = response.xpath('//div[@class="pagelist"]/a[@class="page-next"]/@href').extract()

        if pics:
            for pic in pics:
                picUrl = self.baseUrl + pic.xpath('@href').extract()[0]
                text = pic.xpath('@title').extract()[0]
                print('\n爬取到：',text,picUrl,'\n')
                yield scrapy.Request(picUrl, callback=self.getPic)
        if pageUrl:
            print('\n跳转下一页...\n')
            yield scrapy.Request(self.baseUrl+pageUrl[0],callback=self.parse)
    

    #组图页面
    def getPic(self,response):
        print('\n获取到图片组...\n')
        urls = response.xpath('//ul[@class="pli"]/li/div/a/@href').extract()
        for url in urls:
            _url = self.baseUrl + url
            yield scrapy.Request(_url, callback=self.savePic)


    #组图内单张图片页面，存在下载按钮，下载图片时，header的Referer设置带上该url
    def savePic(self,response):
        item = IvskyItem()
        #图片地址
        url = response.xpath('/*').re('<script.*?imgURL=\'(.*?)\'.*?</script>')
        #url = re.match(r'<a.*?class="bt-green".*?href="(.*?)".*?</a>',response.xpath('/*').extract())
        #图片名字
        name = response.xpath('//div[@id="al_tit"]/h1/text()').extract()
        #图片分类位置
        pos = response.xpath('//div[@class="pos"]/a/text()').extract()
        #图片分辨率
        resolution = response.xpath('//*[@id="pic_info"]/span[1]/text()').extract()
        #referer
        referer = response.url

        print('\n正在爬取{name}\n'.format(name=name[0]))
        for i in range(len(pos)):
            pos[i] = pos[i].replace('/','／') .replace('\\','＼')
        item['referer'] = referer
        item['url'] = self.baseUrl + url[0]
        item['name'] = name[0].replace('/','／') .replace('\\','＼')
        item['pos'] = '\\'.join(pos)
        item['resolution'] = resolution[0]
        return item


        