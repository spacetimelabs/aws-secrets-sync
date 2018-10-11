#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

from awssecretssync.awssync import list_secrets, secrets_manager_to_passwordstore


@click.group()
@click.pass_context
def main(ctx):
    return


@main.command(name='aws2pass')
@click.pass_context
def aws2pass(ctx):
    """
    Get secrets from AWS
    """

    click.secho('Reading AWS Secrets Manager...', fg='green')
    secrets = list_secrets(ctx.obj.client)
    click.secho('Saving secrets to Pass...', fg='green')
    secrets_manager_to_passwordstore(ctx.obj.client, secrets)
    click.secho('Saved: {}'.format(secrets))
