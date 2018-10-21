from pocket import Pocket, PocketException
import os, click

@click.group()
def main():
    pass

@main.command()
@click.argument("url")
@click.option(
    "--consumer-key",
    "-c",
    envvar="POCKET_CONSUMER_KEY",
    help="Your Consumer Key for Pocket",
    type=str
)
@click.option(
    "--access-token",
    "-a",
    envvar="POCKET_ACCESS_TOKEN",
    help="Your Access Token for Pocket",
    type=str
)
def add(url, consumer_key, access_token):
    """
    A little pocket tool that adds the url passed to Pocket.
    Made for personal use, tired of sending links from my pc to android,
    using Messenger or Whatsapp or Email.
    """
    pocket = Pocket(
        consumer_key=consumer_key,
	access_token=consumer_key
    )

    pocket.add(url)

@main.command()
@click.option(
    "--consumer-key",
    "-c",
    envvar="POCKET_CONSUMER_KEY",
    help="Your Consumer Key for Pocket",
    type=str
)
@click.option(
    "--access-token",
    "-a",
    envvar="POCKET_ACCESS_TOKEN",
    help="Your Access Token for Pocket",
    type=str
)
def config(consumer_key, access_token):
    """
    Store configuration values (consumer-key and access-token) in a file.
    """
    config_consumer_file = os.path.expanduser("~/.pocket_consumer_key.cfg")
    config_access_file = os.path.expanduser("~/.pocket_access_token.cfg")

    consumer_key = click.prompt(
        "Please enter your Pocket Consumer Key",
        default=consumer_key
    )

    access_token = click.prompt(
        "Please enter your Pocket Access Token",
        default=access_token
    )


    with open(config_consumer_file, "w") as ck:
        ck.write(consumer_key)

    with open(config_access_file, "w") as at:
        at.write(access_token)


if __name__ == "__main__":
    main()
