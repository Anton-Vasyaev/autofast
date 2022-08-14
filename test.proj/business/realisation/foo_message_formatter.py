# project
from ..interfaces    import IMessageFormatter
from ..data          import CityMessage
from ..configuration import FormatConfiguration, LanguageType, WordType




class FooMessageFormatter(IMessageFormatter):
    def __init__(
        self, 
        config : FormatConfiguration
    ):
        self.config = config
        

    def format_message(self, message: CityMessage) -> str:
        city  = message.city
        mayor = message.mayor
        
        message_str = ''
        if self.config.language_type == LanguageType.ENGLISH:
            message_str = (
                f'City {city.name} with polulation {city.population} citizens rules by mayor '
                f'{mayor.name} [Skill: {mayor.skills}, Age: {mayor.age}].'
            )
            
        elif self.config.language_type == LanguageType.RUSSIAN:
            message_str = (
                f'Городом {city.name} с населением {city.population} человек управляет мэр '
                f'{mayor.name} [Скилл: {mayor.skills}, возраст: {mayor.age}].'
            )

        else:
            raise ValueError(f'unspected language type:{self.config.language_type}')
        
        if self.config.word_type == WordType.LOWER:
            message_str = message_str.lower()
        elif self.config.word_type == WordType.UPPER:
            message_str = message_str.upper()
        else:
            raise ValueError(f'unspected word type:{self.config.word_type}')
        
        return message_str