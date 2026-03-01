@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (0, 0, 0),
    ],
    ids=[
        "small_numbers",
        "same_numbers",
        "zeros"
    ]
)
def test_add_with_ids(a, b, expected):
    assert add(a, b) == expected

#fixtures and parametrize
#@pytest.mark.parametrize("role", ["admin", "user", "guest"])
#def test_user_roles(sample_user, role):
 #   sample_user["role"] = role
 #   assert sample_user["role"] in ["admin", "user", "guest"]