# Library Catalog System (Database Systems Course Project)

This repository contains a third-year bachelor project for the **Database Systems** course at the Canadian Institute of Technology.

The project models and implements a **Library Catalog System** with Microsoft SQL Server, plus a Django-based admin interface used to interact with the database tables.

## Project Scope

The system covers:
- Book and edition management
- Author and genre associations
- Member and librarian management
- Branch and shelf management
- Loans, reservations, and fines
- Reviews and availability tracking

## Main Entities

- `BOOK`
- `BOOK_EDITION`
- `AUTHOR`
- `AUTHORBOOKASSOCIATION`
- `GENRE`
- `BOOKGENREASSOCIATION`
- `LANGUAGE_`
- `PUBLISHER`
- `REVIEW`
- `AVAILABILITY_STATUS`
- `MEMBER_`
- `LOAN`
- `RESERVATION`
- `FINE`
- `SHELF`
- `LIBRARY_BRANCH`
- `LIBRARIAN`

## Deliverables Implemented

The project includes:
- Enterprise and business-rule definition
- ER design (Crow's Foot) and normalization work
- Data dictionary
- SQL Server DDL and DML
- Query set with joins and advanced SQL features
- View, stored function, stored procedures, and triggers
- Basic UI layer through Django admin

## Repository Tree

Recommended GitHub upload tree:

```text
project Database Systems/
├── .gitignore
├── README.md
├── Database Project ER diagram.png  (optional)
└── LIBRARYY/
    └── LIBRAR_SYSTEM/
        ├── manage.py
        ├── models.py
        ├── DATABASE_APP/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── tests.py
        │   ├── views.py
        │   └── migrations/
        │       ├── 0001_initial.py
        │       └── 0002_authgroup_authgrouppermissions_authpermission_and_more.py
        ├── LIBRAR_SYSTEM/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── templates/
```

## Tech Stack

- Database: Microsoft SQL Server
- ORM/UI layer: Django (Python)
- SQL features used: joins, subqueries, grouping, window functions, views, stored procedures, triggers

## Notes About the Current Codebase

- `DATABASE_APP/models.py` is mostly reverse-engineered (`managed = False`) and mapped to existing SQL Server tables.
- `DATABASE_APP/admin.py` registers the domain models for Django admin usage.
- `DATABASE_APP/views.py` is currently empty.
- `LIBRAR_SYSTEM/urls.py` currently exposes only the admin route (`/admin/`).
- SQL scripts were documented in the original course report, not in a separate `.sql` file in this repository.

## How To Run (Local)

1. Create the SQL Server database and tables using the SQL from the report.
2. Configure DB connection in `LIBRARYY/LIBRAR_SYSTEM/LIBRAR_SYSTEM/settings.py`:
   - `ENGINE = 'mssql'`
   - correct `HOST`, `NAME`, and ODBC driver for your machine
3. Install dependencies (at minimum):
   - `django`
   - `mssql-django`
   - `pyodbc`
4. Run:
   - `python manage.py runserver`
5. Open:
   - `http://127.0.0.1:8000/admin/`

## Team

Team details removed for privacy.
