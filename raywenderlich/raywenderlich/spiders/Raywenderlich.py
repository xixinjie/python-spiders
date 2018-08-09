# -*- coding: utf-8 -*-
import scrapy


class RaywenderlichSpider(scrapy.Spider):
    name = 'Raywenderlich'
    allowed_domains = ['raywenderlich.com']
    start_urls = ['http://raywenderlich.com/page/1']

    def parse(self, response):
        for article in response.css('article'):
            yield {
                'title': article.css('h2.entry-title a::text').extract_first(),
                'href': article.css('h2.entry-title a::attr(href)').extract_first(),
                'author': article.css('div.author-meta a.author-name::text').extract_first(),
                'date': article.css('div.author-meta span.author-post-date::text').extract_first(),
                'overview': article.css('div.entry-content p::text').extract_first(),
                'category': article.css('li.category::text').extract_first(),
            }

        next_page = response.css(
            'div.wp-pagenavi a.nextpostslink::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            self.log('Found next page: %s' % next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            self.log('Completed.')
