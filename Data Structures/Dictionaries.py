#dictionaries are sets of key:value pairs
my_group = [
    {"name": "Grant", "last_name": "Cooper", "fave_thing": "Car"},
    {"name": "Blume", "last_name": "Matthew", "fave_thing": "Terraria"},
    {"name": "Matthew", "last_name": "Blume", "fave_thing": "Minecraft"},
    {"name": "Max", "last_name": "Turner", "fave_thing": "Terraria"},
]


# class User:
#     def __init__(self, username: str, email: str):
#         self.username = username
#         self.email = email


from dataclasses import dataclass
@dataclass
class User:
    username: str
    email: str

user = User("Grant", "nnheo@example.com")