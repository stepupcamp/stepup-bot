# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


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

import time
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from rasa_sdk.forms import FormAction

def get_last_action(events:List[Dict[Text, Any]], action_name:str) -> bool:
    for event in reversed(events):
        if event.get('name') == action_name:
            return True
    return False

class ActionAskTime(Action):
    def name(self) -> Text:
        return "action_ask_time"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        reminder_time = tracker.get_slot("time")
        if reminder_time == None:
            # user didn't give us the time
            print("No time entered or we were able to detect (first_time)")
            dispatcher.utter_message(template = "utter_ask_time")
            return[FollowupAction("action_listen")]
        # slot is filled but action was not carried out
        elif get_last_action(tracker.events, "action_check_time") == False:
            print("No time entered or we were able to detect (second_time)")
            return[FollowupAction("action_check_time")]
        


class ActionAskDate(Action):
    def name(self) -> Text:
        return "action_ask_date"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        reminder_date = tracker.get_slot("date")
        if reminder_date == None:
            # user didn't give us the date
            print("No date entered or we were able to detect (first_time)")
            dispatcher.utter_message(template = "utter_ask_date")
            return[FollowupAction("action_listen")]
        # slot is filled but action was not carried out
        elif get_last_action(tracker.events, "action_check_date") == False:
            print("No date entered or we were able to detect (second_time)")
            return[FollowupAction("action_check_date")]

class ReminderForm(FormAction):
    """A form in rasa requires 4 mandatory stuffs
    - name : form_name
    - required_slots : specifies which slots are required
    - slot_mappings : tells the assistant how to fill the slots
    - submit : what to do once all of the slots have been filled.
    """

    def name(self):
        return "reminder_form"