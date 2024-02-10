from bot.utilities import count_characters, token_count
from faker import Faker

def test_character_count():
    faker = Faker()
    text = faker.texts(nb_texts=1000)  # Generate text up to a maximum number of characters

    assert count_characters(text) == 1000


def test_token_count():
    assert token_count(21) == 6
    assert token_count(16) == 4
