from mylib.extract import extract
from mylib.transform import load_data_to_db
from mylib.query import run_query

def test_extract():
    result = extract()
    print(result)
    assert result == "success", "Test for data extraction failed"
    print("Extract test passed")


def test_transform():
    result = load_data_to_db()
    assert result == "success", "Test for data transformation and load failed"
    print("Transform test passed")

def test_query():
    result = run_query()
    assert result == "success", "Test for querying the database failed"
    print("Query test passed")


if __name__ == "__main__":
    test_extract()
    test_transform()
    test_query()
    print("All tests passed successfully")
