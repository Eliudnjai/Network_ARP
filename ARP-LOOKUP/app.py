import click

@click.group()
def cli():
    pass

@cli.command()
def fn():
    click.echo('Jane')


@cli.command()
def fm():
    click.echo('12:45:89:op:98')

cli.add_command(fn)
cli.add_command(fm)


# @click.command()
# @click.option("--count", default=1, help="Number of greetings")

# def hello(count):
#     for _ in range(count):
#         click.echo(f"Hello Sir!")


if __name__ == '__main__':
    cli()