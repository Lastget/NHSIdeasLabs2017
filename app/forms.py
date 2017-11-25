from wtforms import Form, StringField, IntegerField, DateField

class AddPatient(Form):
    first_name = StringField('First Name')
    second_name = StringField('Surname')
    birthday    = DateField('Date of Birth')

class Observation(Form):
    heart_rate = IntegerField('Heart Rate')
    sys_bp      = IntegerField('Systolic Pressure')
    dia_bp      = IntegerField('Diastolic Pressure')
    temp        = IntegerField('Temperature')
    resp_rate   = IntegerField('Respiratory Rate')
    gcs         = IntegerField('GCS', [validators.NumberRange(max=15, min=3)])
