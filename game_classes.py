class GameObject:

    def __init__(self, name: str, appearance: str, feel: str, smell: str):
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
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(524, objects)

    def create_objects(self) -> list[GameObject]:
        return [
            GameObject(
                "Norminette Terminal",
                '''Norminette has delivered its verdict:

Error: TOO MANY FUNCTIONS (5)

Someone has written underneath:

"This number will haunt you."''',
                """The keyboard is warm.
Someone was coding here recently.

Or they're still here.""",
                """Hot electronics and fear.

Mostly fear.""",
            ),
            GameObject(
                "Coffee Cup",
                """Someone wrote \"42\" on the cup.

The 4 has been aggressively crossed out.

Only the 2 remains.

Understandable.""",
                """Stone cold.

This coffee died hours ago.""",
                "Strong enough to compile your thoughts.",
            ),
            GameObject(
                "Rubber Duck",
                """A small yellow rubber duck sits beside the keyboard.

Its blank stare suggests it has listened to several hours of debugging and knows things no duck should know.""",
                """You squeeze the rubber duck.

SQUEAK.

Finally, someone responds to your debugging questions.""",
                """It smells like rubber.

The only emotionally stable thing in this room.""",
            ),
            GameObject(
                "Hammock",
                """A hammock hangs in the corner.

Its shape suggests someone recently attempted to turn \"I'll rest for ten minutes\" into a full night's sleep.""",
                """Suspiciously warm.

You decide not to investigate further.""",
                """Energy drink,
sleep deprivation,
and poor time management.""",
            ),
            GameObject(
                "Forgotten Hoodie",
                """A black hoodie lies abandoned over a chair.

Naturally, it is black.

Identifying its owner among 42 students may be impossible.""",
                """You carefully poke it.

There does not appear to be a student inside.""",
                "You immediately regret implementing the sniff() method.",
            ),
            GameObject(
                "Whiteboard",
                """The whiteboard is covered in boxes,
arrows,
memory addresses,
and increasingly desperate question marks.

In the center someone has written:

SEGFAULT???

Three arrows point toward it.

None explain why.""",
                """The marker isn't dry yet.

Whoever understood this diagram may still be nearby.""",
                """Whiteboard marker.

For a brief moment you understand pointers.

The feeling passes.""",
            ),
            GameObject(
                "Plant",
                """Somehow the plant is still alive despite being maintained by programmers.

Its leaves are reaching desperately toward the window.""",
                """The soil is completely dry.

Apparently water() was never called.""",
                """It smells like the outside world.

You remember why you're trying to escape.""",
            ),
            GameObject(
                "Crumpled Exam Paper",
                """You unfold the crumpled exam paper.

Most of it has been furiously crossed out.

At the bottom one result remains painfully visible:

LEVEL 4 - FAILED

Someone has written

\"I WAS SO CLOSE\"

underneath.""",
                """The paper is deeply crumpled.

Whoever owned this processed their feedback physically.""",
                """Paper,
stress,
and the faint scent of a shattered ego.""",
            ),
            GameObject(
                "Vending Machine",
                """A vending machine stands against the wall.

You don't remember there being a vending machine here before.

Stranger still, it is filled almost entirely with chocolate bars.

Chocolate.

Next to computers.

Reckless.

A handwritten sign says:

MAXIMUM SNACK MODE.""",
                """The machine vibrates ominously.

You decide not to press anything.

You've debugged enough unfamiliar systems tonight.""",
                "Capitalism.",
            ),
        ]

    def find_game_object(self, name: str) -> GameObject | None:
        for game_object in self.room.game_objects:
            if game_object.name.lower() == name.lower():
                return game_object
        return None

    def show_help(self) -> None:
        print("""Available commands:
  look <object>
  touch <object>
  sniff <object>
  code <number>
  help
  quit""")

    def show_introduction(self) -> None:
        print("""It is 03:42.

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

        self.attempts += 1
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
        if command == "code":
            return self.try_code(argument)
        if command in ("look", "touch", "sniff"):
            if not argument:
                print(f"What would you like to {command}?")
                return False

            game_object = self.find_game_object(argument)
            if game_object is None:
                object_names = ", ".join(self.room.get_game_object_names())
                print(f"You cannot find '{argument}'. Try one of: {object_names}")
                return False

            action = getattr(game_object, command)
            print(action())
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
