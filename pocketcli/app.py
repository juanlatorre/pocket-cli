from pocket import Pocket, PocketException
import click

@click.group()
@click.option(
    "--consumer-key",
    "-c",
    envvar="POCKET_CONSUMER_KEY",
    help="Your Consumer Key for Pocket",
)
@click.option(
    "--access-token",
    "-a",
    envvar="POCKET_ACCESS_TOKEN",
    help="Your Access Token for Pocket",
)
def main(consumer_key, access_token):
    print(consumer_key, access_token)

@main.command()
@click.argument("url")
def add(url):
    """
    A little pocket tool that adds the url passed to Pocket.
    Made for personal use, tired of sending links from my pc to android,
    using Messenger or Whatsapp or Email.
    """
    click.echo(url)
    #pocket.add(url)

@main.command()
def config():
    print("config")

if __name__ == "__main__":
    main()
