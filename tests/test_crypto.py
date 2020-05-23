from pysapphire.sapphire import encrypt, decrypt


def test_crypto(sample_data):
    plain_text, key, encrypted_bytes = sample_data

    assert encrypted_bytes == encrypt(
        key.encode(), plain_text.encode())
    assert plain_text.encode() == decrypt(
        key.encode(), encrypted_bytes)


