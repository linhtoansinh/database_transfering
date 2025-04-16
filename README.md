```bash
docker exec -it mongo mongosh --eval 'rs.initiate({_id: "rs0", members:[{_id: 0, host: "localhost:27017"}]})'
```