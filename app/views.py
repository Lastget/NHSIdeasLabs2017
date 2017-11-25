from flask.views import views

class AddPatientView(View):

    def get_template_name(self):
        return 'addpatient.html'

class ObservationView(View):

    def get_template_name(self):
        return 'observation.html

class PatienView(View):

    def get_template_name(self):
        return 'patients.html'

    def get_objects(self):
        return Patient.query.all()s
