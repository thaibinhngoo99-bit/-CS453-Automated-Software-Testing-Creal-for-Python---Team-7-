def cleanup_threads_and_processes(quiet=True):
    for t in TMP_THREADS:
        t.stop(quiet=quiet)
    for p in TMP_PROCESSES:
        try:
            p.terminate()
        except Exception as e:
            print(e)
    clear_list(TMP_THREADS)
    clear_list(TMP_PROCESSES)