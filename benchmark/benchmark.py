# # benchmark.py
import time
from sql_loader.query_sql import query_sql
from mongodb_loader.query_mongo import query_mongodb
from neo4j_loader.query_neo4j import query_neo4j
import queries
def measure_query_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

def run_benchmarks():
    times_data = {}

    # Assuming all databases have the same set of query names for benchmarking
    query_names = queries.sql_queries.keys()

    # Measure query times
    for query_name in query_names:
        # MongoDB query handling
        mongo_query = queries.mongodb_queries[query_name]
        mongo_query_time = measure_query_time(
            query_mongodb,
            mongo_query["query_type"],
            mongo_query["query"],
            mongo_query.get("limit"),
            mongo_query.get("sort")
        )

        # SQL and Neo4j query handling
        sql_query_time = measure_query_time(query_sql, queries.sql_queries[query_name])
        neo4j_query_time = measure_query_time(query_neo4j, queries.neo4j_queries[query_name])

        times_data[query_name] = {
            "SQL": sql_query_time,
            "MongoDB": mongo_query_time,
            "Neo4j": neo4j_query_time
        }

    return times_data, query_names

# if __name__ == "__main__":
#     results, query_names = run_benchmarks()
#     # Further code to process or display results
