# API Service

This is a Django REST Framework-based API service that implements a product catalog with hierarchical categories, customer management, and order processing.

## Features

- Hierarchical product categories (unlimited depth)
- Customer management
- Order processing
- OpenID Connect authentication
- SMS notifications via Africa's Talking
- Email notifications for administrators
- RESTful API endpoints
- Comprehensive test coverage
- CI/CD pipeline integration

## Tech Stack

- Python 3.11+
- Django 5.2.1
- Django REST Framework
- PostgreSQL
- Docker & Kubernetes
- OpenID Connect for authentication
- Africa's Talking SMS Gateway

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

---

## API & Admin Endpoints

### **Home Page**

- **`/`**
  - Displays the project’s home/welcome page.

### **Admin Panel**

- **`/admin/`**
  - Django Admin interface for managing users, products, orders, etc.
  - Requires superuser login.

### **OAuth2 Provider**

- **`/api/`** (OAuth2 endpoints)
  - Endpoints for OAuth2 authentication and token management.
  - Provided by `django-oauth-toolkit`.
  - Example endpoints:
    - `/api/authorize/`
    - `/api/token/`
    - `/api/revoke_token/`
  - See [django-oauth-toolkit docs](https://django-oauth-toolkit.readthedocs.io/en/latest/) for details.

### **Products API**

- **`/api/products/`**
  - Endpoints for managing products.
  - Example:
    - `GET /api/products/` — List products
    - `POST /api/products/` — Create a new product

### **Orders API**

- **`/api/orders/`**
  - Endpoints for managing orders.
  - Example:
    - `GET /api/orders/` — List orders
    - `POST /api/orders/` — Create a new order

---

**Note:**

- Some `/api/` endpoints may require authentication depending on your configuration.
- For more details, see the respective app’s documentation or browse the API using Django Admin.

---

## Testing

Run tests with coverage:

```bash
pytest --cov
```

## Deployment

This application is containerized using Docker and orchestrated with Kubernetes.  
For local development and testing, [Minikube](https://minikube.sigs.k8s.io/docs/) is used to run a local Kubernetes cluster.

- **Database:** PostgreSQL is deployed as a separate pod and accessed via a Kubernetes service.
- **Kubernetes:** All application components (Django app, PostgreSQL) are managed using Kubernetes manifests.
- **Minikube:** Provides a local environment to run and test the service application.

## License

MIT
