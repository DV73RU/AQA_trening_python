response = {
    "status_code": 200,
    "body": {
        "token": "abc123",
        "user_id": 42
    },
    "headers": {
        "Content-Type": "application/json",
        "Server": "nginx"
    }
}


if "headers" in response: # Если есть ключ в ответе
    return response["headers"] == response[""]