1. **docker**
```bash
docker compose up -d
```
2. **After the container started, init mongo rs and create a user**

```bash
docker exec -it mongo mongosh
```

```bash
rs.initiate({_id: "rs0", members:[{_id: 0, host: "mongo"}]})
```

```bash
use admin
db.createUser({
  user: "debezium",
  pwd: "password",
  roles: [
    { role: "read", db: "local" },       // access to the oplog
    { role: "read", db: "test" },        // access to your DB
    { role: "readAnyDatabase", db: "admin" } // sometimes needed
  ]
})
```

3. **Create mongo connector**
```bash
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ --data "@connectors/mongo_config.json"
```

4. **Watch for any changes updating to kafka**
```bash
kafka-console-consumer --bootstrap-server kafka:9092 --topic test.test.products --from-beginning
```