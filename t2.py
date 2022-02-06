print("Написать программу, которая упорядочивает файлы в директории")
print("по следующему принципу:")
print("Символ - должен стать символом / в пути к файлу pathlib")
import click
import logging
from pathlib import Path

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
def orderby():
    try:
        for i in Path('directory/').iterdir():
            a = i.parent / (i.stem.replace('-', '/') + '.txt')
            a.parent.mkdir(parents=True, exist_ok=True)
            i.rename(a)
        log.info("finish program orderby")
    except Exception as Ex:
     log.error(Ex)

cli.add_command(orderby)

if __name__ == '__main__':
    cli()