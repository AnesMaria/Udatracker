import pytest
from unittest.mock import Mock

from ..order_tracker import OrderTracker


# --- Fixtures for Unit Tests ---

@pytest.fixture
def mock_storage():
    """
    Provides a mock storage object for tests.
    This mock will be configured to simulate various storage behaviors.
    """
    mock = Mock()

    # By default, mock get_order to return None (no order found)
    mock.get_order.return_value = None

    # By default, mock get_all_orders to return an empty dict
    mock.get_all_orders.return_value = {}

    return mock


@pytest.fixture
def order_tracker(mock_storage):
    """
    Provides an OrderTracker instance initialized with the mock_storage.
    """
    return OrderTracker(mock_storage)


# --- Tests ---


def test_add_order_success(order_tracker, mock_storage):
    order = order_tracker.add_order(
        order_id="ORD-001",
        item_name="Laptop",
        quantity=1,
        customer_id="CUST-001"
    )

    assert order == {
        "order_id": "ORD-001",
        "item_name": "Laptop",
        "quantity": 1,
        "customer_id": "CUST-001",
        "status": "pending"
    }

    mock_storage.save_order.assert_called_once_with(
        "ORD-001",
        {
            "order_id": "ORD-001",
            "item_name": "Laptop",
            "quantity": 1,
            "customer_id": "CUST-001",
            "status": "pending"
        }
    )


def test_add_order_duplicate_id_raises_error(order_tracker, mock_storage):
    mock_storage.get_order.return_value = {
        "order_id": "ORD-001",
        "item_name": "Laptop",
        "quantity": 1,
        "customer_id": "CUST-001",
        "status": "pending"
    }

    with pytest.raises(ValueError, match="Order ID already exists"):
        order_tracker.add_order(
            order_id="ORD-001",
            item_name="Mouse",
            quantity=2,
            customer_id="CUST-002"
        )


def test_get_order_by_id_success(order_tracker, mock_storage):
    expected_order = {
        "order_id": "ORD-001",
        "item_name": "Laptop",
        "quantity": 1,
        "customer_id": "CUST-001",
        "status": "pending"
    }

    mock_storage.get_order.return_value = expected_order

    result = order_tracker.get_order_by_id("ORD-001")

    assert result == expected_order

    mock_storage.get_order.assert_called_with("ORD-001")

def test_get_order_by_id_not_found(order_tracker, mock_storage):
    mock_storage.get_order.return_value = None

    result = order_tracker.get_order_by_id("ORD-999")

    assert result is None
    mock_storage.get_order.assert_called_with("ORD-999")

def test_update_order_status_success(order_tracker, mock_storage):
    existing_order = {
        "order_id": "ORD-001",
        "item_name": "Laptop",
        "quantity": 1,
        "customer_id": "CUST-001",
        "status": "pending"
    }

    mock_storage.get_order.return_value = existing_order

    updated_order = order_tracker.update_order_status(
        "ORD-001",
        "shipped"
    )

    assert updated_order["status"] == "shipped"

    mock_storage.save_order.assert_called_with(
        "ORD-001",
        updated_order
    )

def test_update_order_status_not_found(order_tracker, mock_storage):
    mock_storage.get_order.return_value = None

    result = order_tracker.update_order_status(
        "ORD-999",
        "shipped"
    )

    assert result is None
    mock_storage.get_order.assert_called_with("ORD-999")

def test_list_all_orders(order_tracker, mock_storage):
    orders = {
        "ORD-001": {
            "order_id": "ORD-001",
            "item_name": "Laptop",
            "quantity": 1,
            "customer_id": "CUST-001",
            "status": "pending"
        },
        "ORD-002": {
            "order_id": "ORD-002",
            "item_name": "Mouse",
            "quantity": 2,
            "customer_id": "CUST-002",
            "status": "shipped"
        }
    }

    mock_storage.get_all_orders.return_value = orders

    result = order_tracker.list_all_orders()

    assert result == orders
    mock_storage.get_all_orders.assert_called_once()

def test_list_orders_by_status(order_tracker, mock_storage):
    orders = {
        "ORD-001": {
            "order_id": "ORD-001",
            "item_name": "Laptop",
            "quantity": 1,
            "customer_id": "CUST-001",
            "status": "pending"
        },
        "ORD-002": {
            "order_id": "ORD-002",
            "item_name": "Mouse",
            "quantity": 2,
            "customer_id": "CUST-002",
            "status": "shipped"
        },
        "ORD-003": {
            "order_id": "ORD-003",
            "item_name": "Keyboard",
            "quantity": 1,
            "customer_id": "CUST-003",
            "status": "pending"
        }
    }

    mock_storage.get_all_orders.return_value = orders

    result = order_tracker.list_orders_by_status("pending")

    assert result == [
        orders["ORD-001"],
        orders["ORD-003"]
    ]