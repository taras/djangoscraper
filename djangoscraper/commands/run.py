from scrapy.command import ScrapyCommand
from scrapy.core.manager import scrapymanager
from scrapy.core.engine import scrapyengine
from scrapy.spider import spiders
from scrapy.http import Request
from scrapy import log
from datetime import datetime, timedelta, date
import djangoscraper.utils.timetext as timetext
from djangoscraper.models import Task
from scrapy.xlib.pydispatch import dispatcher
from scrapy.core import signals
import subprocess, os, time, signal
from scrapy.conf import settings

if settings.get('MEMDEBUG_WITH_GUPPY', False):
    try:
        import guppy
    except ImportError:
        guppy = False
        log.msg('Could not import Guppy module.', level=log.ERROR)

interupted = False

def interupt(signal, frame):
    global interupted
    print '\nReceived cancel request, waiting for item to finish execution'
    interupted = True
    
class Command(ScrapyCommand):
    
    def syntax(self):
        return "[options] <domain>"
    
    def short_desc(self):
        return "Run scraper for specific domain."

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("--server", dest="server", action="store_true", help="Run scraper server that polls for tasks and runs them")
        parser.add_option("--demonize", dest="demonize", action="store_true", help="Run scrapy as a demon process continiously processing the spider's tasks.")
        parser.add_option("--all", dest="all", action="store_true", help="Run all available tasks for the spider.")
        parser.add_option('--interval', dest='interval', help="Polling interval for executing the spider in demon mode.")
        parser.add_option('--priority', dest='priority', help="Priority of task that you want to execute." )
        parser.add_option('--task-name', dest='task_name', help="Name of task that you would like to execute.", default=None )
        parser.add_option('--task-id', dest='task_id', help="Id of task that you would like to execute.", default=None )
        parser.add_option('--child-logfile', dest='child_logfile', help="Pass this parameter if you want to log output of child processes.", default=None)
        parser.add_option("--child", dest="child", action="store_true", help="Make this process a child.")

    def run(self, args, opts):
        
        if opts.server:
            global interupted
            signal.signal(signal.SIGINT, interupt)

            while not interupted:
                self._loop(args, opts)
                
        else:
            self.execute(args, opts)

    def _loop(self, args, opts):
        if settings.get('MEMDEBUG_WITH_GUPPY', False) and guppy:
            heapy = guppy.hpy()
            
        task = Task().next(locked=0, completed=0)
        if task:
            task.lock()
            cmd = ['python', os.path.join(os.getcwd(), 'scrapy-ctl.py'), 'run']
            cmd.append('--task-id=%s'%task.id)
            if opts.child_logfile:
                cmd.append('--logfile=%s'%opts.child_logfile)
                cmd.append('--child')
            task.start = datetime.now()
            process = subprocess.Popen(cmd, shell=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
            task.result, task.errors = process.communicate()
            task.finish = datetime.now()
            task.completed = 1
            task.save()
            timetext.LANG = 'en'
            total = task.finish - task.start
            log.msg('Finished: %s(%s) in %s'%(task.name, task.id, timetext.stringify(total)), level=log.INFO, domain=task.domain)
            if settings.get('MEMDEBUG_WITH_GUPPY', False) and guppy:
                log.msg(heapy.heap(), level=log.DEBUG)
                heapy.setref()
        else:
            time.sleep(30)
    
    def execute(self, args, opts):            
        
        task = None
        
        if opts.task_id:
            task = Task().load(id=opts.task_id)
        if opts.task_name:
            task = Task().next(name=opts.task_name)
            
        if task or len(args):
            
            if task:
                domain = task.domain
            else:
                domain = args[0]
            
            spider = spiders.fromdomain(domain)         
            scrapymanager.configure()
            if opts.child:
                def _stop():
                    pass
                # monkeypatching stop command to prevent stoping prematurely in child mode
                scrapymanager.stop = _stop
            if not task.locked:
                task.lock()
            self.crawl(spider, task)
            scrapyengine.start()

        else:
            log.msg('You must specify atleast 1 domain', level=log.ERROR)
            
    def crawl(self, spider, task):
        ''' Crawl task on specific spider '''
        spider.load(task)
        scrapymanager.crawl(*spider.start_urls)