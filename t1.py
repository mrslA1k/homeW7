import click
import datetime
import random
from enum import Enum


@click.group()
def cli():
    pass

@click.command()
@click.option('--hours', is_flag=True)
def newyear(hours):
    date1= datetime.datetime.now()
    date2=datetime.datetime(2023,1,1)
    delta=date2-date1
    hours1 = delta.total_seconds()// 3600

    if hours:
        click.echo(print(f'{int(hours1//24)} дней и {int(hours1%24)} часов'))
    else:
        click.echo(print(f'{int(hours_1//24)} дней'))

cli.add_command(newyear)

@click.command()
def toy():
    class Toys(Enum):
        RED = "Red Ball"
        PURPLE = "Puple Angel"

    click.echo(print(random.choice(list(Toys)).value))

cli.add_command(toy)


if __name__ == '__main__':
    cli()