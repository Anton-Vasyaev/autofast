# project
from ..interfaces import IMessageFormatter

from ..data import CityMessage



class FooMessageFormetter(IMessageFormatter):
    def __init__(self):
        self.language = 'rus'
        

    def format_message(self, message: CityMessage) -> str:
        city  = message.city
        mayor = message.mayor
        
        if self.language == 'rus':
            return (
                f'Городом {city.name} с населением {city.population} человек управляет мэр '
                f'{mayor.name} [Скилл: {mayor.skills}, возраст: {mayor.age}].'
            )
        elif self.language == 'eng':
            return (
                f'City {city.name} with polulation {city.population} citizens rules by mayor '
                f'{mayor.name} [Skill: {mayor.skills}, возраст: {mayor.age}].'
            )
        else:
            raise ValueError(f'unspected language:{self.language}')