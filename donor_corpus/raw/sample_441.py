from airbnb_priceforecaster.models import train_model
from airbnb_priceforecaster.models import build_model
from airbnb_priceforecaster.data import AirBnBDataset
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("-y", "--year", default=2020, type=int)
@click.option("-m", "--month", default=5, type=int)
@click.option("-d", "--day", default=30, type=int)
def train(year, month, day):
    result = train_model(year, month, day)
    click.echo(result)


@cli.command()
@click.option("-y", "--year", default=2020, type=int)
@click.option("-m", "--month", default=5, type=int)
@click.option("-d", "--day", default=30, type=int)
def prod(year, month, day):
    dataset = AirBnBDataset(year=year, month=month, day=day)
    model = build_model()

    model.train_estimator(dataset)
    model.save_estimator(prod=True)


if __name__ == '__main__':
    cli()
