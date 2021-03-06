"""
Autocomplete classes
"""
from agnocomplete.register import register
from agnocomplete.core import AgnocompleteChoices, AgnocompleteModel
from demo.models import Person


class AutocompleteColor(AgnocompleteChoices):
    choices = ['green', 'gray', 'blue', 'grey']


class AutocompleteChoicesPages(AgnocompleteChoices):
    choices = ["choice{}".format(i) for i in range(200)]


class AutocompleteChoicesPagesOverride(AutocompleteChoicesPages):
    page_size = 30


class AutocompletePerson(AgnocompleteModel):
    model = Person
    fields = ['first_name', 'last_name']


# Special: not integrated into the registry (yet)
class AutocompletePersonQueryset(AgnocompleteModel):
    fields = ['first_name', 'last_name']

    def get_queryset(self):
        return Person.objects.filter(email__contains='example.com')


# Special: not integrated into the registry (yet)
class AutocompletePersonMisconfigured(AgnocompleteModel):
    fields = ['first_name', 'last_name']


# Registration
register(AutocompleteColor)
register(AutocompletePerson)
register(AutocompleteChoicesPages)
register(AutocompleteChoicesPagesOverride)
