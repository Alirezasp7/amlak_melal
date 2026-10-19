# Amlak Melal (Real Estate Platform)

A full-stack real estate platform featuring raw request management, consultant workflows, and public property listings.

## Repository Structure

This project is a monorepo containing both the backend API and the frontend client.

- `backend/`: Django REST Framework API (Python)
- `frontend/`: React single-page application (JavaScript/TypeScript)

## Getting Started

To run the full stack locally, you will need to open **two separate terminals**.

### 1. Backend (Django)

```bash
# Navigate to the backend folder
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Start the API server
python manage.py runserver
```

### 2. Frontend (React)

```bash
# In a new terminal, navigate to the frontend folder
cd frontend

# Install Node.js dependencies
npm install

# Start the Vite/React development server
npm run dev
```

## Local Development API Access

While developing locally, the React frontend can access the backend API at:

**Base API URL:** `http://127.0.0.1:8000/api/v1/`

**Public Filings Endpoint:** `http://127.0.0.1:8000/api/v1/core/public-filings/`

## Git & Commit Guidelines

To keep the repository clean and stable, we follow a strict branching and commit message standard. **Nobody pushes directly to `master`.**

## API Documentation

Swagger (OpenAPI) is used for interactive API documentation and updates automatically.

- **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
- **OpenAPI Schema (JSON):** `http://127.0.0.1:8000/api/schema/`

### Branching Rules
1. Always pull the latest code from `master` before starting new work.
2. Create a new branch for every specific task or feature:
   * `feature/frontend-home-page`
   * `feature/backend-publish-api`
   * `bugfix/image-url`
3. When finished, push your branch and open a **Pull Request** to merge into `master`.

### Commit Message Format
We use the **Conventional Commits** standard. This makes the Git history readable.
Format: `type: short description`

**Common Types:**
*   `feat:` A new feature for the user (e.g., `feat: build homepage property cards`)
*   `fix:` A bug fix (e.g., `fix: correct spacing on mobile view`)
*   `chore:` Updates to build tools, dependencies, or structure (e.g., `chore: update npm packages`)
*   `docs:` Changes to documentation (e.g., `docs: update readme setup steps`)
*   `refactor:` Rewriting code without changing its behavior (e.g., `refactor: move API call to separate file`)

**Examples:**
*   `feat(api): add jwt login endpoint`
*   `feat(ui): add contact agent button`
*   `fix: handle empty description on property page`


