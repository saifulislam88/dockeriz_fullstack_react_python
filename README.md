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
├── backend/        # Flask backend
├── consumer/       # Python consumer for RabbitMQ
├── frontend/       # React frontend with nginx.conf
├── lb/             # Container based Nginx load balancer config
├── docker-compose.yml
├── .gitignore
└── README.md
```

project-root/
├── backend/
│   ├── app.py
│   └── Dockerfile
├── frontend/
│   ├── public/ (can be empty)
│   ├── src/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── Dockerfile
├── lb/
│   └── nginx.conf
├── docker-compose.yml
└── README.md




## 🚀 Quick Start

### 1. Clone this Repository

```bash
git clone https://github.com/saifulislam88/dockeriz_fullstack_react_python.git
mv dockeriz_fullstack_react_python fs_app
cd fs_app



