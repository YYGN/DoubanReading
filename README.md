# DoubanReading
抓取豆瓣阅读所有标签下的评分人数在两千人以上且评分在8.0分以上的书籍信息。
主要还是用了scrapy框架，采用了随机头部信息中间件和代理中间件，本次采用的代理是xx-net提供的代理，网上找的免费代理太不靠谱了，几乎是不能用的。
最后还是存储到MONGODB中。
豆瓣阅读网站还好，没有把信息隐藏起来，不过就是对浏览器头和IP限制比较严重，网站结构也清晰，所有的标签下都是同样的网页框架，所以写起来很容易，只需要写一个就可以了。
<hr>

更新时间：2018年03月14日

修改了随机代理和随机头的机制，改正了一处逻辑错误，谢谢@shcalm指出的错误。随机代理使用了[https://github.com/Python3WebSpider/ProxyPool](https://github.com/Python3WebSpider/ProxyPool)的项目，加上了爬取限制，目前还没有出现错误～～