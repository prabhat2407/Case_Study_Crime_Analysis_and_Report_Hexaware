class Report:
    def __init__(self, report_id, details):
        self._report_id = report_id
        self._details = details

    def get_report_id(self):
        return self._report_id

    def set_report_id(self, report_id):
        self._report_id = report_id

    def get_details(self):
        return self._details

    def set_details(self, details):
        self._details = details
