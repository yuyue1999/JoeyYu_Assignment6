# import json
from mylib.extract import extract
from mylib.transform import load_data_to_db
from mylib.query import run_query

# Main function to handle 3 key processes: Extract, Transform & Load, and Query
def main_res():
    extract_result = extract()
    transform_result = load_data_to_db()
    query_result = run_query()
    results = {
        "extract": extract_result,
        "transform_db": transform_result,
        "query": query_result,
    }

    return results


if __name__ == "__main__":
    print(main_res())

