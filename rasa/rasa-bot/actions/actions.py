# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
# def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import dateutil.parser
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ReminderForm(FormAction):
    def name(self):
        return "reminder_form"

    @staticmethod
    def required_slots(tracker):
        return ["date", "subject"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked
        """
        return {
            "date": [self.from_entity(entity="date")],
            "subject": [self.from_entity(entity="subject")],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # what the form has to do after recieving the slots.
        # we have to pre-process the date-time stamp here only.
        # i am not doing any formatting here as of now, but it can be done easily
        
        datetime_obj = dateutil.parser.parse(tracker.get_slot("date"))
        humanDate = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        time = datetime_obj.time()

        SlotSet(key="date", value=humanDate)

        dispatcher.utter_message(
            template="utter_set_reminder",
            time=time,
            date=tracker.get_slot("date"),
            subject=tracker.get_slot("subject"),
        )
        return []