class GameObject:
    def __init__(self, name: str, appearance: str, feel: str, smell: str) -> None:
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self) -> str:
        return f"You look at the {self.name}. {self.appearance}"

    def touch(self) -> str:
        return f"You touch the {self.name}. {self.feel}"

    def sniff(self) -> str:
        return f"You take a deep sniff of the {self.name}. {self.smell}"


class Room:
    def __init__(self, escape_code: int, game_objects: list[GameObject]):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code: int) -> bool:
        return code == self.escape_code

    def get_game_object_names(self) -> list[str]:
        names = []
        for game_object in self.game_objects:
            names.append(game_object.name)
        return names


class Game:
    def __init__(self) -> None:
        objects = self.create_objects()
        self.room = Room(524, objects)
        self.location = "door"

        self.left_objects = objects[0:3]
        self.right_objects = objects[3:6]
        self.away_objects = objects[6:9]

    def create_objects(self) -> list[GameObject]:
        return [
            GameObject(
                "Norminette Terminal",
                (
                    "Norminette has delivered its verdict:\n\n"
                    "Error: TOO MANY FUNCTIONS (5)\n\n"
                    "Someone has written underneath:\n\n"
                    '"This number will haunt you."'
                ),
                (
                    "The keyboard is warm.\n"
                    "Someone was coding here recently.\n\n"
                    "Or they're still here."
                ),
                "Hot electronics and fear.\n\nMostly fear.",
            ),
            GameObject(
                "Coffee Cup",
                (
                    'Someone wrote "42" on the cup.\n\n'
                    "The 4 has been aggressively crossed out.\n\n"
                    "Only the 2 remains.\n\n"
                    "Understandable."
                ),
                "Stone cold.\n\nThis coffee died hours ago.",
                "Strong enough to compile your thoughts.",
            ),
            GameObject(
                "Rubber Duck",
                (
                    "A small yellow rubber duck sits beside the keyboard.\n\n"
                    "Its blank stare suggests it has listened to several hours "
                    "of debugging and knows things no duck should know.\n\n"
                    "Someone has stuck a tiny note beneath it:\n\n"
                    '"Start where the errors are."'
                ),
                (
                    "You squeeze the rubber duck.\n\n"
                    "SQUEAK.\n\n"
                    "Finally, someone responds to your debugging questions."
                ),
                (
                    "It smells like rubber.\n\n"
                    "The only emotionally stable thing in this room."
                ),
            ),
            GameObject(
                "Hammock",
                (
                    "A hammock hangs in the corner.\n\n"
                    "Its shape suggests someone recently attempted to turn "
                    '"I\'ll rest for ten minutes" into a full night\'s sleep.'
                ),
                "Suspiciously warm.\n\nYou decide not to investigate further.",
                "Energy drink,\nsleep deprivation,\nand poor time management.",
            ),
            GameObject(
                "Forgotten Hoodie",
                (
                    "A black hoodie lies abandoned over a chair.\n\n"
                    "Naturally, it is black.\n\n"
                    "Identifying its owner among 42 students may be impossible."
                ),
                (
                    "You carefully poke it.\n\n"
                    "There does not appear to be a student inside."
                ),
                "You immediately regret implementing the sniff() method.",
            ),
            GameObject(
                "Whiteboard",
                (
                    "The whiteboard is covered in boxes,\n"
                    "arrows,\n"
                    "memory addresses,\n"
                    "and increasingly desperate question marks.\n\n"
                    "In the center someone has written:\n\n"
                    "SEGFAULT???\n\n"
                    "Three arrows point toward it.\n\n"
                    "None explain why.\n\n"
                    "In one clear corner, another message reads:\n\n"
                    "ERROR → COFFEE → FAILURE\n\n"
                    "Beneath it:\n\n"
                    '"The natural progression of a 42 student."'
                ),
                (
                    "The marker isn't dry yet.\n\n"
                    "Whoever understood this diagram may still be nearby."
                ),
                (
                    "Whiteboard marker.\n\n"
                    "For a brief moment you understand pointers.\n\n"
                    "The feeling passes."
                ),
            ),
            GameObject(
                "Plant",
                (
                    "Somehow the plant is still alive despite being maintained "
                    "by programmers.\n\n"
                    "Its leaves are reaching desperately toward the window."
                ),
                "The soil is completely dry.\n\nApparently water() was never called.",
                (
                    "It smells like the outside world.\n\n"
                    "You remember why you're trying to escape."
                ),
            ),
            GameObject(
                "Crumpled Exam Paper",
                (
                    "You unfold the crumpled exam paper.\n\n"
                    "Most of it has been furiously crossed out.\n\n"
                    "At the bottom one result remains painfully visible:\n\n"
                    "LEVEL 4 - FAILED\n\n"
                    "Someone has written\n\n"
                    '"I WAS SO CLOSE"\n\n'
                    "underneath."
                ),
                (
                    "The paper is deeply crumpled.\n\n"
                    "Whoever owned this processed their feedback physically."
                ),
                "Paper,\nstress,\nand the faint scent of a shattered ego.",
            ),
            GameObject(
                "Vending Machine",
                (
                    "A vending machine stands against the wall.\n\n"
                    "You don't remember there being a vending machine here before.\n\n"
                    "Stranger still, it is filled almost entirely with chocolate bars.\n\n"
                    "Chocolate.\n\n"
                    "Next to computers.\n\n"
                    "Reckless.\n\n"
                    "A handwritten sign says:\n\n"
                    "MAXIMUM SNACK MODE."
                ),
                (
                    "The machine vibrates ominously.\n\n"
                    "You decide not to press anything.\n\n"
                    "You've debugged enough unfamiliar systems tonight."
                ),
                "Capitalism.",
            ),
        ]

    def find_game_object(self, name: str) -> GameObject | None:
        for game_object in self.get_nearby_objects():
            if game_object.name.lower() == name.lower():
                return game_object
        return None

    def get_nearby_objects(self) -> list[GameObject]:
        if self.location == "left":
            return self.left_objects
        if self.location == "right":
            return self.right_objects
        if self.location == "away":
            return self.away_objects
        return []

    def look_around(self) -> None:
        nearby_objects = self.get_nearby_objects()

        if not nearby_objects:
            print("You are facing the locked door. There are no objects here to inspect.")
            return

        print("Nearby objects:")
        for game_object in nearby_objects:
            print(f"  - {game_object.name}")

    def show_help(self) -> None:
        if self.location == "door":
            print("""Available commands:
  walk left
  walk right
  walk away
  code <number>
  help
  quit""")
        else:
            print("""Available commands:
  look around
  look at <object>
  touch <object>
  sniff <object>
  walk towards door
  help
  quit""")

    def walk(self, direction: str) -> None:
        direction = direction.lower()

        if self.location == "door":
            if direction == "left":
                self.location = "left"
                print("You walk to the left side of the room.")
            elif direction == "right":
                self.location = "right"
                print("You walk to the right side of the room.")
            elif direction == "away":
                self.location = "away"
                print("You turn away from the door and walk across the room.")
            else:
                print("You can walk left, right, or away from the door.")
        elif direction == "towards door":
            self.location = "door"
            print("You walk back towards the locked door.")
        else:
            print("Walk towards the door before choosing another direction.")

    def show_introduction(self) -> None:
        print("""┌─────────────────────────────────────────────┐
│                                             │
│              42 BERLIN                      │
│                                             │
│      MAXIMUM PRODUCTIVITY MODE              │
│               ENABLED                       │
│                                             │
│             [ LOCKED ]                      │
│                                             │
└─────────────────────────────────────────────┘

It is 03:42.
You should have gone home hours ago.

You are still at 42.

This was supposed to be a productive evening.

At some point,

\"I'll just fix one more thing\"

became several hours of debugging.

You decide enough is enough and walk toward the exit.

The door does not open.

A terminal beside it suddenly lights up.

MAXIMUM PRODUCTIVITY MODE ENABLED.

ENTER 3-DIGIT EXIT CODE.

NO STUDENT LEAVES BEFORE REACHING THEIR MAXIMUM POTENTIAL.

Fantastic.

Somewhere in this room are the clues you need to escape the dread of coding through the entire night.
""")
        self.show_help()

    def try_code(self, code_text: str) -> bool:
        if not code_text.isdigit() or len(code_text) != 3:
            print("Please enter a 3-digit code, for example: code 123")
            return False

        if not self.room.check_code(int(code_text)):
            print("INCORRECT CODE. Keep exploring the room.")
            return False

        print("""ACCESS GRANTED.

The door clicks open.

Cold night air hits your face.

You have escaped Maximum Productivity Mode.

Somewhere behind you,

the rubber duck squeaks.

You choose not to investigate.""")
        return True

    def handle_command(self, user_input: str) -> bool:
        parts = user_input.strip().split(maxsplit=1)
        if not parts:
            return False

        command = parts[0].lower()
        argument = parts[1].strip() if len(parts) == 2 else ""

        if command == "quit":
            print("You return to your computer. The door can wait.")
            return True
        if command == "help":
            self.show_help()
            return False
        if command == "walk":
            if not argument:
                print("Where would you like to walk?")
                return False
            self.walk(argument)
            return False
        if command == "code":
            if self.location != "door":
                print("The code terminal is beside the door. You need to walk back towards it.")
                return False
            return self.try_code(argument)
        if command == "look" and argument.lower() == "around":
            self.look_around()
            return False
        if command == "look":
            if not argument.lower().startswith("at "):
                print("Use 'look around' or 'look at <object>'.")
                return False
            argument = argument[3:].strip()
        if command in ("look", "touch", "sniff"):
            if not argument:
                if command == "look":
                    print("What would you like to look at?")
                else:
                    print(f"What would you like to {command}?")
                return False

            if self.location == "door":
                print("There is nothing here to inspect. Walk somewhere first.")
                return False

            game_object = self.find_game_object(argument)
            if game_object is None:
                object_names = ", ".join(
                    game_object.name for game_object in self.get_nearby_objects()
                )
                print(f"You cannot find '{argument}'. Try one of: {object_names}")
                return False

            if command == "look":
                print(game_object.look())
            elif command == "touch":
                print(game_object.touch())
            elif command == "sniff":
                print(game_object.sniff())
            return False

        print("Unknown command. Type 'help' to see the available commands.")
        return False

    def run(self) -> None:
        self.show_introduction()

        while True:
            try:
                user_input = input("\n> ")
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye.")
                break

            if self.handle_command(user_input):
                break
