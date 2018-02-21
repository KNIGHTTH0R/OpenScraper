
from controller import *
# from admin import AdminHandler


### all routing functions are in controller.py
urls = [
	# (r"/", MainHandler),
	# (r"/test", TestHandler),

	### main pages
	(r"/", MainHandler),
	(r"/recommended/", ContributorsHandler),
	(r"/edit/([0-9Xx\-]+)", ContributorEditHandler),
	(r"/add", ContributorEditHandler),

	(r"/testspider", TestSpiderHandler),


	# (r"/crawl/", CrawlerHandler )

	# (r"/admin", AdminHandler),    
]