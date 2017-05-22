from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'ajuhl'

LOGGER = getLogger(__name__)

class KnockKnockSkill(MycroftSkill)

    def __init__(self):
        super(KnockKnockSkill, self).__init__(name="KnockKnockSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        knock_knock_intent = IntentBuilder("KnockKnockIntent").\
            require("KnockKnockKeyword").build()
        self.register_intent(knock_knock_intent, self.handle_knock_knock_intent)

    def handle_knock_knock_intent(self, message):
        self.speak_dialog("knock")

    def stop(self):
        pass
def create_skill():
    return KnockKnockSkill()
