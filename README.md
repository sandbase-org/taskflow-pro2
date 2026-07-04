# TaskFlow Pro

Modern full-stack task management application

**Backend**: FastAPI + SQLModel + PostgreSQL
**Frontend**: React 19 + TypeScript + Vite + TanStack Query
**Deployment-ready**: Docker + docker-compose + GitHub Actions

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-brightgreen)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19-blue)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.6+-blue)](https://www.typescriptlang.org/)


## Features

- JWT authentication (access + refresh tokens)
- Task CRUD with priority, status, due dates
- Clean React frontend with TanStack Query
- Role-based access (planned: admin / member)
- Dockerized backend + frontend + PostgreSQL
- GitHub Actions CI (lint + test)


## Quick Start (Development)

```bash
# 1. Clone & enter directory
git clone https://github.com/bundlab/taskflow-pro.git
cd taskflow-pro

# 2. Start everything with one command
docker compose up -d --build

# 3. Backend will be on → http://localhost:8000
#    Docs (Swagger) → http://localhost:8000/docs

# 4. Frontend will be on → http://localhost:5173
```

## Contributing

Contributions are welcome!
Feel free to submit pull requests.


## License

MIT License


## Author

Abdullahi Bundi


## Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork the project
* 🛠 Contribute improvements

---
