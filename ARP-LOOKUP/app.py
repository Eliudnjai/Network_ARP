import click
import ip_addr
import mac_addr


@click.group()
def cli():
    pass

@cli.command()
def fn():
    name = ip_addr.GetHostName()
    click.echo(name)



@cli.command()
def fm():
    mac = mac_addr.get_mac_address()
    click.echo(mac)

# cli.add_command(fn)
# cli.add_command(fm)

# @click.command()
# @click.option("--all", default="No IP or MAC found", help="show you both name and mac address")

# def findall(all):
#     click.echo(fm)
#     click.echo(fn)

# @click.command()
# @click.option("--count", default=1, help="Number of greetings")

# def hello(count):
#     for _ in range(count):
#         click.echo(f"Hello Sir!")


if __name__ == '__main__':
    cli()
    # findall()