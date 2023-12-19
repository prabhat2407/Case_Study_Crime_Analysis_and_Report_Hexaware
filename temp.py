from entity.incident import Incident
from util.DBConnUtil import DBConnUtil


connection = DBConnUtil.get_connection()
cursor = connection.cursor()
start_date = "2023-01-10"
end_date = "2023-04-25"
select_query = "SELECT * FROM Incidents WHERE IncidentDate BETWEEN %s AND %s"
cursor.execute(select_query, (start_date, end_date))
for i in cursor.fetchall():
    print(i)
