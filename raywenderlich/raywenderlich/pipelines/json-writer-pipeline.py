import json


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('articles.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
