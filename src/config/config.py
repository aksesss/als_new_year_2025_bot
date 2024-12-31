import os

token_path = os.path.join(os.path.abspath('.'), 'src/config/token.txt')

with open(token_path, 'r') as f:
    TOKEN = f.read()
