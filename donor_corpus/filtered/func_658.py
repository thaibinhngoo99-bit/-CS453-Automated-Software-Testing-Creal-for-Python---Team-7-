@cli.command()
@click.option('-y', '--year', default=2020, type=int)
@click.option('-m', '--month', default=5, type=int)
@click.option('-d', '--day', default=30, type=int)
def prod(year, month, day):
    dataset = AirBnBDataset(year=year, month=month, day=day)
    model = build_model()
    model.train_estimator(dataset)
    model.save_estimator(prod=True)