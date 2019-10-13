import urllib,json
from .models import News, Sources

# getting api key

api_key = None

# getting the news base url

base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets json response to our url request
    '''

    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response["articles"]:
            news_results_list = get_news_response["articles"]
            news_results = process_results(news_results_list)

    return news_results
def search_news(topic):
    '''
    Function to search for news by topic
    '''
    
    search_news_url = "https://newsapi.org/v2/everything?q={}&apiKey={}".format(topic, api_key)
    
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)
        
        search_news_results = None
        if search_news_response["articles"]:
            search_news_list = search_news_response["articles"]
            search_news_results = process_results(search_news_list)
    
    return search_news_results

