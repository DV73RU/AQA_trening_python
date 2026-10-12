from dataclasses import dataclass,field

@dataclass
class User:
    count = 0
    name: str
    id: int = field(init=False)
    role: str = "user"
    registered: bool = True


    def __post_init__(self):
        User.count += 1
        self.id = User.count

user = User("Емелян")
print(user)
user2 = User("Коля")
print(user2)