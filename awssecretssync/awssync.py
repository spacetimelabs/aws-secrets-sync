# -*- coding: utf-8 -*-

import json
import os
import sh

from awssecretssync.passeditor import PASS_CONTENT_FILE


def _save_to_passwordstore(secret_name, value):
    mysecret = open(PASS_CONTENT_FILE, 'w')
    mysecret.write('{}'.format(value))
    mysecret.close()
    os.environ["EDITOR"] = "secretssynceditor"
    cmd = sh.Command('pass')
    cmd("edit", secret_name)


def secrets_manager_to_passwordstore(client, secrets=[]):
    for secret in secrets:
        response = client.get_secret_value(SecretId=secret)
        value = response.get('SecretString', '{}')
        _save_to_passwordstore(secret, json.loads(value))


def list_secrets(client):
    response = client.list_secrets(MaxResults=64)
    secrets = response.get('SecretList', [])
    return [s.get('Name') for s in secrets]
