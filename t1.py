print("CLI приложение, которое показывает сколько дней до НГ либо рандомнамя игрушка")
import click
import datetime
import random
from enum import Enum
import logging

logfile = './log_t1.log'

log = logging.getLogger("log")
log.setLevel(logging.INFO)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
FH.setFormatter(basic_formater)
log.addHandler(FH)


@click.group()
def cli():
    pass


@click.command()
@click.option('--hours', is_flag=True)
def newyear(hours):
    try:
        date1 = datetime.datetime.now()
        date2 = datetime.datetime(2023, 1, 1)
        delta = date2 - date1
        hours1 = delta.total_seconds() // 3600
        if hours:
            click.echo(print(f'{int(hours1 // 24)} дней и {int(hours1 % 24)} часов'))
        else:
            click.echo(print(f'{int(hours1 // 24)} дней'))
        log.info("finish program newyear")            
    except Exception as Ex:
      log.error(Ex)
@click.command()
def toy():
 try:
        class Toys(Enum):
            RED = "Red Ball"
            PURPLE = "Puple Angel"
        click.echo(print(random.choice(list(Toys)).value))
        log.info("finish program toy")
 except Exception as Ex:
  log.error(Ex)

cli.add_command(newyear)
cli.add_command(toy)

if __name__ == '__main__':
    cli()
