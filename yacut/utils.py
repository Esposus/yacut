import random, string


SYMBOLS = string.ascii_letters + string.digits


def get_unique_short_url() -> str:
   return ''.join(random.choices(list(SYMBOLS), k=6))


def check_symbols(custom_id):
   for symbol in custom_id:
      if symbol not in SYMBOLS:
         return False
   return True