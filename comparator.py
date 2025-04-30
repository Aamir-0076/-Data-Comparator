from .json_parser import load_json, extract_data
from .db_connector import DBConnector

class Comparator:
    def __init__(self, json_path, mapping_path, db_path):
        self.json_data = load_json(json_path)
        self.mapping_data = load_json(mapping_path)
        self.db_connector = DBConnector(db_path)

    def compare(self):
        results = []
        for mapping in self.mapping_data['mappings']:
            json_values = extract_data(self.json_data, mapping['jsonPath'])
            db_df = self.db_connector.query_table(mapping['table'])
            db_values = db_df[mapping['column']].tolist()

            match = set(json_values) == set(db_values)
            results.append({
                'jsonPath': mapping['jsonPath'],
                'table': mapping['table'],
                'column': mapping['column'],
                'match': match,
                'json_values': json_values,
                'db_values': db_values
            })
        return results
