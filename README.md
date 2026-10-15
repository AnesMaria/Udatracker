# Udatracker – Order Tracking Service with TDD

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
```

---

## Main Features

The application provides the following features:

- Create a new order.
- Retrieve an order by its ID.
- Update the status of an existing order.
- List all stored orders.
- Filter orders by status.
- Return JSON responses through a Flask REST API.
- Use a simple frontend interface to interact with the API.

Each order contains the following fields:

```text
order_id
item_name
quantity
customer_id
status
```

A newly created order receives the default status:

```text
pending
```

---

## Supported Order Statuses

The application supports the following order statuses:

```text
pending
processing
shipped
delivered
cancelled
```

---

## Test-Driven Development Approach

This project was developed using a test-first approach.

Instead of implementing all features at once, I worked progressively by focusing on one behavior at a time.

For each feature, I followed the same process:

1. Write or run a test that describes the expected behavior.
2. Confirm that the test fails.
3. Implement the minimum code required to make it pass.
4. Run the tests again.
5. Refactor the implementation when needed.

This approach made the development process easier to manage and helped identify problems early.

---

## Unit Tests

The unit tests are located in:

```text
backend/tests/test_order_tracker.py
```

They verify the main behaviors of the `OrderTracker` class, including:

- adding a new order;
- preventing duplicate order IDs;
- retrieving an existing order;
- handling a non-existing order;
- updating an order status;
- handling an update for a non-existing order;
- listing all orders;
- filtering orders by status.

Mock storage is used in the unit tests so that the business logic can be tested independently from the storage implementation.

---

## Integration Tests

The API integration tests are located in:

```text
backend/tests/test_api.py
```

These tests verify that the Flask routes behave correctly and return the expected JSON responses and HTTP status codes.

The integration tests cover operations such as:

- creating an order;
- retrieving an order;
- updating an order status;
- listing all orders.

---

## Running the Tests

Tests should be run from the project root.

To run the complete test suite:

```bash
pytest
```

To run only the unit tests:

```bash
pytest backend/tests/test_order_tracker.py
```

To run only the API integration tests:

```bash
pytest backend/tests/test_api.py
```

At the end of development, the full test suite passes successfully.

---

## Installation

The Udacity Workspace already provides the required environment and dependencies.

If running the project locally, install the required dependencies with:

```bash
pip install -r backend/requirements.txt
```

---

## Running the Application

From the project root, start the Flask application with:

```bash
python -m backend.app
```

The application runs on port 5000.

For local development, open:

```text
http://127.0.0.1:5000
```

When using the Udacity Workspace, the Flask application can be accessed through the forwarded port provided by the Workspace.

---

## REST API

### Create an Order

**Endpoint**

```text
POST /api/orders
```

Example request:

```json
{
  "order_id": "ORD100",
  "item_name": "Laptop",
  "quantity": 1,
  "customer_id": "CUST100"
}
```

Example response:

```json
{
  "order_id": "ORD100",
  "item_name": "Laptop",
  "quantity": 1,
  "customer_id": "CUST100",
  "status": "pending"
}
```

---

### Get an Order

**Endpoint**

```text
GET /api/orders/<order_id>
```

Example:

```text
GET /api/orders/ORD100
```

If the order exists, the API returns the order as JSON.

If the order does not exist, the API returns a 404 response.

---

### Update Order Status

**Endpoint**

```text
PUT /api/orders/<order_id>/status
```

Example request:

```json
{
  "new_status": "shipped"
}
```

The API returns the updated order when the operation succeeds.

---

### List All Orders

**Endpoint**

```text
GET /api/orders
```

This endpoint returns all currently stored orders.

---

### Filter Orders by Status

**Endpoint**

```text
GET /api/orders?status=<status>
```

Example:

```text
GET /api/orders?status=shipped
```

This endpoint returns only the orders matching the selected status.

---

## Example curl Commands

Create an order:

```bash
curl -X POST http://127.0.0.1:5000/api/orders \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": "ORD100",
    "item_name": "Laptop",
    "quantity": 1,
    "customer_id": "CUST100"
  }'
```

Retrieve an order:

```bash
curl http://127.0.0.1:5000/api/orders/ORD100
```

Update an order status:

```bash
curl -X PUT http://127.0.0.1:5000/api/orders/ORD100/status \
  -H "Content-Type: application/json" \
  -d '{"new_status":"shipped"}'
```

List all orders:

```bash
curl http://127.0.0.1:5000/api/orders
```

Filter orders by status:

```bash
curl "http://127.0.0.1:5000/api/orders?status=shipped"
```

---

## Frontend

The project includes a simple frontend located in the `frontend/` directory.

The interface allows the user to:

- add a new order;
- retrieve an order;
- update an order status;
- display all orders;
- filter orders by status.

The frontend communicates with the Flask REST API using JavaScript `fetch()` requests.

---

## Storage

The project uses an in-memory storage implementation.

This keeps the application simple and makes it easy to test.

Because the data is stored only in memory, all orders are lost when the Flask server restarts.

A future improvement would be to replace the in-memory storage with persistent storage such as SQLite or PostgreSQL.

---

## Reflection

One design decision I made was to keep the business logic inside the `OrderTracker` class and keep the Flask routes focused mainly on handling HTTP requests and responses. This separation made the code easier to understand and test.

One important lesson from this project was how useful small and focused tests can be. When a test failed, it was usually easier to understand which behavior needed to be corrected instead of debugging the entire application at once.

If I continued improving this project, I would add persistent storage, stronger input validation, more complete error handling, and a DELETE endpoint so that orders could also be removed.

---

## Possible Future Improvements

Some possible improvements for the project include:

- persistent database storage;
- stricter input validation;
- centralized API error handling;
- DELETE support for removing orders;
- filtering by customer ID;
- additional unit and integration tests;
- API documentation using OpenAPI or Swagger;
- Docker support for local deployment.

---

## Conclusion

This project helped reinforce the main ideas behind Test-Driven Development and REST API development.

By following the Red → Green → Refactor cycle, each feature was implemented in small steps and verified with automated tests before moving to the next feature.
