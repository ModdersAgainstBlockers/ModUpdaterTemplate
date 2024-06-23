import requests

from platforms.platform import Platform

modrinth_api = "https://api.modrinth.com/v2/project/"


class Modrinth(Platform):

    def __init__(self, platform_id, auth_token):
        super().__init__(platform_id, auth_token)

    def get_mod_body(self, mod_body: dict[str, str]):
        for mod_id in mod_body.keys():
            r = requests.get(modrinth_api + mod_id)
            if r.ok:
                json = r.json()
                if 'body' in json:
                    mod_body[mod_id] = json['body']

    def set_mod_body(self, mod_body: dict[str, str], auth_token: str):
        for mod_id, body in mod_body.items():
            if body:
                requests.patch(modrinth_api + mod_id, params={'body': body}, headers={'Authorization': auth_token})
