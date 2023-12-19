class Status:
    def __init__(self, status_id, status_name):
        self._status_id = status_id
        self._status_name = status_name

    def get_status_id(self):
        return self._status_id

    def set_status_id(self, status_id):
        self._status_id = status_id

    def get_status_name(self):
        return self._status_name

    def set_status_name(self, status_name):
        self._status_name = status_name
