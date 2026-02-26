from basics.context_manager import FileManager, DatabaseConnection


def test_file_manager(tmp_path):
    file_path = tmp_path / "test.txt"

    with FileManager(file_path, "w") as f:
        f.write("Hello")

    with FileManager(file_path, "r") as f:
        content = f.read()

    assert content == "Hello"


def test_database_connection():
    with DatabaseConnection() as conn:
        assert conn == "Database connected"