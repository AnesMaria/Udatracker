# Udatracker Starter Code

This directory contains the starter code for the Udatracker project. The initial structure of directories and files is described below.

```
.
├── backend# Udatracker – Order Tracking Service with TDD

## Project Overview

Udatracker is a small order tracking application built with Python and Flask.

The main goal of this project is to practice Test-Driven Development (TDD) while building a simple backend service. The development process follows the Red → Green → Refactor cycle:

1. Write or run a failing test.
2. Implement the minimum code needed to make the test pass.
3. Run the test again.
4. Refactor the code while keeping all tests passing.

The application allows users to:

- create a new order;
- retrieve an order by ID;
- update the status of an order;
- list all orders;
- filter orders by status.

The application uses in-memory storage, so all data is reset when the server restarts.

---

## Project Structure

```text
.
├── backend
│   ├── __init__.py
│   ├── app.py
│   ├── in_memory_storage.py
│   ├── order_tracker.py
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       ├── test_api.py
│       └── test_order_tracker.py
├── frontend
│   ├── css
│   │   └── style.css
│   ├── index.html
│   └── js
│       └── script.js
├── pytest.ini
└── README.md
│   ├── __init__.py
│   ├── app.py
│   ├── in_memory_storage.py
│   ├── order_tracker.py
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       ├── test_api.py
│       └── test_order_tracker.py
├── frontend
│   ├── css
│   │   └── style.css
│   ├── index.html
│   └── js
│       └── script.js
├── pytest.ini
└── README.md
```
