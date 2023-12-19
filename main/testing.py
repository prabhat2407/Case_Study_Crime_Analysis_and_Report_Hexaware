import unittest
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.incident import Incident
from entity.status import Status
from unittest.mock import MagicMock


class TestCrimeAnalysisService(unittest.TestCase):
    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor
        self.crime_service = CrimeAnalysisServiceImpl()
        self.crime_service.connection = self.mock_connection

    def test_create_incident(self):
        self.mock_cursor.execute.return_value = True
        incident = Incident('None', 'Residential burglary in the suburbs','2023-03-20', 'Burglary', 'None', 'None')
        created = self.crime_service.create_incident(incident)
        self.assertTrue(created)
        self.assertTrue(self.mock_connection.commit.called)

    def test_update_incident_status(self):
        status = Status(status_id=1, status_name="Closed")
        self.mock_cursor.execute.return_value = True
        updated = self.crime_service.update_incident_status(status, incident_id=1)
        self.assertTrue(updated)
        self.assertTrue(self.mock_connection.commit.called)


if __name__ == '__main__':
    unittest.main()
