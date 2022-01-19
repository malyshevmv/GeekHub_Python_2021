# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3 as sq
from .year_month_day import date


class BotPipeline:
    def __init__(self):
        self.con = sq.connect(f'{date}.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS news (
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            tags TEXT NOT NULL,
            url TEXT NOT NULL
            )''')

    def process_item(self, item, spider):
        self.cur.execute('''INSERT INTO news (title, text, tags, url)
            VALUES (?, ?, ?, ?)''', (str(item['title']), str(item['text']), str(item['tags']), str(item['url'])))
        self.con.commit()
        return item
