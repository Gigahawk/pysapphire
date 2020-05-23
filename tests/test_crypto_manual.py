from pysapphire.sapphire import Sapphire


def test_crypto_manual(sample_data):
    plain_text, key, encrypted_bytes = sample_data

    sph = Sapphire(key.encode())
    eb = []
    for b in plain_text.encode():
        eb.append(sph.encrypt(b))
    eb = bytearray(eb)
    assert eb == encrypted_bytes

    sph = Sapphire(key.encode())
    db = []
    for b in encrypted_bytes:
        db.append(sph.decrypt(b))
    db = bytearray(db)
    assert db == plain_text.encode()

