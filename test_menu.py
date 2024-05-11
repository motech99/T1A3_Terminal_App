import pytest
from menu import validate_name

def test_name_validation():
    # Valid name
    print("Running valid name test")
    assert validate_name('Mohammed') == None

    # Invalid name (empty string)
    print("Running empty string test")
    with pytest.raises(ValueError):
        validate_name('')

    # Invalid name (contains numbers)
    print("Running numbers test")
    with pytest.raises(ValueError):
        validate_name('undertaker12345WWE')

    # Invalid name (contains special characters)
    print("Running special characters test")
    with pytest.raises(ValueError):
        validate_name('tonystark@stark')
