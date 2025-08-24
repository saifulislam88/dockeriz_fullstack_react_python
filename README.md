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
├── consumer/                    # Python consumer for RabbitMQ
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
├── .gitignore
└── README.md
```



## 🚀 Quick Start

### 1. Clone this Repository

```bash
git clone https://github.com/saifulislam88/dockeriz_fullstack_react_python.git
mv dockeriz_fullstack_react_python fs_app
cd fs_app



