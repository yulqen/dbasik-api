from typing import Optional

from starlette.requests import Request
from starlette.responses import Response

auth_key = 'dbasik_account'


def set_auth(response: Response, user_id: int):
    response.set_cookie(auth_key, str(user_id), secure=False,
                        httponly=True)  # this would be set to True in prod (when SSL used)


def get_user_id_from_auth_cookie(request: Request) -> Optional[int]:
    if auth_key not in request.cookies:
        return None

    user_id = int(request.cookies[auth_key])
    return user_id
