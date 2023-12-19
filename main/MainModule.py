from datetime import datetime
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.incident import Incident
from entity.status import Status
from entity.case import Case

def print_menu():
    print("\n==== Crime Analysis and Reporting System ====")
    print("1. Create Incident")
    print("2. Update Incident Status")
    print("3. Get Incidents in Date Range")
    print("4. Search Incidents")
    print("5. Generate Incident Report")
    print("6. Create Case")
    print("7. Get Case Details")
    print("8. Update Case Details")
    print("9. Get All Cases")
    print("0. Exit")

def main():
    service = CrimeAnalysisServiceImpl()

    while True:
        print_menu()
        choice = input("Enter your choice (0-9): ")

        if choice == "0":
            print("Exiting the Crime Analysis and Reporting System. Goodbye!")
            break
        elif choice == "1":
            incident_id = None
            description = input("Enter Incident Description: ")
            date = datetime.now()
            incident_type = input("Enter Incident Type: ")

            incident = Incident(incident_id=incident_id, description=description, date=date,
                                incident_type=incident_type)

            created = service.create_incident(incident)

            if created:
                print("Incident created successfully!")
            else:
                print("Failed to create incident.")
        elif choice == "2":
            incident_id = int(input("Enter Incident ID to update status: "))
            status_name = input("Enter new Status: ")
            status = Status(status_id=None, status_name=status_name)
            updated = service.update_incident_status(status, incident_id)
            if updated:
                print("Incident status updated successfully!")
            else:
                print("Failed to update incident status.")
        elif choice == "3":
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            incidents = service.get_incidents_in_date_range(start_date, end_date)
            if incidents:
                print("Incidents in date range:")
                for incident in incidents:
                    print(f"Incident ID: {incident.get_incident_id()}, Type: {incident.get_incident_type()}, Date: {incident.get_date()}")

            else:
                print("No incidents found in the given date range.")
        elif choice == "4":
            search_criteria = input("Enter incident type: ")
            search_results = service.search_incidents(search_criteria)
            if search_results:
                print(f"Incidents matching incident type '{search_criteria}':")
                for incident in search_results:
                    print(f"Incident ID: {incident.get_incident_id()}, Type: {incident.get_incident_type()}, Date: {incident.get_date()}")

            else:
                print(f"No incidents found matching search criteria '{search_criteria}'.")
        elif choice == "5":
            incident_id_to_report = int(input("Enter Incident ID to generate report: "))
            incident_to_report = service.get_incident_details(incident_id_to_report)

            if incident_to_report:
                report = service.generate_incident_report(incident_to_report)
                if report:
                    print(f"Incident Report:\n{report.get_details()}")
                else:
                    print("Failed to generate incident report.")
            else:
                print(f"No incident found with ID {incident_id_to_report}.")

        elif choice == "6":
            case_description = input("Enter Case Description: ")
            new_case = service.create_case(case_description)

            if new_case:
                print(f"Case created successfully!\nCase ID: {new_case.get_case_id()}, Description: {new_case.get_description()}")
            else:
                print("Failed to create case.")

        elif choice == "7":
            case_id_to_fetch = int(input("Enter Case ID to fetch details: "))
            fetched_case = service.get_case_details(case_id_to_fetch)

            if fetched_case:
                print(
                    f"Case Details:\nCase ID: {fetched_case.get_case_id()}, Description: {fetched_case.get_description()}")
                print("Incidents in the case:")
                for incident in fetched_case.get_incidents():
                    print(
                        f"Incident ID: {incident.get_incident_id()}, Type: {incident.get_incident_type()}, Date: {incident.get_date()}")
            else:
                print(f"No case found with ID {case_id_to_fetch}.")

        elif choice == "8":
            try:
                case_id_to_update = int(input("Enter Case ID to update details: "))
                fetched_case = service.get_case_details(case_id_to_update)

                if fetched_case:
                    new_description = input("Enter updated Case Description: ")
                    fetched_case.set_description(new_description)

                    updated_case = service.update_case_details(fetched_case)

                    if updated_case:
                        print("Case details updated successfully!")
                    else:
                        print("Failed to update case details.")
                else:
                    print(f"No case found with ID {case_id_to_update}.")

            except ValueError:
                print("Invalid input. Please enter a valid Case ID.")

        elif choice == "9":
            all_cases = service.get_all_cases()
            if all_cases:
                print("All Cases:")
                for case in all_cases:
                    print(f"Case ID: {case.get_case_id()}, Description: {case.get_description()}")

            else:
                print("No cases found.")
        else:
            print("Invalid choice. Please enter a number between 0 and 9.")

if __name__ == "__main__":
    main()
