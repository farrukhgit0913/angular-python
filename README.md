# Angular-Python

A simple full-stack application with:

* **Angular 22** frontend
* **Python FastAPI** REST API
* REST API integration between Angular and Python

## Project Structure

```text
angular-python/
├── angular-fe/          # Angular 22 frontend
├── python-be/           # Python FastAPI backend
├── .gitignore
└── README.md
```

## Requirements

Make sure you have installed:

* Node.js
* npm
* Python 3.9+
* Angular CLI 22

Check versions:

```bash
node --version
npm --version
python3 --version
```

## 1. Run Python FastAPI API

Open Terminal and go to the backend directory:

```bash
cd python-be
```

### Create Virtual Environment

If the virtual environment does not already exist:

```bash
python3 -m venv venv
```

### Activate Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

After activation, you should see `(venv)` in your terminal prompt.

### Install Dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet:

```bash
pip install fastapi uvicorn
```

### Start FastAPI

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### API URLs

Health check:

```text
http://127.0.0.1:8000/health
```

Users:

```text
http://127.0.0.1:8000/users
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 2. Run Angular Frontend

Open a **new Terminal window or tab**.

Go to the Angular project:

```bash
cd angular-fe
```

Install dependencies:

```bash
npm install
```

Start Angular:

```bash
npm start
```

The Angular application will be available at:

```text
http://localhost:4200
```

## 3. Run Both Projects

You need **two terminals**.

### Terminal 1 — Python FastAPI

```bash
cd python-be
source venv/bin/activate
python -m uvicorn main:app --reload
```

### Terminal 2 — Angular

```bash
cd angular-fe
npm start
```

Then open:

```text
http://localhost:4200
```

Angular will communicate with the Python API:

```text
http://127.0.0.1:8000/users
```

## API Endpoints

| Method | Endpoint      | Description    |
| ------ | ------------- | -------------- |
| GET    | `/`           | API status     |
| GET    | `/health`     | Health check   |
| GET    | `/users`      | Get all users  |
| GET    | `/users/{id}` | Get user by ID |
| POST   | `/users`      | Create user    |
| PUT    | `/users/{id}` | Update user    |
| DELETE | `/users/{id}` | Delete user    |

## Angular → FastAPI

The Angular application uses Angular's `HttpClient` to communicate with the FastAPI backend.

Example:

```ts
this.http.get<User[]>('http://127.0.0.1:8000/users')
```

FastAPI must allow requests from the Angular development server:

```text
http://localhost:4200
```

CORS is configured in the FastAPI application.

## Development

### Python API

```bash
cd python-be
source venv/bin/activate
python -m uvicorn main:app --reload
```

### Angular

```bash
cd angular-fe
npm start
```

Both applications support live reload during development.

## Deactivate Python Virtual Environment

When you are finished working with the Python backend:

```bash
deactivate
```

This returns your terminal to the normal system Python environment.
