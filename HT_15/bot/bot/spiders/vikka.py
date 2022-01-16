import scrapy
from ..year_month_day import year, month, day


class VikkaSpider(scrapy.Spider):
    name = 'vikka'
    start_urls = []
    main_url = 'https://www.vikka.ua/'
    date = f'{year}/{int(month):02}/{int(day):02}/'
    start_urls.append(main_url + date)

    def parse(self, response):
        """збираємо урли новин на вибраній сторінці"""
        url_new = response.css('h2.title-cat-post a::attr(href)').getall()
        yield from response.follow_all(url_new, self.parse_new)

    def parse_new(self, response):
        """збираємо потрібну інформацію зі сторінки"""
        tags_raw = response.css('a.post-tag::text').getall()
        tags = []
        for i in tags_raw:
            tags.append('#' + i)
        inf = {
            'title': response.css('h1.post-title.-margin-b::text').get().strip(),
            'text_list': response.css('p::text').getall(),
            'tag_list': tags,
        }
        yield inf
