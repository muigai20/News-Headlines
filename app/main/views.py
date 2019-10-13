from flask import render_template, request, redirect, url_for



@main.route("/")
def index():
    '''
    View root page function that returns the index page and its data
    '''
    top_headlines = get_news("top-headlines")

    title = "News headlines"
    return render_template("index.html", title = title, top=top_headlines)

@main.route("/search/<news_name>")
def search(news_name):
    '''
    function to display the search results
    '''
    return render_template("search.html", news = searched_news)

@main.route("/sources")
def source():
    '''
    view function to display sources of news
    '''
    source = sources_news()
    return render_template("sources.html", source = source)