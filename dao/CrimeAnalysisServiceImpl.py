from datetime import datetime
from dao.ICrimeAnalysisService import ICrimeAnalysisService
from entity.incident import Incident
from entity.status import Status
from entity.case import Case
from entity.report import Report
from util.DBConnUtil import DBConnUtil

class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()
        self.current_incident = None

    def create_incident(self, incident: Incident) -> bool:
        try:
            cursor = self.connection.cursor()
            inert_query = "INSERT INTO Incidents (IncidentType, Description, IncidentDate) VALUES (%s, %s, %s)"
            cursor.execute(inert_query, (incident.get_incident_type(), incident.get_description(), incident.get_date()))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating incident: {e}")
            return False

    def update_incident_status(self, status: Status, incident_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            update_query = "UPDATE Incidents SET status = %s WHERE IncidentID = %s"
            cursor.execute(update_query, (status.get_status_name(), incident_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating incident status: {e}")
            return False

    def get_incidents_in_date_range(self, start_date, end_date) -> list[Incident]:
        try:
            cursor = self.connection.cursor()
            select_query = "SELECT IncidentID, Description, IncidentDate, IncidentType FROM Incidents WHERE IncidentDate BETWEEN %s AND %s"
            cursor.execute(select_query, (start_date, end_date))
            incidents = [Incident(*row) for row in cursor.fetchall()]
            cursor.close()
            return incidents
        except Exception as e:
            print(f"Error getting incidents in date range: {e}")
            return []

    def search_incidents(self, criteria) -> list[Incident]:
        try:
            cursor = self.connection.cursor()
            select_query = "SELECT IncidentID, Description, IncidentDate, IncidentType FROM Incidents WHERE IncidentType = %s"
            cursor.execute(select_query, (criteria,))
            incidents = [Incident(*row) for row in cursor.fetchall()]
            cursor.close()
            return incidents
        except Exception as e:
            print(f"Error searching incidents: {e}")
            return []

    def get_incident_details(self, incident_id):
        try:
            cursor = self.connection.cursor()
            select_query = ("SELECT ID.IncidentID, ID.Description, ID.IncidentDate, ID.IncidentType, "
                            "V.FirstName AS victim_name, S.FirstName AS suspect_name "
                            "FROM Incidents ID "
                            "JOIN Victims V ON ID.VictimID = V.VictimID "
                            "JOIN Suspects S ON ID.SuspectID = S.SuspectID "
                            "WHERE ID.IncidentID = %s")

            cursor.execute(select_query, (incident_id,))
            details = cursor.fetchone()

            if details:
                incident = Incident(*details)
                self.current_incident = incident
                return incident
            else:
                return None

        except Exception as e:
            print(f"Error getting incident details: {e}")
            return None

    def generate_incident_report(self):
        if self.current_incident:
            report_details = f"Incident ID: {self.current_incident.get_incident_id()}\n"
            report_details += f"Incident Type: {self.current_incident.get_incident_type()}\n"
            report_details += f"Incident Date: {self.current_incident.get_date()}\n"
            report_details += f"Description: {self.current_incident.get_description()}\n"
            # Add other details to the report
            report_details += "Report generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            report = Report(report_id=None, details=report_details)
            return report
        else:
            print("No current incident.")
            return None

    def generate_incident_report(self, incident: Incident) -> Report:
        try:
            cursor = self.connection.cursor()
            select_query = ("SELECT V.FirstName AS victim_name, "
                            "S.FirstName AS suspect_name "
                            "FROM Incidents ID "
                            "JOIN Victims V ON ID.VictimID = V.VictimID "
                            "JOIN Suspects S ON ID.SuspectID = S.SuspectID "
                            "WHERE ID.IncidentID = %s")
            cursor.execute(select_query, (incident.get_incident_id(),))
            details = cursor.fetchone()

            report_details = f"Incident ID: {incident.get_incident_id()}\n"
            report_details += f"Incident Type: {incident.get_incident_type()}\n"
            report_details += f"Incident Date: {incident.get_date()}\n"
            report_details += f"Description: {incident.get_description()}\n"

            if details:
                victim_name, suspect_name = details
                report_details += f"Victim: {victim_name}\n"
                report_details += f"Suspect: {suspect_name}\n"

            report_details += "Report generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            report = Report(report_id=None, details=report_details)

            cursor.close()
            return report
        except Exception as e:
            print(f"Error generating incident report: {e}")
            return None

    def create_case(self, case_description: str) -> Case:
        try:
            cursor = self.connection.cursor()

            insert_case_query = "INSERT INTO Cases (CaseDescription) VALUES (%s)"
            cursor.execute(insert_case_query, (case_description,))
            case_id = cursor.lastrowid
            self.connection.commit()
            cursor.close()

            return Case(case_id, case_description, [])
        except Exception as e:
            print(f"Error creating case: {e}")
            return None

    def get_case_details(self, case_id: int) -> Case:
        try:
            cursor = self.connection.cursor()

            # SQL query to retrieve case details and associated incidents
            select_query = ("SELECT c.CaseID, c.CaseDescription, i.IncidentID, i.IncidentDate, i.IncidentType "
                            "FROM Cases c "
                            "LEFT JOIN Incidents i ON c.CaseID = i.CaseID "
                            "WHERE c.CaseID = %s")
            cursor.execute(select_query, (case_id,))
            results = cursor.fetchall()

            if results:
                case_id, case_description, incident_id, incident_date, incident_type = results[0]

                incidents = [Incident(incident_id, None, incident_date, incident_type)]

                for row in results[1:]:
                    incident_id, _, incident_date, incident_type = row[2:]
                    incidents.append(Incident(incident_id, None, incident_date, incident_type))

                cursor.close()
                return Case(case_id, case_description, incidents)
            else:
                cursor.close()
                return None
        except Exception as e:
            print(f"Error getting case details: {e}")
            return None

    def update_case_details(self, case: Case) -> bool:
        try:
            cursor = self.connection.cursor()
            update_query = "UPDATE Cases SET CaseDescription = %s WHERE CaseID = %s"
            cursor.execute(update_query, (case.get_description(), case.get_case_id()))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating case details: {e}")
            return False

    def get_all_cases(self) -> list[Case]:
        try:
            cursor = self.connection.cursor()
            select_query = "SELECT * FROM Cases"
            cursor.execute(select_query)
            cases_data = cursor.fetchall()

            cases = []
            for case_data in cases_data:
                case_id, case_description = case_data[0], case_data[1]

                select_query = "SELECT IncidentID, Description, IncidentDate, IncidentType FROM Incidents WHERE CaseID = %s"
                cursor.execute(select_query, (case_id,))
                incidents_data = cursor.fetchall()

                incidents = [Incident(*incident_data) for incident_data in incidents_data]
                case_instance = Case(case_id, case_description, incidents)
                cases.append(case_instance)

            cursor.close()
            return cases
        except Exception as e:
            print(f"Error getting all cases: {e}")
            return []
