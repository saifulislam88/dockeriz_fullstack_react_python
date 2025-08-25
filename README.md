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
git clone https://github.com/saifulislam88/dockeriz_fullstack_react_python.git
mv dockeriz_fullstack_react_python fs_app
cd fs_app
ls -ll
```

### 2. Image build and application starting

```bash
docker-compose build
docker image ls
docker-compose up -d                             # Run All Services
docker-compose ps                                # Running container or apps
docker-compose images                            #Check running images
```
<img width="2267" height="561" alt="image" src="https://github.com/user-attachments/assets/3dedaa90-ea17-4801-9717-01595a62628b" />

### 2. Image build and application starting












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




