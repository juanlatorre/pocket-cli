from pocket import Pocket, PocketException
import click

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
    p = Pocket(
	consumer_key='<Your Consumer Key>',
	access_token='<Your Access Token>'
    )

    print(pocket)
    #pocket.add(url)

if __name__ == "__main__":
    main()
