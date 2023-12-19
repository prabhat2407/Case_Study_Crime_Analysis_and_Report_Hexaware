class Incident:
    def __init__(self, incident_id, description, date, incident_type, victim_name = None, suspect_name = None):
        self._incident_id = incident_id
        self._description = description
        self._date = date
        self._incident_type = incident_type
        self._victim_name = victim_name
        self._suspect_name = suspect_name

    def get_incident_id(self):
        return self._incident_id

    def set_incident_id(self, incident_id):
        self._incident_id = incident_id

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_incident_type(self):
        return self._incident_type

    def set_incident_type(self, incident_type):
        self._incident_type = incident_type
