# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset


class ActionValidMeeting(Action):

    def name(self) -> Text:
        return "action_valid_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link = "https://meet.google.com/nmv-jxcq-txo"
        dispatcher.utter_template("utter_meeting_created", tracker, meeting_link=link)

        return []

class ActionInvalidMeeting(Action):

    def name(self) -> Text:
        return "action_invalid_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link = "https://meet.google.com/nmv-jxcq-txo"
        dispatcher.utter_template("utter_meeting_not_allowed", tracker, meeting_link=link)

        return []


class ValidateReminderForm(Action):
    def name(self) -> Text:
        return "reminder_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots = ["time", "reminder_subject"]

        for slot_name in required_slots:
            if tracker.slot.get(slot_name) is None:
                # The slot is not filled yet, request the user to fill the slot next time.
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]


class ActionCreateReminder(Action):
    def name(self) -> Text:
        return "action_create_reminder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        dispatcher.utter_message(template="utter_reminder_form_slots_values",
                                time=tracker.get_slot("time"),
                                reminder_subject=tracker.get_slot("reminder_subject"))

        return [AllSlotsReset()]
