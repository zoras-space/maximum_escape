import readline

from ascii_art import ASCII_ART, TITLE_ART


RED = "\033[31m"
GREEN = "\033[32m"
BROWN = "\033[33m"
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
CYAN = "\033[36m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
WHITE = "\033[97m"
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"


class GameObject:
    def __init__(
        self, name: str, appearance: str, feel: str, smell: str, color: str
    ) -> None:
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell
        self.color = color

    def get_colored_name(self) -> str:
        return f"{self.color}{self.name}{RESET}"

    def look(self) -> str:
        art = ASCII_ART[self.name].strip("\n")
        return f"{art}\n\nYou look at the {self.get_colored_name()}. {self.appearance}"

    def touch(self) -> str:
        return f"You touch the {self.get_colored_name()}. {self.feel}"

    def sniff(self) -> str:
        return f"You take a deep sniff of the {self.get_colored_name()}. {self.smell}"


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
                RED,
            ),
            GameObject(
                "Coffee Cup",
                (
                    "It's just your usual 42 cup. Nothing out of the ordinary.\n\n"
                    "The 4 has been aggressively crossed out.\n\n"
                    "Only the 2 remains.\n\n"
                    "Understandable."
                ),
                "Stone cold.\n\nThis coffee died hours ago.",
                "Strong enough to compile your thoughts.",
                BROWN,
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
                YELLOW,
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
                CYAN,
            ),
            GameObject(
                "Forgotten Hoodie",
                (
                    "A black hoodie lies abandoned over a chair.\n\n"
                    "Naturally, it is black and therefore not a 42 Hoodie.\n\n"
                    "Identifying its owner among 42 students may be impossible."
                ),
                (
                    "You carefully poke it.\n\n"
                    "There does not appear to be a student inside."
                ),
                "You immediately regret implementing the sniff() method.",
                GRAY,
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
                WHITE,
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
                GREEN,
            ),
            GameObject(
                "Crumpled Exam Paper",
                (
                    "You unfold the crumpled exam paper.\n\n"
                    "Most of it has been furiously crossed out.\n\n"
                    "At the bottom one result remains painfully visible:\n\n"
                    f"LEVEL 4 - {RED}FAILED{RESET}\n\n"
                    "Someone has written\n\n"
                    '"I WAS SO CLOSE"\n\n'
                    "underneath."
                ),
                (
                    "The paper is deeply crumpled.\n\n"
                    "Whoever owned this processed their feedback physically."
                ),
                "Paper,\nstress,\nand the faint scent of a shattered ego.",
                MAGENTA,
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
                BLUE,
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

    def get_completion_options(self) -> list[str]:
        if self.location == "door":
            return [
                "walk left",
                "walk right",
                "walk away",
                "code",
                "help",
                "quit",
            ]

        options = ["look around", "walk towards door", "help", "quit"]

        for game_object in self.get_nearby_objects():
            options.append(f"look at {game_object.name}")
            options.append(f"touch {game_object.name}")
            options.append(f"sniff {game_object.name}")

        return options

    def complete_command(self, text: str, state: int) -> str | None:
        matches = []
        for option in self.get_completion_options():
            if option.lower().startswith(text.lower()):
                matches.append(option)

        if state < len(matches):
            return matches[state]
        return None

    def setup_autocomplete(self) -> None:
        readline.set_completer_delims("")
        readline.set_completer(self.complete_command)
        backend = getattr(readline, "backend", None)
        if backend == "editline" or (
            backend is None and "libedit" in (readline.__doc__ or "")
        ):
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")

    def look_around(self) -> None:
        nearby_objects = self.get_nearby_objects()

        if not nearby_objects:
            print(
                f"You are facing the {ORANGE}locked door{RESET}. "
                "There are no objects here to inspect."
            )
            return

        print("Nearby objects:")
        for game_object in nearby_objects:
            print(f"  - {game_object.get_colored_name()}")

    def show_help(self) -> None:
        if self.location == "door":
            print(f"""Available commands:
  walk left
  walk right
  walk away
  {ORANGE}code <number>{RESET}
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
                print(
                    f"{ORANGE}You can only walk left, right, or away from the door.{RESET}"
                )
        elif direction == "towards door":
            self.location = "door"
            print(ASCII_ART["Door"].strip("\n"))
            print(f"You walk back towards the {ORANGE}locked door{RESET}.")
        else:
            print(
                f"{ORANGE}Walk towards the door before choosing another direction.{RESET}"
            )

    def show_introduction(self) -> None:
        print(TITLE_ART.strip("\n"))
        print(ASCII_ART["Door"].strip("\n"))
        print(f"""┌─────────────────────────────────────────────┐
│                                             │
│              42 BERLIN                      │
│                                             │
│      {BOLD}{ORANGE}MAXIMUM PRODUCTIVITY MODE{RESET}              │
│               {BOLD}{ORANGE}ENABLED{RESET}                       │
│                                             │
│             {BOLD}{ORANGE}[ LOCKED ]{RESET}                      │
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

{BOLD}{ORANGE}MAXIMUM PRODUCTIVITY MODE ENABLED.{RESET}

{ORANGE}ENTER 3-DIGIT EXIT CODE.{RESET}

{ORANGE}NO STUDENT LEAVES BEFORE REACHING THEIR MAXIMUM POTENTIAL.{RESET}

Fantastic.

Somewhere in this room are the clues you need to escape the dread of coding through the entire night.
""")
        self.show_help()

    def try_code(self, code_text: str) -> bool:
        if not code_text.isdigit() or len(code_text) != 3:
            print(
                f"{RED}Invalid code.{RESET} "
                "Please enter exactly 3 digits, for example: code 123"
            )
            return False

        if not self.room.check_code(int(code_text)):
            print(f"{RED}INCORRECT CODE.{RESET} Keep exploring the room.")
            return False

        victory_art = ASCII_ART["Victory"].strip("\n")
        print(f"{GREEN}{victory_art}{RESET}\n")
        print(f"""{GREEN}{BOLD}ACCESS GRANTED.{RESET}

{GREEN}The door clicks open.{RESET}

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
                print(f"{RED}Missing direction.{RESET} Where would you like to walk?")
                return False
            self.walk(argument)
            return False
        if command == "code":
            if self.location != "door":
                print(
                    f"{ORANGE}The code terminal is beside the locked door.{RESET} "
                    "You need to walk back towards it."
                )
                return False
            return self.try_code(argument)
        if command == "look" and argument.lower() == "around":
            self.look_around()
            return False
        if command == "look":
            if not argument.lower().startswith("at "):
                print(
                    f"{RED}Invalid look command.{RESET} "
                    "Use 'look around' or 'look at <object>'."
                )
                return False
            argument = argument[3:].strip()
        if command in ("look", "touch", "sniff"):
            if not argument:
                if command == "look":
                    print(f"{RED}Missing object.{RESET} What would you like to look at?")
                else:
                    print(
                        f"{RED}Missing object.{RESET} "
                        f"What would you like to {command}?"
                    )
                return False

            if self.location == "door":
                print(
                    f"{ORANGE}There is nothing here to inspect.{RESET} "
                    "Walk somewhere first."
                )
                return False

            game_object = self.find_game_object(argument)
            if game_object is None:
                object_names = ", ".join(
                    game_object.get_colored_name()
                    for game_object in self.get_nearby_objects()
                )
                print(
                    f"{RED}You cannot find '{argument}'.{RESET} "
                    f"Try one of: {object_names}"
                )
                return False

            if command == "look":
                print(game_object.look())
            elif command == "touch":
                print(game_object.touch())
            elif command == "sniff":
                print(game_object.sniff())
            return False

        print(
            f"{RED}Unknown command.{RESET} "
            "Type 'help' to see the available commands."
        )
        return False

    def run(self) -> None:
        self.setup_autocomplete()
        self.show_introduction()

        while True:
            try:
                user_input = input("\n> ")
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye.")
                break

            if self.handle_command(user_input):
                break
