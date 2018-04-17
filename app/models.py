class Sources:
    '''
    Sources class to define News_sources Objects
    '''

    def __init__(self, source_id, source_name, description, url):
        self.source_id = source_id
        source_name = source_name
        self.description = description
        self.url = url


class Articles:
    '''
    Articles class to define News_articles Objects
    '''

    def __init__(self, source_id, author, title, description, url, urlToImage, publishedAt):
        self.source_id = source_id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
