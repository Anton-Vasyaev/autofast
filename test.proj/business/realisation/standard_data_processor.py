# project
from ..interfaces import IPrinter
from ..interfaces import IMessageFormatter
from ..interfaces import IMessageLoader
from ..interfaces import IDataProcessor



class StandardDataProcessor(IDataProcessor):
    def __init__(
        self,
        message_loader    : IMessageLoader,
        message_formatter : IMessageFormatter,
        printer           : IPrinter
    ):
        self.message_loader    = message_loader
        self.message_formatter = message_formatter
        self.printer           = printer
        

    def process(self):
        message = self.message_loader.load_message()
        
        message_str = self.message_formatter.format_message(message)
        
        self.printer.print_data(message_str)