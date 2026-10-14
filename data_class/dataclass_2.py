from dataclasses import dataclass, field


@dataclass
class ApiCredentials:
    username:str
    password:str = field(repr=False)
    environment:str =field(default="DEV")


api_cred = ApiCredentials("user1","pass")
print(api_cred)

credentials = ApiCredentials("admin", "secret123", "STAGE")

print(credentials)
print(credentials.password)