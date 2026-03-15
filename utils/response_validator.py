def validate_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status {expected_status}, "
        f"but got {response.status_code}"
    )


def validate_json_key(response, key):
    data = response.json()
    assert key in data, f"Response JSON missing key: {key}"


def validate_json_value(response, key, expected_value):
    data = response.json()
    assert data[key] == expected_value, (
        f"Expected {key} to be {expected_value}, "
        f"but got {data[key]}"
    )