
"""
MAIN STRUCTURE FOR DB COLLECTIONS

MongoDB instantiated at Application level 

"""

### to instantiate user core fields in mongoDB
USER_CORE_FIELDS = [
	"username",
	"email",
	"uuid",		#
	"password" 	# needs to be hashed
]


### to instantiate datamodel core fields in mongoDB
DATAMODEL_FIELDS_TYPES = [
	"url", 
	"text", 
	"image", 
	"adress", 
	"date", 
	"tags", 
	"price"
]
DATAMODEL_CORE_FIELDS = [
	{"field_name" : "next_page", 		"field_type" : "text"},
	{"field_name" : "follow_xpath", 	"field_type" : "url"}, 
	{"field_name" : "link_data", 		"field_type" : "url"},
	{"field_name" : "link_src", 		"field_type" : "url"},
	{"field_name" : "added_by", 		"field_type" : "text"}, 
	{"field_name" : "item_created_at", 	"field_type" : "date"},
	
	{"field_name" : "testClass", "field_type" : "text"}
]
DATAMODEL_DEFAULT_CUSTOM_FIELDS = [
	{"field_name" : "author",	"field_type" : "text"},
	{"field_name" : "abstract", "field_type" : "text"},
	{"field_name" : "tags", 	"field_type" : "tags"},
	{"field_name" : "url", 		"field_type" : "url"},
]

### to instantiate contributor core fields in mongoDB
CONTRIBUTOR_CORE_FIELDS = {
	
	# custom infos 
	"infos" : {
		"name" 			: "" , 	# real name contributor
		"page_url" 		: "" ,
		"contact" 		: "",
		"notes" 		: "",
		"added_by" 		: "",
		"is_working" 	: False
	},

	# scraper - custom for scraping basics
	 "scraper_config" : {
		"spidername" 	: "",
		"start_urls" 	: [],
		"parse_follow" 	: False,
		"next_page" 	: "",
		"follow_xpath" 	: "",
		"page_needs_splash" : False,
	},

	# scraper - custom for scraping xpaths
	"scraper_config_xpaths" : {
		# "next_page_xpath" : None,
	},

	# scraper - global settings	
	"scraper_settings" : {
		"LIMIT" 			: 100,
		"download_delay" 	: 0,
		"page_count" 		: 1,
	},

	# scraper stats	
	"stats" : {
		"error_array" 		: [],
		"item_count" 		: 0,
		"item_count_depth_1" : 0
	},

}

CONTRIBUTOR_EDIT_FIELDS = {

	### fields displayed in edit contributor page
	### "needed" = to be displayed
	### "optional" = optional (in drawer)

	# custom infos 
	"infos" : {
		"needed" : [
			"name", 
			"page_url",
			# "added_by",
		],
		"optional" : [
			"contact",
			"notes",
		]
	},

	# scraper - custom for scraping basics
	 "scraper_config" : {
		"needed" : [
			"spidername" ,
			"start_urls",
			"next_page",
			"parse_follow",
			"follow_xpath",
		], 
		"optional": [
			"page_needs_splash",
		]
	 },

	# # scraper - custom for scraping xpaths
	# "scraper_config_xpaths" : {
	# # 	"next_page_xpath" : None,
	# },

	# # scraper - global settings	
	# "scraper_settings" : {
	# 	"LIMIT" : 100,
	# 	"download_delay" : 0,
	# 	"page_count" : 1,
	# },

	# # scraper stats	
	# "stats" : {
	# 	"error_array" : [],
	# 	"item_count" : 0,
	# 	"item_count_depth_1" : 0
	# },
}

class SpiderConfig :

	def __init__(self, *args, **kwargs) :
		"""
		a spider config object to instantiate a config
		this config will be stored in db
		"""
		
		self.spider_config_empty = CONTRIBUTOR_CORE_FIELDS
		for key in self.spider_config_empty.keys() :
			pass