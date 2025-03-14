from neo4j import GraphDatabase

URI = "neo4j+s://9fb9060c.databases.neo4j.io"
AUTH = ("neo4j", "g1VvyGk8OI0Q7MmmjgcmS1lRQfmVyG-SfHA8tKDHEQk")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

class FraudDetection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self._test_connection()

    def _test_connection(self):
        """Verifies the connection before running queries"""
        try:
            with self.driver.session() as session:
                session.run("RETURN 1")  
            print("✅ Connection Verified: Successfully connected to Neo4j AuraDB!")
        except Exception as e:
            print(f"❌ Connection Error: {e}")
            exit(1)

    def detect_high_value_transactions(self):
        query = """
        MATCH (t:Transaction)-[:TRANSFERRED_TO]->(a:Account)
        WHERE t.amount > 100000
        RETURN t.id AS TransactionID, t.amount AS Amount, a.name AS Recipient
        """
        with self.driver.session() as session:
            result = session.run(query)
            print("\n🚨 Fraudulent Transactions Detected 🚨")
            for record in result:
                print(f"⚠️ Transaction ID: {record['TransactionID']} | Amount: ${record['Amount']} | Recipient: {record['Recipient']}")

if __name__ == "__main__":
    fraud_detector = FraudDetection(URI, "neo4j", "g1VvyGk8OI0Q7MmmjgcmS1lRQfmVyG-SfHA8tKDHEQk")
    fraud_detector.detect_high_value_transactions()
