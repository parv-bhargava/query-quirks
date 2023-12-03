# SQL Database Configuration
SQL_HOST = 'localhost:3306'
SQL_PORT = 3306
SQL_LH = 'localhost'
SQL_USER = 'root'
SQL_PASSWORD = 'password'
SQL_DB = 'anime'
TABLE_NAME = 'yellow_taxi_data'
QUERY = "SELECT * FROM yellow_taxi_data LIMIT 10"

# Neo4j Configuration
NEO4J_URI = 'bolt://localhost:7687'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'password'
NEO4J_TEST ='MATCH (n:Trip) RETURN n LIMIT 10'
BATCH_SIZE_NEO = 50000

# MongoDB Configuration
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = 'nyutaxi'
MONGO_COLLECTION = 'taxi'
MONGO_TEST = {}

TOTAL_RECORDS_LIMIT = 2000000
BATCH_SIZE = 1000000