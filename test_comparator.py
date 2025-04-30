from src.comparator import Comparator

def test_comparator_logic():
    comparator = Comparator('data/sample.json', 'data/mappings.json', 'db/comparator.db')
    results = comparator.compare()
    assert isinstance(results, list)
    assert len(results) > 0
    for result in results:
        assert 'match' in result
