class ItemRepository:
    def __init__(self):
        self.items = []

    def get_all_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
