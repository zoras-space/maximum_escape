class GameObject:

    def __init__(self, name: str, appearance: str, feel: str, smell: str):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):
        return f"You look at the {self.name}. {self.appearance}"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}"

    def sniff(self):
        return f"You take a deep sniff of the {self.name}. {self.smell}"

class Room:
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code: int):
        return code == self.escape_code

    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names

class Room:
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects
        self.room = Room(111, objects)

    def create_objects(self):
        return []