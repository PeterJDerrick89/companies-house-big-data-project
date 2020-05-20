import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy.item import Item, Field
from scrapy.http import Request, Response

from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
import requests

class MyItem(Item):
    file_urls = Field()
    files = Field()

class XBRLSpider(CrawlSpider):

    name = "xbrl_scraper"

    # custom_settings = {
    #      'ITEM_PIPELINES' : {'scrapy.pipelines.files.FilesPipeline': 1},
    #      'FILES_STORE' : "/shares/data/20200519_companies_house_accounts/xbrl_scraped_data_testing/"
    # }

    allowed_domains = ['download.companieshouse.gov.uk/en_accountsdata.html']
    start_urls = ['http://download.companieshouse.gov.uk/en_accountsdata.html']

    filepath = "/shares/data/20200519_companies_house_accounts/xbrl_scraped_data_testing/"

    def parse(self, response):

        links = response.xpath('//body//a/@href').extract()

        # Trim out links which do not point to zip files
        links = [link for link in links if link.split('.')[-1] == "zip"]

        for link in links:

            link = response.urljoin(link)

            #item = MyItem(file_urls=['http://download.companieshouse.gov.uk/Accounts_Bulk_Data-2020-05-19.zip'])
            item = MyItem(file_urls=[link])

            #print("1")
            #print(item)
            #print("2")

            yield item

    # def parse(self, response):
    #
    #     print("hello")
    #
    #     links = response.xpath('//body//a/@href').extract()
    #
    #     # Trim out links which do not point to zip files
    #     links = [link for link in links if link.split('.')[-1] == "zip"]
    #
    #     #print(links)
    #
    #     for link in range(0, len(links)):
    #
    #         links[link] = response.urljoin(links[link])
    #
    #     #links = [links[0]]
    #
    #     print(links)
    #     links = [links[0]]
    #     print(links)
    #
    #     #filepath = "/shares/data/20200519_companies_house_accounts/xbrl_scraped_data_testing/"
    #     filename = self.filepath + "test.zip"
    #
    #     # r = Request(links[0])
    #     # with open(filename, "wb") as f:
    #     #     f.write(r.body)
    #
    #     #r = requests.get(links[0])
    #
    #     r = Response.follow(self, url=links)
    #
    #     #print(r)
    #
    #     # with open(filename, "wb") as f:
    #     #     f.write(r.content)
    #
    #     print("Reached here")
    #
    #     item = MyItem()
    #     item['file_urls'] = links[0]
    #
    #     return item

# class MyFilesPipeline(FilesPipeline):
# #
#     def file_path(self, request, response=None, info=None):
#
# #
#         print("Here")
# #
# #         print('files/' + os.path.basename(urlparse(request.url).path))
# #
# #         return None
# #
#     def get_media_requests(self, item, info):
#         print("Hello")
#
#         for file_url in item['file_urls']:
#             print("Hello")
#             print(file_url)
# #             yield Request(file_url)