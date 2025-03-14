from neo4j import GraphDatabase


URI = "neo4j+s://9fb9060c.databases.neo4j.io"  
AUTH = ("neo4j", "g1VvyGk8OI0Q7MmmjgcmS1lRQfmVyG-SfHA8tKDHEQk")  

def test_neo4j_connection():
    try:
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            driver.verify_connectivity()  
            print("✅ Successfully connected to Neo4j AuraDB!")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

test_neo4j_connection()
