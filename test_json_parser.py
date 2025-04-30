from src.json_parser import load_json, extract_data

def test_load_json():
    data = load_json('data/sample.json')
    assert data["person"]["personId"] == "123"

def test_extract_data():
    data = load_json('data/sample.json')
    assert extract_data(data, 'person.name.first') == ["John"]
