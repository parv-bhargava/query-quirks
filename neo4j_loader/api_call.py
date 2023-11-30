from neo4j import GraphDatabase
import requests
from neo4j_config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

# Neo4j Connection
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# API Call
url = 'https://data.cityofnewyork.us/resource/kxp8-n2sj.json'
data = requests.get(url).json()

# Function to Load Data into Neo4j
def load_data(tx, data):
    for record in data:
        if all(key in record for key in ['VendorID', 'PULocationID', 'DOLocationID']):
            # Create your query based on the structure of your data and database schema
            query = """
            MERGE (v:Vendor { id: $VendorID })
            MERGE (pickup:Location { id: $PULocationID })
            MERGE (dropoff:Location { id: $DOLocationID })
            CREATE (trip:Trip {
                pickup_datetime: $tpep_pickup_datetime,
                dropoff_datetime: $tpep_dropoff_datetime,
                passenger_count: toInteger($passenger_count),
                trip_distance: toFloat($trip_distance),
                rate_code: toInteger($RatecodeID),
                store_and_fwd_flag: $store_and_fwd_flag,
                payment_type: toInteger($payment_type),
                fare_amount: toFloat($fare_amount),
                extra: toFloat($extra),
                mta_tax: toFloat($mta_tax),
                tip_amount: toFloat($tip_amount),
                tolls_amount: toFloat($tolls_amount),
                improvement_surcharge: toFloat($improvement_surcharge),
                total_amount: toFloat($total_amount),
                congestion_surcharge: toFloat($congestion_surcharge)
            })
            MERGE (v)-[:OPERATED]->(trip)
            MERGE (trip)-[:STARTED_AT]->(pickup)
            MERGE (trip)-[:ENDED_AT]->(dropoff)
            """
            tx.run(query, record)

# Load to Neo4j
with driver.session() as session:
    session.write_transaction(load_data, data)

driver.close()
