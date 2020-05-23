import pytest

@pytest.fixture
def sample_data():
    plain_text = "Hello World!"
    key = "123456"
    encrypted_bytes = bytearray([
        0x82, 0xb8, 0x82, 0x81, 0xf4, 0x63,
        0x79, 0x23, 0x1f, 0x43, 0x94, 0x20
    ])

    return plain_text, key, encrypted_bytes
