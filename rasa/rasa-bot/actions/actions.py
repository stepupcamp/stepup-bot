# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet
from rasa.core.actions.forms import FormAction


class ActionValidMeeting(Action):
    def name(self) -> Text:
        return "action_valid_meeting"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        link = "https://meet.google.com/nmv-jxcq-txo"
        # dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_template("utter_meeting_created", tracker, meeting_link=link)

        return []


class ActionInvalidMeeting(Action):
    def name(self) -> Text:
        return "action_invalid_meeting"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        link = "https://meet.google.com/nmv-jxcq-txo"
        # dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_template(
            "utter_meeting_not_allowed", tracker, meeting_link=link
        )

        return []


# class AskForSlotTime(Action):
#     def name(self) -> Text:
#         return "action_ask_reminder_form_time"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(text="utter_ask_reminder_form_time")
#         return []


# class AskForSlotReminderSubject(Action):
#     def name(self) -> Text:
#         return "action_ask_reminder_form_reminder_subject"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(text="utter_ask_reminder_form_reminder_subject")
#         return []


# class ReminderForm(FormAction):
#     def name(self):
#         return "reminder_form"

#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["reminder_subject", "time"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         return {
#             "reminder_subject": [self.from_entity(entity="reminder_subject")],
#             "time": [self.from_entity("time")],
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:

#         dispatcher.utter_message("utter_reminder_form_slots_values")
#         return []


class ValidateReminderForm(Action):
    def name(self) -> Text:
        return "reminder_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["time", "reminder_subject"]

        for slot_name in required_slots:
            if tracker.slot.get(slot_name) is None:
                # The slot is not filled yet, request the user to fill the slot next time.
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]


class ActionCreateReminder(Action):
    def name(self) -> Text:
        return "action_create_reminder"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(template="utter_reminder_form_slots_values",
                                time=tracker.get_slot("time"),
                                reminder_subject=tracker.get_slot("reminder_subject"))
        return []
