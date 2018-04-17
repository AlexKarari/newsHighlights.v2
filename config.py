import os


class Config:
    pass

    NEWS_ARTICLE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}''
    NEWS_SOURCES_URL ='https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # 'https://newsapi.org/v1/sources?apiKey='


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
