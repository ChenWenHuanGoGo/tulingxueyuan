import scrapy
from douban.items import DoubanItem

class DouBanSpider(scrapy.Spider):
    #爬虫名字唯一，不能与项目名相同
    name = "doubanwang"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]
    def parse(self,response):
        sites = response.xpath('//div[@class="article"]/ol/li')
        item = DoubanItem()
        for each in sites:
            # 一定要加一个.    在win下不用加
            item["serial_number"] = each.xpath('.//div[@class="pic"]/em/text()').extract_first()
            item["movie_name"] = each.xpath('.//a[@class=""]/span[1]/text()').extract_first()
            a = each.xpath('.//div[@class="info"]/div[@class="bd"]/p[@class=""]/text()').extract()
            # a是由两个元素的列表，把这两个元素合在一起
            a_content = "".join(a[0].split()) +  "".join(a[1].split())
            item["introduce"] = a_content
            item["star"] = each.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()').extract_first()
            item["evaluate"] = each.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract_first().split("人")[0]
            item["describe"] = each.xpath('.//div[@class="info"]/div[@class="bd"]//span[@class="inq"]/text()').extract_first()
            yield item

        next_link = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_link:
            #next_link是一个列表
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+str(next_link),callback=self.parse)


