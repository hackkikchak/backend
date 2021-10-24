# from .helpers.fake_data import MAILBOX_NAMES
from .helpers.fake_data import MAILBOX_NAMES
from .helpers import string_translit
from .helpers import id_generator
import random


def get_fake_email(full_name: dict):
    """
    Возвращает рандомное ФИО
    """
    name = "".join([full_name[key] for key in full_name])
    translit_name = string_translit(name).replace("'", "")
    public_salt = id_generator()
    mailbox_name = random.choice(MAILBOX_NAMES)
    fake_email = f"{translit_name}" + f"{public_salt}" + f"@{mailbox_name}"
    return fake_email
