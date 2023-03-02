from flask import Flask
from repository.item_repository import ItemRepository
from controller.item_controller import ItemController

app = Flask(__name__)

item_repository = ItemRepository()
item_controller = ItemController(item_repository)


@app.route("/", methods=["GET"])
def index():
    return "Hello world!"


@app.route("/items", methods=["GET"])
def get_all_items():
    return item_controller.get_all_items()


@app.route("/items", methods=["POST"])
def add_item():
    return item_controller.add_item()


@app.route("/items", methods=["DELETE"])
def remove_item():
    return item_controller.remove_item()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=7777,
        debug=True,
    )
