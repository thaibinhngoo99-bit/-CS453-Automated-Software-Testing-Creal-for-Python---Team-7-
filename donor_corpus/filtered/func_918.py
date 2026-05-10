def main():
    if len(sys.argv) < 3:
        print_usage()
        return 2
    try:
        quality_type = sys.argv[1]
        dataset_filepath = sys.argv[2]
    except ValueError:
        print_usage()
        return 2
    try:
        dataset = import_python_file(dataset_filepath)
    except Exception as e:
        print('Error: ' + str(e))
        return 1
    try:
        runner_class = QualityRunner.find_subclass(quality_type)
    except:
        print_usage()
        return 2
    result_store = FileSystemResultStore()
    run_remove_results_for_dataset(result_store, dataset, runner_class)
    return 0