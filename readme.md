# QuickShop — INF601 Mini Project 6 (Django Application)

**Author:** Gabriel Itegbe
**Course:** INF601 — Advanced Programming in Python

---

## Overview

**QuickShop** is a Django web application that works as a small e-commerce product catalog, with personal user wishlists and a dedicated administrator dashboard.

- **Public users** can browse the catalog and view detailed product descriptions.
- **Registered users** can log in and save products to a personal wishlist.
- **Staff and administrators** get a custom Admin Management Dashboard for full **CRUD** (Create, Read, Update, Delete) operations on store inventory, directly from the web interface.

---

## Features & Requirements Met

| Requirement | Implementation |
|---|---|
| **Django project architecture** | Modular structure with a `core` settings package and a `mainapp` application |
| **5+ templated pages** | Responsive pages using template inheritance from `base.html` (see below) |
| **Interactive forms** | `ProductForm` for adding/editing products; `UserCreationForm` for account registration |
| **Authentication system** | Account creation, login redirection, and protected views for wishlist toggles and admin pages |
| **Bootstrap 5 UI** | Responsive grids, navbar, styled tables, badges, and a Bootstrap modal for store policies |
| **Django Admin customization** | Custom admin display settings with search, filters, and field ordering |

### Templates

| Page | Template |
|---|---|
| Home | `home.html` |
| Product Catalog | `product_list.html` |
| Product Detail | `product_detail.html` |
| User Wishlist | `wishlist.html` |
| User Registration | `register.html` |
| User Login | `login.html` |
| Admin CRUD Management | `admin_dashboard.html`, `admin_product_form.html`, `admin_product_confirm_delete.html` |

---

## Installation

### Prerequisites

- Python 3.x
- Git

### 1. Clone the repository

```bash
git clone <repository-url>
cd miniproject6gabrielitegbe
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows (Command Prompt / PowerShell):**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Prepare the local SQLite database and create an administrator account:

```bash
# Generate migration files
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser (admin) account
python manage.py createsuperuser
```

---

## Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

Then open your browser to:

| Interface | URL |
|---|---|
| Web App | <http://127.0.0.1:8000/> |
| Django Admin Panel | <http://127.0.0.1:8000/admin/> |

---

## AI Usage

In accordance with the course AI Use Policy, this section describes how AI tools were used during development of Mini Project 6.

### Where I Used AI

- **Architecture planning:** Brainstormed project ideas that met all requirements and outlined the initial Django directory structure.
- **Debugging:** Diagnosed runtime and setup errors, including:
  - SSL certificate handshake failures during `pip install`
  - A post-login redirect to `/accounts/profile/` returning a 404
  - A missing import (`NameError: ProductForm`)
- **Boilerplate generation:** Produced starter Bootstrap templates and basic Django URL routing.
- **Documentation:** Reformatted and polished this `README.md`.

### What AI Provided

- Starter template snippets using Bootstrap 5 classes and modal markup.
- Standard Django code structures (`models.Model`, `admin.ModelAdmin`, and view functions).
- Troubleshooting suggestions, such as the `--trusted-host` pip flag and the `LOGIN_REDIRECT_URL` setting in `core/settings.py`.

### Changes I Made

- **App customization:** Renamed the generic app to `mainapp` and tailored the data models (`Product`, `WishlistItem`) to an e-commerce catalog.
- **Front-end admin CRUD:** Went beyond the built-in Django admin by building a custom staff dashboard (`admin_dashboard_view`) with full CRUD routes and templates.
- **Forms and layout:** Added JavaScript helpers to apply Bootstrap classes to the registration and login forms, updated button styling, and secured views with `@staff_member_required`.
- **Review and debugging:** Reviewed, restructured, and manually debugged all generated code to meet the project header guidelines and run cleanly.