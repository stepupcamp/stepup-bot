# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionValidMeeting(Action):

    def name(self) -> Text:
        return "action_valid_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link = "https://meet.google.com/nmv-jxcq-txo"
        # dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_template("utter_meeting_created", tracker, meeting_link=link)

        return []

class ActionInvalidMeeting(Action):

    def name(self) -> Text:
        return "action_invalid_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link = "https://meet.google.com/nmv-jxcq-txo"
        # dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_template("utter_meeting_not_allowed", tracker, meeting_link=link)

        return []
