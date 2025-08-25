## 🐳 Full Stack Docker App with RabbitMQ, PostgreSQL, Flask, React, Nginx Load Balancer

### 📦 Components
- **PostgreSQL** (with pgAdmin)
- **RabbitMQ** (with Management UI)
- **Flask** Backend (Python)
- **React** Frontend(with nginx.conf)
- **Nginx** Load Balancer
- **Consumer** (RabbitMQ message listener)

## Project Structure

```bash
dockeriz_fullstack_react_python/
├── backend/                     # Flask backend
│   ├── app.py
│   └── Dockerfile
├── consumer/
│   ├── app.py
│   └── Dockerfile               # Python consumer for RabbitMQ
├── frontend/                    # React frontend with nginx.conf
│   ├── public/ (can be empty)
│   ├── src/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   ├── node_modules/
│   └── Dockerfile
│   └── nginx.conf
├── lb/                         # Container based Nginx load balancer config
│   └── nginx.conf
├── docker-compose.yml
└── db_data/ (host bind mount for db)
├── .gitignore
└── README.md
```



## 🚀 Quick Start

### 1. Clone this Repository

```bash
cd /home/saiful/
git clone https://github.com/saifulislam88/dockeriz_fullstack_react_python.git
mv dockeriz_fullstack_react_python fs_app
cd fs-app
ls -ll
```

**Note:** `docker-compose` related all command must execute from respective project directory such as `/home/saiful/fs-app`

### 2. Image build and application starting

```bash
docker-compose build                             # Imaage building
docker image ls                                  # View all images
docker-compose up -d                             # Run All Services
docker-compose ps                                # Running container or apps
docker-compose images                            # Check running images
```
<img width="2267" height="561" alt="image" src="https://github.com/user-attachments/assets/3dedaa90-ea17-4801-9717-01595a62628b" />

Note: all containers and service are running. So chekc the services.

### 3. Check frontend application and insert data in db

http://192.168.1.107/             # Browse `frontend` application using own IP

<img width="973" height="198" alt="image" src="https://github.com/user-attachments/assets/fa753d1e-01fd-455a-9c29-0ab8a704f875" />


### 4. Backend service check

```bash 
docker-compose exec backend curl -X POST -v http://backend:5000/api/submit
```
**Error:** OCI runtime exec failed: exec failed: unable to start container process: exec: "curl": executable file not found in $PATH: unknown

- Temporarily install curl inside the backend container
```bash
docker-compose exec backend bash
curl -X POST -v http://localhost:5000/api/submit
apt update && apt install -y curl               # You can also install curl package permanently from backend Dockerfile
```

```bash
docker-compose exec backend curl -X POST -v http://backend:5000/api/submit
```
```bash
docker-compose exec backend curl -X POST -H "Content-Type: application/json" -d '{"name": "saiful", "email": "saiful@example.com", "batch": "n5"}' http://backend:5000/api/submit
```





Successfully built eafd50c5bae3
Successfully tagged fs_app_consumer:latest
-
fs_app_backend
fs_app_consumer
fs_app_frontend
fs_app_lb
fs_app_postgres
pgadmin






### 3. Clone this Repository




docker-compose up --build                        # Live Code Changes (Dev Tip)
docker compose build frontend
docker-compose down -v --rmi all                 # Clean Previous Volumes & Images
docker-compose down -v
docker-compose down --volumes --remove-orphans   #Rebuild
docker-compose down -v --remove-orphans
docker-compose build --no-cache                  #Rebuild
docker-compose up --force-recreate               #Rebuild
docker-compose up --build -d
docker logs -f <container_id>

```




