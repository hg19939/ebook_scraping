# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:13:05 2022

@author: hg19939
"""

from elasticsearch import Elasticsearch

csv_file = open("scraped_books.csv")
es = Elasticsearch("http://localhost:9200")

body = {
    "settings": {
       "analysis": {
         "analyzer": {
            "custom_analyzer": {
                "type": "custom",
                "tokenizer": "standard",
                "filter": ["lowercase", "stop", "porter_stem"]
                }
            }
        }
    },
    "mappings": {
        "book": {
            "properties": {
                "title": {
                    "type": "text"
                },
                "plot": {
                    "type": "text",
                    "analyzer": "custom_analyzer"
                },
                "link": {
                    "type": "keyword"
                }
            }    
        }
    }
}

es.indices.create(index="scraped_books_corpus", body=body)
es.bulk(csv_file, index="scraped_books_corpus", doc_type="book")
