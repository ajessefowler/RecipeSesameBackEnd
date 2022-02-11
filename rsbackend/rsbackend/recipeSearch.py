import string
import random
from datetime import datetime
from elasticsearch import Elasticsearch
from django.http import JsonResponse
es = Elasticsearch("http://localhost:9200")

def get_recipe_data(recipe):
    return recipe['_source']

# Parameter 'words' should be single string of keywords separated by single spaces
def search(words):
    es.indices.refresh(index="recs")

    results = es.search(index="recs", body={ #perform sample search
        "query": {
            "multi_match": {
                "query": words,
                "fields": ["title", "instructions", "ingredients"],
                "operator": "or"
                }
            }
        })['hits']['hits']

    return map(get_recipe_data, results) # Return only relevant recipe data

def random_recipes(amount):
    es.indices.refresh(index="recs")

    results = es.search(index="recs", body={
        "size": amount,
        "query": {
            "function_score": {
                "functions": [
                    {
                    "random_score": {
                        "seed": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))
                    }
                    }
                ]
            }
        }
    })['hits']['hits']

    return map(get_recipe_data, results)
        
