# kong-demo

This repo aims to test kong with a REST backend API

The backend is a simple CRUD for creating users and adding trips to them via API

To use it:
- cd tripsme
- docker stack deploy -c docker-compose.yml backend
- cd ..
- cd kong 
- docker stack deploy -c docker-compose.yml kong

It will create 4 swarm services
You can access to tripsme api by http://{localIP}:6622/user/{id} for retreive a user or
http://{localIP}/user with parameters using POST for creating


