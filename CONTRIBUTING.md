# Contributing to TaskFlow Pro

Thank you for considering contributing to **TaskFlow Pro**! 🎉

We welcome contributions of all kinds — from bug fixes and feature requests to documentation improvements and ideas. This document outlines the process to help you get started smoothly.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md) (based on the Contributor Covenant). We expect respectful and inclusive communication from everyone.

---

## Quick Start for Contributors

### 1. Fork & Clone the Repository

```bash
git clone https://github.com/bundlab/taskflow-pro.git
cd taskflow-pro
```

### 2. Development Setup

#### Using Docker (Recommended)

```bash
# Start all services (PostgreSQL + Backend + Frontend)
docker compose up -d --build
```

- Backend (Swagger UI): http://localhost:8000/docs
- Frontend: http://localhost:5173

#### Local Development (Alternative)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## Development Workflow

### Branching Strategy

- `main` — Production-ready code (protected)
- `develop` — Integration branch (optional but recommended)
- Feature branches: `feature/short-description`
- Bug fixes: `bugfix/short-description`
- Docs: `docs/short-description`

```bash
git checkout -b feature/add-task-filter
```

### Commit Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation changes
- `refactor:` code refactoring
- `style:` formatting, missing semi-colons, etc.
- `test:` adding or updating tests
- `chore:` maintenance tasks

Example:
```bash
git commit -m "feat: add priority filtering to task list"
```

### Pull Request Process

1. Ensure your branch is up to date with `main`:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. Push your branch and open a PR:
   ```bash
   git push origin feature/your-feature
   ```

3. Fill the PR template completely.

4. Request review from maintainers.

5. Make requested changes and keep the PR updated.

---

## Project Structure

```text
taskflow-pro/
├── backend/                  # FastAPI + SQLModel
│   ├── app/
│   │   ├── api/             # endpoints
│   │   ├── core/            # config & security
│   │   ├── crud/            # database operations
│   │   ├── models/          # SQLModel models
│   │   ├── schemas/         # Pydantic models
│   │   └── main.py
│   └── tests/
├── frontend/                 # React 19 + Vite + TypeScript
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── services/
│   └── vite.config.ts
├── docker-compose.yml
└── .github/workflows/        # CI/CD
```

---

## Frontend Guidelines

- Use **TypeScript** for all new components
- Prefer **TanStack Query** for data fetching
- Component styling: Tailwind CSS (if added) or inline + CSS modules
- Run `npm run lint` and `npm run format` before committing
- Keep components small and reusable

---

## Backend Guidelines

- Use **SQLModel** for models
- Follow dependency injection pattern
- Add proper error handling and validation
- Write tests for new endpoints
- Run `ruff check .` and `ruff format .` before committing

---

## Testing

**Backend:**
```bash
cd backend
pytest -v
```

**Frontend:**
```bash
cd frontend
npm test          # (add Vitest/Jest later)
```

---

## Linting & Formatting

**Backend:**
```bash
ruff check --fix .
ruff format .
```

**Frontend:**
```bash
cd frontend
npm run lint
npm run format
```

---

## Docker & Environment

- Always test changes with `docker compose up --build`
- Update `docker-compose.yml` if you add new services
- Never commit real secrets — use `.env.example`

---

## How to Report Issues

1. Check if the issue already exists
2. Create a new issue using the appropriate template:
   - Bug Report
   - Feature Request
   - Documentation Improvement

Please include:
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if UI related)
- Environment (OS, Node version, Python version, Docker version)

---

## Thank You!

Your contributions make TaskFlow Pro better for everyone.  
Once your PR is merged, your name will appear in the [Contributors](https://github.com/bundlab/taskflow-pro/graphs/contributors) graph.

---

**Happy coding!** 💻

---