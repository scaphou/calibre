#!/usr/bin/env  python

__license__   = 'GPL v3'
__copyright__ = '2009, Darko Miletic <darko.miletic at gmail.com>'
'''
www.uncrate.com
'''

from calibre.web.feeds.recipes import BasicNewsRecipe
from calibre.ebooks.BeautifulSoup import BeautifulSoup, Tag

class Uncrate(BasicNewsRecipe):
    title                  = 'Uncrate'
    __author__             = 'Darko Miletic'
    description            = 'Uncrate is a web magazine for guys who love stuff. Our team digs up the best gadgets, clothes, cars, DVDs and more. New items are posted daily. Enjoy responsively.'
    oldest_article         = 7
    max_articles_per_feed  = 100
    no_stylesheets         = True
    use_embedded_content   = False
    encoding               = 'utf-8'
    publisher              = 'Zombie corp.'
    category               = 'news, gadgets, clothes, cars, DVDs'
    lang                   = 'en-US'
    language               = _('English')
    
    html2lrf_options = [
                          '--comment', description
                        , '--category', category
                        , '--publisher', publisher
                        ]
    
    html2epub_options = 'publisher="' + publisher + '"\ncomments="' + description + '"\ntags="' + category + '"' 

    keep_only_tags = [dict(name='div', attrs={'class':'lefttext'})]
    remove_tags_after = dict(name='div', attrs={'class':'serif'})
    remove_tags = [dict(name=['object','link','script','iframe','form'])]
    
    feeds = [(u'Articles', u'http://feeds.feedburner.com/uncrate')]

    def preprocess_html(self, soup):
        mlang = Tag(soup,'meta',[("http-equiv","Content-Language"),("content",self.lang)])
        mcharset = Tag(soup,'meta',[("http-equiv","Content-Type"),("content","text/html; charset=utf-8")])
        soup.head.insert(0,mlang)
        soup.head.insert(1,mcharset)          
        for item in soup.findAll(style=True):
            del item['style']
        return self.adeify_images(soup)
