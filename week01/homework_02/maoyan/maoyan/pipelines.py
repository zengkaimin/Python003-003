# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_date = item['movie_date']
        output = f'|{movie_name}|\t|{movie_type}|\t|{movie_date}|\n\n'
        with open('./maoyan_top_10_movie.csv', 'a+', encoding= 'utf-8') as article:
            article.write(output)
        return item
