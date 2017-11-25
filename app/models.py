from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class Patient(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(string(50))
    second_name = Column(string(50))
    birthday    = Column(date)

class Observations(Model):
    patient_id = Column(Integer, ForeignKey('Patient.id'))
    heart_rate = Column(Integer)
    sys_bp  = Column(Integer)
    dia_bp  = Column(Integer)
    temp    = Column(Integer)
    gcs     = Column(Integer)
    resp_rate   = Column(Integer)
    time    =Column(datetime)
