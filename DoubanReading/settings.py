# -*- coding: utf-8 -*-

# Scrapy settings for DoubanReading project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DoubanReading'

SPIDER_MODULES = ['DoubanReading.spiders']
NEWSPIDER_MODULE = 'DoubanReading.spiders'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'doubanreading'
HOST = 'localhost'
PORT = 6379
PASSWORD = '1989.zzZ'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DoubanReading (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'bid=dh4MdNsC0rk; ll="108309"; _ga=GA1.2.421651830.1516264413; push_doumail_num=0; __utmv=30149280.15179; gr_user_id=981bf643-c187-4c07-a721-9ed9fa21e95c; _vwo_uuid_v2=5B7D522B6C7BE62DF55DCE8A49A5F6DB|1e651c1a4bd8ff125f4143f5c8e83f44; push_noty_num=0; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1517204379,1517279593; ap=1; viewed="26698660_25862578"; ps=y; ue="gu81037@gmail.com"; dbcl2="151795893:y1i++vnvn18"; ck=j6au; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1517569401%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fredir%3Dhttps%253A%252F%252Fbook.douban.com%252Ftag%252F%253Fview%253Dtype%2526icn%253Dindex-sorttags-all%22%5D; _pk_id.100001.3ac3=9fc50b00416a733e.1517203553.8.1517569401.1517566215.; _pk_ses.100001.3ac3=*; __utma=30149280.421651830.1516264413.1517553448.1517569401.11; __utmc=30149280; __utmz=30149280.1517569401.11.8.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; __utmt_douban=1; __utmb=30149280.1.10.1517569401; __utma=81379588.421651830.1516264413.1517560306.1517569402.6; __utmc=81379588; __utmz=81379588.1517569402.6.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; __utmt=1; __utmb=81379588.1.10.1517569402'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DoubanReading.middlewares.DoubanreadingSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'DoubanReading.middlewares.RandomUaMiddleware': 100,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'DoubanReading.middlewares.ProxyMiddleware': 200,
'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware':500,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'DoubanReading.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DOWNLOAD_TIMEOUT = 200