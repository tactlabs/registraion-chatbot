# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from datetime import datetime
from flask import *
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chats_db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(50))
    clg_name = db.Column(db.String(50))
    dept_name = db.Column(db.String(10))
    stud_year = db.Column(db.String(10))
    os_type = db.Column(db.String(50))
    email_id = db.Column(db.String(30))
    date_created = db.Column(db.DateTime, default=datetime.now)
global data 
data=[]



class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_bdb_form"

    def validate_student_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `student_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Student name given = {slot_value} length = {len(slot_value)}")
        data.append(str(slot_value))
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"student_name": None}
        else:
            return {"student_name": slot_value}


    def validate_clg_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `clg_name` value."""

        print(f"College name given = {slot_value} length = {len(slot_value)}")
        data.append(str(slot_value))
        #if len(slot_value) <= 1:
        #    dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
        #    return {"clg_name": None}
        #else:
        return {"clg_name": slot_value}


    def validate_dept_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `dept_name` value."""

        data.append(str(slot_value))
        # If the name is super short, it might be wrong.
        #print(f"Student name given = {slot_value} length = {len(slot_value)}")
        #if len(slot_value) <= 2:
        #    dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
        #    return {"student_name": None}
        #else:
        return {"dept_name": slot_value}


    def validate_stud_year(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `stud_year` value."""

        data.append(str(slot_value))
        # If the name is super short, it might be wrong.
        #print(f"Student name given = {slot_value} length = {len(slot_value)}")
        #if len(slot_value) <= 2:
        #    dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
        #    return {"student_name": None}
        #else:
        return {"stud_year": slot_value}


    def validate_os_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `os_type` value."""

        data.append(str(slot_value))
        # If the name is super short, it might be wrong.
        #print(f"Student name given = {slot_value} length = {len(slot_value)}")
        #if len(slot_value) <= 2:
        #    dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
        #    return {"student_name": None}
        #else:
        return {"os_type": slot_value}


    def validate_email_id(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `email_id` value."""

        data.append(str(slot_value))
        user = User(student_name=data[0], clg_name=data[1], dept_name=data[2], stud_year=data[3], os_type=data[4], email_id=data[5])
        db.session.add(user)
        db.session.commit()

        # If the name is super short, it might be wrong.
        #print(f"Student name given = {slot_value} length = {len(slot_value)}")
        #if len(slot_value) <= 2:
        #    dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
        #    return {"student_name": None}
        #else:
        return {"email_id": slot_value}
  


class Actionreset(Action):

    def name(self) -> Text:
        return "action_reset_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data=[]
        #dispatcher.utter_message(text="reset slots")
        print("reset slots")

        return [AllSlotsReset()]