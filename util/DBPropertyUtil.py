class DBPropertyUtil:
    @staticmethod
    def get_connection_properties(file_path = 'C://Users//acer//Desktop//Hexaware//Python//CARS//util//config.txt'):
        try:
            with open(file_path, 'r') as file:
                properties = {}
                for line in file:
                    key, value = line.strip().split('=')
                    properties[key.strip()] = value.strip()
                return properties
        except Exception as e:
            print(f"Error reading property file: {e}")