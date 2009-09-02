from scrapy.command import ScrapyCommand
from djangoscraper.models import Task

    
class Command(ScrapyCommand):
    
    def syntax(self):
        return "[options] task_name class_name"
    
    def short_desc(self):
        return "Run scraper for specific domain."

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-i", "--init", dest="init", action="store_true", help="Prepare django app for use with djangoscraper.")
        parser.add_option("-c", "--create", dest="create", action="store_true", help="Create new task")
        parser.add_option("-x", "--no-modify", dest="nomodify", action="store_true", help="Use this option if you do not wish for this command to modify your settings.py")

    def run(self, args, opts):
        if opts.init:
            self.init(args, opts)
        
        if opts.create:
            if len(args) == 2:
                self.create(args, opts)
            else:
                print "You have to specify task name and task class"
                print "Syntax: %s" % self.syntax()
                
    def init(self, args, opts):
        pass
    
    def create(self, args, opts):
        pass