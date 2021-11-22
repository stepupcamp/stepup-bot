## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## set reminder
* set_reminder
  - utter_set_reminder

## reminder happy path
* greet
  - utter_greet
* affirm
  - reminder_form
  - form{"name": "reminder_form"}
  - form{"name": null}
  - utter_set_reminder
* goodbye
  - utter_goodbye

## no reminder
* greet
    - utter_greet
* deny
    - utter_goodbye

## reminder stop
* greet
    - utter_greet
* affirm
    - reminder_form
    - form{"name": "reminder_form"}
* out_of_scope
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye

## reminder continue
* greet
    - utter_greet
* affirm
    - reminder_form
    - form{"name": "reminder_form"}
* out_of_scope
    - utter_ask_continue
* affirm
    - reminder_form
    - form{"name": null}
    - utter_set_reminder