from flask import request, jsonify


class ItemController:
    def __init__(self, item_repository):
        self.item_repository = item_repository

    def get_all_items(self):
        items = self.item_repository.get_all_items()
        return jsonify({"items": items})

    def add_item(self):
        item = request.get_json()
        self.item_repository.add_item(item)
        return "", 201

    def remove_item(self):
        item = request.get_json()
        self.item_repository.remove_item(item)
        return "", 204
