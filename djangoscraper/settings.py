# Scrapy settings for scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here
#
#     http://doc.scrapy.org/ref/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

import scraper, os

PROJECT_NAME = 'scraper'

BOT_NAME = PROJECT_NAME
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'
TEMPLATES_DIR = '%s/templates' % scraper.__path__[0]
DEFAULT_ITEM_CLASS = 'scraper.items.ScraperItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
DEPTH_LIMIT = 2

EXTENSIONS = {
    'scrapy.stats.corestats.CoreStats': 0,
    'scrapy.management.web.WebConsole': None,
    'scrapy.management.telnet.TelnetConsole': 0,
    'scrapy.contrib.webconsole.scheduler.SchedulerQueue': 0,
    'scrapy.contrib.webconsole.livestats.LiveStats': None,
    'scrapy.contrib.webconsole.spiderctl.Spiderctl': None,
    'scrapy.contrib.webconsole.enginestatus.EngineStatus': None,
    'scrapy.contrib.webconsole.stats.StatsDump': 0,
    'scrapy.contrib.spider.reloader.SpiderReloader': 0,
    'scrapy.contrib.memusage.MemoryUsage': 0,
    'scrapy.contrib.memdebug.MemoryDebugger': 0,
    'scrapy.contrib.closedomain.CloseDomain': 0,
    'scrapy.contrib.debug.StackTraceDump': 1,    
}

TASKS = {
	# links to your tasks go in here
    #'task_name':'path.to.task.class',
}

COMMANDS_MODULE = 'scraper.commands'