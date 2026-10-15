from dataclasses import dataclass, field


@dataclass
class ApiResponse:
    url: str
    status_code: int = 200
    response_time: float = 0.0

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code <= 299

response = ApiResponse("https://example.com", 200, 0.5)

print(response.is_success)  # True

response.status_code = 404
print(response.is_success)  # False

response.status_code = 201
print(response.is_success)  # True
