# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet, AllSlotsReset
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
        dispatcher.utter_template(
            "utter_meeting_created", tracker, meeting_link=link)

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
        dispatcher.utter_template(
            "utter_meeting_not_allowed", tracker, meeting_link=link)

        return []


class ValidateReminderForm(Action):
    def name(self) -> Text:
        return "reminder_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots = ["time", "reminder_subject"]
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        for slot_name in required_slots:
            slot_to_fill = tracker.get_slot(slot_name)
            if slot_to_fill:
                slot_values.update(self.extract_requested_slot(dispatcher,
                                                            tracker, domain))
            else:
                return [SlotSet("requested_slot", slot_name)]

        # for slot_name in required_slots:
        #     if tracker.slot.get(slot_name) is None:
        #         # The slot is not filled yet, request the user to fill the slot next time.
        #         return [SlotSet("requested_slot", slot_name)]

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


class ActionInformReminder(Action):
    def name(self) -> Text:
        return "action_inform_reminder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        time_slot_value = next(tracker.get_latest_entity_values("time"), None)
        rm_slot_value = next(tracker.get_latest_entity_values("reminder_subject"), None)

        # print("Time Slot value:", time_slot_value)
        # print("Reminder Slot value:", rm_slot_value)

        dispatcher.utter_message(template="utter_reminder_form_slots_values",
                                time=time_slot_value,
                                reminder_subject=rm_slot_value)

        return [AllSlotsReset()]


class ActionSplitGroup(Action):
    def name(self) -> Text:
        return "action_split_group"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import requests
        print(requests.get("https://reqres.in/api/users?page=2").json())

        return []


# class AskForSlotTime(Action):
#     def name(self) -> Text:
#         return "action_ask_reminder_form_time"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(template="utter_ask_reminder_form_time")
#         return []


# class AskForSlotReminderSubject(Action):
#     def name(self) -> Text:
#         return "action_ask_reminder_form_reminder_subject"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(template="utter_ask_reminder_form_reminder_subject")
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

#         dispatcher.utter_message(template="utter_reminder_form_slots_values")
#         return [AllSlotsReset()]


# class ActionCreateReminder(FormAction):
#     """Example of a custom form action"""

#     def name(self):
#         """Unique identifier of the form"""
#         return "action_create_reminder"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""

#         return ["reminder_subject", "time"]

#     def validate(self,
#                  dispatcher: CollectingDispatcher,
#                  tracker: Tracker,
#                  domain: Dict[Text, Any]) -> List[Dict]:
#         """Validate extracted requested slot
#                 else reject the execution of the form action
#         """
#         # extract other slots that were not requested
#         # but set by corresponding entity
#         slot_values = self.extract_other_slots(dispatcher, tracker, domain)

#         # extract requested slot
#         required_slots = ["time", "reminder_subject"]

#         for slot_name in required_slots:
#             slot_to_fill = tracker.get_slot(slot_name)
#             if slot_to_fill:
#                 slot_values.update(self.extract_requested_slot(dispatcher,
#                                                             tracker, domain))
#                 # if not slot_values:
#                 #     # reject form action execution
#                 #     # if some slot was requested but nothing was extracted
#                 #     # it will allow other policies to predict another action
#                 #     raise ActionExecutionRejection(self.name(),
#                 #                                 "Failed to validate slot {0}"
#                 #                                 "with action {1}"
#                 #                                 "".format(slot_to_fill,
#                 #                                             self.name()))


#     def submit(
#         self, dispatcher: CollectingDispatcher,
#         tracker: Tracker
#     ):
#         """Define what the form has to do
#                 after all required slots are filled"""

#         dispatcher.utter_template('utter_reminder_form_slots_values', tracker)

#         return [AllSlotsReset()]
