# Angular-Python

A simple full-stack application with:

* Angular 22 frontend
* Python FastAPI REST API
* REST API integration between Angular and Python
* One-command development startup using `concurrently`

## Project Structure

```text
angular-python/
├── angular-fe/          # Angular 22 frontend
├── python-be/           # Python FastAPI backend
├── .gitignore
├── package.json         # Root scripts for running both applications
└── README.md
```

## Requirements

Make sure the following are installed:

* Node.js
* npm
* Python 3.9+
* Angular CLI 22

Check your versions:

```bash
node --version
npm --version
python3 --version
ng version
```

## Installation

Clone the repository and enter the project directory:

```bash
git clone <your-repository-url>
cd angular-python
```

Install the root dependencies:

```bash
npm install
```

Install Angular dependencies:

```bash
cd angular-fe
npm install
cd ..
```

## Python FastAPI Setup

Go to the backend directory:

```bash
cd python-be
```

Create the Python virtual environment if it does not already exist:

```bash
python3 -m venv venv
```

Activate the virtual environment on macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the backend dependencies:

```bash
pip install fastapi uvicorn
```

Start FastAPI manually:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

Users API:

```text
http://127.0.0.1:8000/users
```

Stop the server with:

```text
CTRL + C
```

Deactivate the virtual environment when finished:

```bash
deactivate
```

## Angular Setup

Go to the Angular frontend:

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

The Angular `start` script should be:

```json
"start": "ng serve -o"
```

The `-o` option automatically opens Angular in the default browser.

## Run Angular + FastAPI Together

The project is configured to run both applications with a single command.

From the project root:

```bash
cd angular-python
npm start
```

The root `package.json` uses `concurrently` to start both services.

### What happens

```text
Angular
    ↓
http://localhost:4200

FastAPI
    ↓
http://127.0.0.1:8000
    ↓
Swagger automatically opens
http://127.0.0.1:8000/docs
```

You only need **one terminal**.

The root `package.json` contains:

```json
"scripts": {
  "start": "concurrently \"npm --prefix angular-fe start\" \"cd python-be && source venv/bin/activate && python -m uvicorn main:app --reload & sleep 2 && open http://127.0.0.1:8000/docs\""
}
```

The root development dependency is:

```json
"devDependencies": {
  "concurrently": "^10.0.5"
}
```

## API Endpoints

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/`           | API welcome message |
| GET    | `/health`     | Health check        |
| GET    | `/users`      | Get all users       |
| GET    | `/users/{id}` | Get a specific user |
| POST   | `/users`      | Create a user       |
| PUT    | `/users/{id}` | Update a user       |
| DELETE | `/users/{id}` | Delete a user       |

## Angular → FastAPI

The Angular application communicates with the FastAPI backend through HTTP requests.

Example:

```typescript
this.http.get<User[]>(
  'http://127.0.0.1:8000/users'
);
```

FastAPI allows requests from the Angular development server:

```text
http://localhost:4200
```

This is configured using FastAPI CORS middleware.

## Development Commands

### Start everything

From the root:

```bash
npm start
```

### Start Angular only

```bash
cd angular-fe
npm start
```

### Start FastAPI only

```bash
cd python-be
source venv/bin/activate
python -m uvicorn main:app --reload
```

### Stop everything

Press:

```text
CTRL + C
```

## Useful URLs

| Service      | URL                          |
| ------------ | ---------------------------- |
| Angular      | http://localhost:4200        |
| FastAPI      | http://127.0.0.1:8000        |
| Swagger UI   | http://127.0.0.1:8000/docs   |
| ReDoc        | http://127.0.0.1:8000/redoc  |
| Health Check | http://127.0.0.1:8000/health |
| Users API    | http://127.0.0.1:8000/users  |

## Notes

* The Python virtual environment is located at `python-be/venv/`.
* `venv/` is ignored by Git.
* Angular `node_modules/`, `.angular/`, and `dist/` are ignored by Git.
* Both applications can be developed independently or started together.
* `concurrently` allows Angular and FastAPI to run from a single terminal.
* FastAPI Swagger opens automatically when using the root `npm start` command.
* Angular opens automatically because its `start` script uses `ng serve -o`.

## Stop the Python Virtual Environment

If you manually activated the Python virtual environment:

```bash
deactivate
```

## Git

Check the current Git status:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Update README and project setup"
```

Push:

```bash
git push origin main
```
