from datetime import datetime
from elasticsearch import Elasticsearch
from django.http import JsonResponse
es = Elasticsearch("http://localhost:9200")

# Parameter 'words' should be single string of keywords separated by single spaces
def search(words):
    es.indices.refresh(index="recs")

    return es.search(index="recs", body={ #perform sample search
        "query": {
            "multi_match": {
                "query": words,
                "fields": ["title", "instructions", "ingredients"],
                "operator": "or"
                }
            }
        })['hits']['hits']