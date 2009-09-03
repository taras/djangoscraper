from scrapy.contrib.spiders.crawl import CrawlSpider
from scrapy import log
from scrapy.http import Request
from scrapy.utils.misc import arg_to_iter
from djangoscraper.models import Task
from scrapy.utils.misc import load_object
from scrapy.conf import settings

class TaskSpider(CrawlSpider):
    '''
    TaskSpider is a base task oriented spider that other task spiders inherit from.
    TaskSpider works like BaseSpider but it's more oriented towards accomplishing specific tasks.
    '''
    
    task = None
    
    def __init__(self):
        """Constructor takes care of loading task definition and compiling rules"""
        super(CrawlSpider, self).__init__()
    
    def load(self, task):
        '''
        Gets task for the spider, loads the tasks's module code and applies code
        from configuration to the spider.
        '''
        self.task = task
        configuration = None
        if settings.get('TASKS'):
            available_tasks = settings.get('TASKS')
            if available_tasks.has_key(task.name):
                try:
                    configuration = load_object(available_tasks[task.name])
                except Exception, (ErrorMessage):
                    log.msg('Could not load configuration for task %s' % task.name, level=log.ERROR)
                    log.msg(ErrorMessage, level=log.DEBUG, domain='tripcentral.ca')
                configuration = configuration(task, self)
                if hasattr(configuration, 'start_urls'):
                    setattr(self, 'start_urls', configuration.start_urls)
                if hasattr(configuration, 'rules'):
                    setattr(self, 'rules', configuration.rules)
                if hasattr(configuration, 'parse_start_url'):
                    setattr(self, 'parse_start_url', configuration.parse_start_url)
                self.start_urls = self.get_start_urls()
                self._compile_rules()                
            else:
                log.msg('%s is not defined in settings.TASKS' % task.name, level=log.ERROR, domain=task.domain )
        else:
            log.msg('settings.TASKS is not defined', level=log.ERROR, domain=task.domain )
                
    def get_start_urls(self):
        '''Gets list of start_urls for the task and returns them'''
        urls = []
        if self.has_task() and self.task.start_urls:
            urls = self.task.start_urls.splitlines()
        return urls
                
    def fetch_task(self, id=None, name=None):
        ''' Gets the next pending task and returns it '''
        if name:
            task = Task.objects.filter(domain=self.domain_name, locked=0, completed=0, name=name).order_by('priority')
        elif id:
            task = Task.objects.filter(domain=self.domain_name, locked=0, completed=0, id=id).order_by('priority')
        else:
            task = Task.objects.filter(domain=self.domain_name, locked=0, completed=0).order_by('priority')            

        if task:
            task = task[0]
            task.locked = 1
            task.save()
            return task
        return None

    def has_pending(self, name=None):
        '''
        Return true if pending tasks for this domain exist.
        Pending task is a task that is not locked and not completed.
        '''
        if name:
            pending = bool(Task.objects.filter(domain=self.domain_name, locked=0, completed=0, name=name))
        else:
            pending = bool(Task.objects.filter(domain=self.domain_name, locked=0, completed=0))

        return pending
        
    def has_task(self):
        '''
        Return true if instance of spider has task assigned to it.
        '''
        return bool(self.task)