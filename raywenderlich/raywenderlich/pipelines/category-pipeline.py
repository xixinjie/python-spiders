# 字段处理: 删除 item 的 category 字段中的 '\t' 和 '\n'


class ArticleCategoryPipeline(object):

    vat_factor = 1.15

    def process_item(self, item, spider):
        item['category'] = item['category'].replace("\n", "").replace("\t", "")
        return item
