# -*- coding: utf-8 -*-

import click
import os
import boto3
from .cli import main


class AwsConnection(dict):

    def __init__(self):
        self._client = None
        super(AwsConnection, self).__init__()

    @property
    def client(self):
        if self._client is None:
            AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')
            self._client = boto3.client('secretsmanager', region_name=AWS_REGION)
        return self._client


def run():
    default_context = AwsConnection()

    try:
        return main(obj=default_context)
    except Exception as exc:
        click.secho(str(exc), fg='red')


if __name__ == '__main__':
    run()
