from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from .fields import OtherModelField

author = 'Philip Chapkovski, chapkovski@gmail.com'

doc = """
Example of 'Other' field 
"""


class Constants(BaseConstants):
    name_in_url = 'other_field_app'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ddd = OtherModelField(label='Who should be the next German soccer team coach?',
                          choices=['Donald Trump', 'Vladimir Putin', 'Arnold Schwarzenegger'],
                          other_label='Someone else')
    edu = OtherModelField(label='What is the highest level of school you have completed or the highest '
                                'degree you have received?',
                          choices=['No formal education', 'Primary school', 'Secondary school',
                                   'Some college but no degree',
                                   'Lower degree (certificate or diploma)', 'Higher degree', 'Master\'s degree',
                                   'Doctoral degree',
                                   'Prefer not to state'],
                          other_label='Other (please specify)',
                          other_value='filka'
                          )
