import urllib.request
import json
from .models import sources, Articles

# Getting the API KEY
api_key = None

# Getting the news base url
base_url = None
def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
def get_sources(sources):
    '''
    Fuction to retrieve news sources list from the News api_key
    '''
    get_sources_url = base_url.format(sources, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    Fuction that process the results list and transform them into a list of objects
    Args:
        sources_list: A list of dictionariesthat contains news sources details
    returns:
        sources_list: a list of news sources objects
    '''

    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        source_object = Sources(id, name, description, url, category)
        sources_results.append(source_object)
    return sources_results
