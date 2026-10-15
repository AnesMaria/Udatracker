from flask import Flask, request, jsonify, send_from_directory

from backend.order_tracker import OrderTracker
from backend.in_memory_storage import InMemoryStorage


app = Flask(__name__, static_folder="../frontend")

in_memory_storage = InMemoryStorage()
order_tracker = OrderTracker(in_memory_storage)


@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)


@app.route("/api/orders", methods=["POST"])
def add_order_api():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    try:
        order = order_tracker.add_order(
            order_id=data["order_id"],
            item_name=data["item_name"],
            quantity=data["quantity"],
            customer_id=data["customer_id"],
            status=data.get("status", "pending"),
        )

        return jsonify(order), 201

    except KeyError as error:
        return jsonify(
            {"error": f"Missing required field: {error.args[0]}"}
        ), 400

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.route("/api/orders/<string:order_id>", methods=["GET"])
def get_order_api(order_id):
    order = order_tracker.get_order_by_id(order_id)

    if order is None:
        return jsonify({"error": "Order not found"}), 404

    return jsonify(order), 200


@app.route("/api/orders/<string:order_id>/status", methods=["PUT"])
def update_order_status_api(order_id):
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    if "new_status" not in data:
        return jsonify({"error": "Missing required field: new_status"}), 400

    try:
        updated_order = order_tracker.update_order_status(
            order_id,
            data["new_status"],
        )

        if updated_order is None:
            return jsonify({"error": "Order not found"}), 404

        return jsonify(updated_order), 200

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.route("/api/orders", methods=["GET"])
def list_orders_api():
    status = request.args.get("status")

    try:
        if status:
            orders = order_tracker.list_orders_by_status(status)
            return jsonify(orders), 200

        orders = order_tracker.list_all_orders()

        # Storage returns a dictionary; the API returns a list.
        return jsonify(list(orders.values())), 200

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)