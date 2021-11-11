from faker import Faker
from pprint import pprint
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename = BASE_DIR / 'user.log', level=logging.INFO,filemode="w")


fake = Faker('fr_Fr')

def get_user():
    """Generate a single user

    Returns:
        str: user
    """
    logging.info('Generate user with first and last name ')
    return f'{fake.first_name()} {fake.last_name()}'


def get_users(number):
    
    """Generate multiples users

    Args:
        int: number

    Returns:
        users: str
    """
    logging.info(f'Generating {number} users')
    return [get_user() for _ in range(number)]

if __name__ == "__main__":
    user = get_users(8)
    print(user)
    
