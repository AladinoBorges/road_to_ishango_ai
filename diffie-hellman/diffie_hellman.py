import secrets


def get_random_number(prime_number: int) -> int:
    return secrets.choice(range(2, prime_number))


def private_key(p: int) -> int:
    return get_random_number(p)


def public_key(p: int, g: int, private: int) -> int:
    result: int = pow(g, private) % p

    return result


def secret(p: int, public: int, private: int) -> int:
    result: int = pow(public, private) % p

    return result
