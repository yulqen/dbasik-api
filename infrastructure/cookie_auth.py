import hashlib
from typing import Optional

from starlette.requests import Request
from starlette.responses import Response

from infrastructure.num_convert import try_int

auth_cookie_name = 'dbasik_account'


def set_auth(response: Response, user_id: int):
    hash_val = _hash_text(str(user_id))
    val = "{}:{}".format(user_id, hash_val)
    response.set_cookie(auth_cookie_name, val, secure=False,
                        httponly=True, samesite='Lax')  # this would be set to True in prod (when SSL used)


def _hash_text(text: str) -> str:
    text = 'salty_' + text + '_text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_user_id_from_auth_cookie(request: Request) -> Optional[int]:
    if auth_cookie_name not in request.cookies:
        return None

    val = request.cookies[auth_cookie_name]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    user_id = parts[0]
    hash_val = parts[1]
    hash_val_check = _hash_text(user_id)
    if hash_val != hash_val_check:
        print("Warning: Hash mismatch, invalid cookie value")
        return None
    return try_int(user_id)


def logout(response: Response):
    response.delete_cookie(auth_cookie_name)