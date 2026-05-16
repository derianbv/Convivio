# **Prototipo Convivio**
Los archivos ejecutables actualmente son:
* [testing/pqrs_testing.py](testing/pqrs_testing.py) - Ejecuta y procesa una PQRS (creación y respuesta) de un Residente a la Administración, retorna el "registro" del procedimiento.
* [testing/reservation_testing.py](testing/reservation_testing.py) - Ejecuta y procesa una reserva de una "zona común", retorna el "registro" del procedimiento.
* [testing/property_testing.py](testing/property_testing.py) - Ejecuta y procesa la "creación" de una copropiedad con 3 "unidades", retorna el "contenido" del procedimiento.
* [testing/user_testing.py](testing/user_testing.py) - Ejecuta y procesa la llegada de 3 residentes a una "unidad", retorna el "registro" del procedimiento.



## **Database and Frontend Placeholder Files**

### **Configuration Module** (config)

| File | Status | Purpose |
|------|--------|---------|
| __init__.py | Stub | Module initialization file |
| database.py | **Partially Implemented** | PostgreSQL connection configuration with environment variables. Stores DB credentials, host, port, database name, and connection pool settings. Will be used by `DatabaseConnection` to establish and manage the database engine. |
| api.py | **Partially Implemented** | FastAPI server configuration including CORS settings for React frontend (localhost:3000). Defines API title, version, and allowed origins. Will be used by the main app.py to initialize the server. |

---

### **Infrastructure Module** (infrastructure)

| File | Status | Purpose |
|------|--------|---------|
| __init__.py | Stub | Module initialization file |
| db_connection.py | **Partially Implemented** | Database connection handler that creates and manages SQLAlchemy engine with connection pooling. Includes `test_connection()` method to validate PostgreSQL connectivity. Will be called during app startup to establish database connections. |
| database_session.py | **Partially Implemented** | SQLAlchemy session factory and dependency injector. Provides `get_db()` for FastAPI dependency injection and `DatabaseSession` context manager. Will be used in all route handlers to access the database. |

---

### **API Module** (api)

| File | Status | Purpose |
|------|--------|---------|
| __init__.py | Stub | Module initialization file |
| middleware.py | **Placeholder** | CORS and error handling middleware setup. Currently includes basic exception handlers. Will be expanded to add request/response logging, authentication, and request validation for React frontend communication. |
| routes.py | **Placeholder** | FastAPI route definitions. Contains health check endpoints and placeholder endpoints for users, properties, reservations, and PQRS. Will be expanded with full CRUD operations connected to business logic in service module. |

---

### **Main Application**

| File | Status | Purpose |
|------|--------|---------|
| app.py | **Partially Implemented** | Main FastAPI application entry point. Creates the app, sets up middleware, includes routes, and defines startup/shutdown events. Run with `python app.py` to start the backend server on http://localhost:8000. React frontend will call this API. |

---

### **Dependencies**

| File | Status | Purpose |
|------|--------|---------|
| requirements.txt | **Updated** | Python package dependencies including FastAPI, SQLAlchemy, psycopg2, uvicorn, and development tools. Run `pip install -r requirements.txt` to install all required packages. |

---

## **Quick Reference Table**

```
config/
├── __init__.py                          [Stub]
├── database.py                          [Partially Impl] → PostgreSQL config
└── api.py                               [Partially Impl] → FastAPI/CORS config

infrastructure/
├── __init__.py                          [Stub]
├── db_connection.py                     [Partially Impl] → DB engine manager
└── database_session.py                  [Partially Impl] → Session factory

api/
├── __init__.py                          [Stub]
├── middleware.py                        [Placeholder] → CORS/Error handling
└── routes.py                            [Placeholder] → API endpoints

app.py                                   [Partially Impl] → FastAPI main app
requirements.txt                         [Updated] → Dependencies
```

---

## **Implementation Notes for Collaborators:**

- **Placeholders** need endpoint implementations connected to the existing service layer (audit_service, pqrs_service, reservation_service)
- **Partially Implemented** files have core structure but need error handling refinement and validation
- **Stubs** (`__init__.py`) are ready as-is
- PostgreSQL must be running locally or accessible at configured host/port for app startup
- React frontend should be configured to call `http://localhost:8000/api/v1/*` endpoints
