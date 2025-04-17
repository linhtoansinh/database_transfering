rs.initiate({_id: "rs0", members:[{_id: 0, host: "mongo"}]});

sleep(10000); // wait 10s for rs initiation

db.getSiblingDB("admin").createUser({
  user: "debezium",
  pwd: "password",
  roles: [
    { role: "read", db: "local" },       // access to the oplog
    { role: "read", db: "test" },        // access to your DB
    { role: "readAnyDatabase", db: "admin" } // sometimes needed
  ]
});
