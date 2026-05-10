@click.command()
@click.option('--input_path', type=click.STRING, help='Path to input file')
@click.option('--output_path', type=click.STRING, help='Path to input file')
@click.option('--set_', type=click.Choice(['train', 'test']), help='set')
def preprocess(input_path, output_path, set_):
    """pre-process script

    :param input_path: path to input file
    :type input_path: str
    :param output_path: path to output file
    :type output_path: str
    :param set_: kind of data
    :type set_: str
    """
    if set_ == 'train':
        df = pd.read_csv(input_path, sep='|')
    else:
        df = pd.read_csv(input_path)
    df['clean_txt'] = df['Pregunta'].apply(lambda x: preprocess_f(x))
    df.to_csv(output_path, index=False)