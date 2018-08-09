from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from raywenderlich.middlewares.resources import USER_AGENTS
import random


class RandomUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', ua)
