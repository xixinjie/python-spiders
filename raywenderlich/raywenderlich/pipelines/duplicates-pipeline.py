from scrapy.exceptions import DropItem

# 去重: 丢弃含有重复title的item


class DuplicatesPipeline(object):

    def __init__(self):
        self.titles_seen = set()

    def process_item(self, item, spider):
        if item['title'] in self.titles_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.titles_seen.add(item['title'])
            return item
