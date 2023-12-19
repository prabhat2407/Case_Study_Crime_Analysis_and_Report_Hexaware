from abc import ABC, abstractmethod
from entity.incident import Incident
from entity.case import Case
from entity.report import Report
from entity.status import Status

class ICrimeAnalysisService(ABC):
    @abstractmethod
    def create_incident(self, incident: Incident) -> bool:
        pass

    @abstractmethod
    def update_incident_status(self, status: Status, incident_id: int) -> bool:
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date, end_date) -> list[Incident]:
        pass

    @abstractmethod
    def search_incidents(self, criteria) -> list[Incident]:
        pass

    @abstractmethod
    def generate_incident_report(self, incident: Incident) -> Report:
        pass

    @abstractmethod
    def create_case(self, case_description: str, incidents: list[Incident]) -> Case:
        pass

    @abstractmethod
    def get_case_details(self, case_id: int) -> Case:
        pass

    @abstractmethod
    def update_case_details(self, case: Case) -> bool:
        pass

    @abstractmethod
    def get_all_cases(self) -> list[Case]:
        pass
