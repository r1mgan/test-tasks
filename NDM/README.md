# Resoult

I tested from my PC

```
avakhitov@T15p:~$ curl -H "X-Forwarded-For:8.8.8.8" http://127.0.0.1:8081
X-Forwarded-For: 172.18.0.1

avakhitov@T15p:~$ curl -H "X-Forwarded-For:8.8.8.8" http://127.0.0.1:8082
X-Forwarded-For: 172.18.0.1

avakhitov@T15p:~$ curl -H "X-Forwarded-For:8.8.8.8" http://127.0.0.1:8083
X-Forwarded-For: 172.18.0.1

avakhitov@T15p:~$ curl -H "X-Forwarded-For:8.8.8.8" http://127.0.0.1:8081/chain/
X-Forwarded-For: 172.18.0.1, 172.18.0.5, 172.18.0.4

avakhitov@T15p:~$ curl -H "X-Forwarded-For:8.8.8.8" http://127.0.0.1:8082/chain/
X-Forwarded-For: 172.18.0.1, 172.18.0.4

avakhitov@T15p:~$ curl -H "X-Forwarded-For:8.8.8.8" http://127.0.0.1:8083/chain/
X-Forwarded-For: 172.18.0.1
```