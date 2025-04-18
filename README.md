
# MongoDB + Debezium + Kafka Setup

## 1. Start Docker Compose

```bash
docker compose up -d
```

---

## 2. Initialize MongoDB Replica Set & Create User

Once the container is running, access the Mongo shell:

```bash
docker exec -it mongo mongosh
```

Initiate the replica set:

```javascript
rs.initiate({
  _id: "rs0",
  members: [{ _id: 0, host: "mongo" }]
});
```

Create the `debezium` user:

```javascript
use admin;
db.createUser({
  user: "debezium",
  pwd: "password",
  roles: [
    { role: "read", db: "local" },            // access to the oplog
    { role: "read", db: "test" },             // access to your DB
    { role: "readAnyDatabase", db: "admin" }  // sometimes needed
  ]
});
```

Set Change Stream Options:

```javascript
db.runCommand({
  setClusterParameter: {
    changeStreamOptions: {
      preAndPostImages: {
        expireAfterSeconds: 100
      }
    }
  }
});
```

Create the `products` collection and enable `preAndPostImages`:

```javascript
use test;
db.createCollection("products");

db.runCommand({
  collMod: "products",
  changeStreamPreAndPostImages: { enabled: true }
});
```

---

## 3. Create Kafka Connect Connectors

Post your connector config to Kafka Connect:

```bash
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" \
localhost:8083/connectors/ --data "@connectors/mongo_config.json"

curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" \
localhost:8083/connectors/ --data "@connectors/postgres_config.json"
```

---

## 4. Watch for Changes in Kafka (Optional)

Use this command to monitor change events:

```bash
kafka-console-consumer --bootstrap-server kafka:9092 --topic test.test.products --from-beginning
```

---

## 5. Perform MongoDB Operations

Perform `insert`, `update`, or `delete` operations on:

```
MongoDB: localhost:27017
Database: test
Collection: products
```

And observe real-time changes sync to:

```
PostgreSQL: localhost:5432
User: postgres
Password: postgres
Database: postgres
Table: test_test_products

```

_(Note: Sink connector configuration for the database name must still be set up.)_
