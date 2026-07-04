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
## Project Structure
```text
taskflow-pro/
├── backend/                  # FastAPI application
├── frontend/                 # React 19 + Vite + TypeScript
├── docker-compose.yml
├── .github/workflows/        # CI/CD
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── README.md
```
## Contributing
We love contributions! Whether it's bug fixes, new features, documentation, or just fixing a typo — every help counts.
Please read our **CONTRIBUTING.md** and **CODE_OF_CONDUCT.md** before submitting a Pull Request.

## Quick Contribution Steps
1. Fork the repository
2. Create a feature branch (```git checkout -b feature/amazing-feature```)
3. Commit your changes (```git commit -m 'feat: add amazing feature'```)
4. Push to the branch (```git push origin feature/amazing-feature```)
5. Open a Pull Request

## License
This project is licensed under the **MIT License** — see the **LICENSE** file for details.


## Author
bundlab


## Support
If you like this project:

* ⭐ Star the repository
* 🍴 Fork the project
* 🛠 Contribute improvements

---
