class Case:
    def __init__(self, case_id, description, incidents):
        self._case_id = case_id
        self._description = description
        self._incidents = incidents

    def get_case_id(self):
        return self._case_id

    def set_case_id(self, case_id):
        self._case_id = case_id

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_incidents(self):
        return self._incidents

    def set_incidents(self, incidents):
        self._incidents = incidents

