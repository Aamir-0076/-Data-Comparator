from src.db_connector import DBConnector

def test_db_connection():
    db = DBConnector('db/comparator.db')
    df = db.query_table('PERSON')
    assert not df.empty
    db.close()
