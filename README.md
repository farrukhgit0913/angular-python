# Angular-Python

A simple full-stack application with:

* **Angular 22** frontend
* **Python FastAPI** REST API
* REST API integration between Angular and Python

## Project Structure

```text
python/
├── angular-fe/          # Angular 22 frontend
├── python-rest-api/     # Python FastAPI backend
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

Open Terminal and go to the API directory:

```bash
cd python-rest-api
```

### Create virtual environment

If the virtual environment does not already exist:

```bash
python3 -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet:

```bash
pip install fastapi uvicorn
```

### Start the API

```bash
uvicorn main:app --reload
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

Open a **new Terminal window/tab**.

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

### Terminal 1 — Python API

```bash
cd python-rest-api
source venv/bin/activate
uvicorn main:app --reload
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

Angular will call the Python API:

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

Python API:

```bash
uvicorn main:app --reload
```

Angular:

```bash
npm start
```

Both applications support live reload during development.
