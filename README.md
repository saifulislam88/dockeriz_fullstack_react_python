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
