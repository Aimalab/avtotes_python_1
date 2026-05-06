import pytest

@pytest.fixture(scope="session")
def browser():
    print()

    print("Браузер!")

    yield
    print("Close browser!")