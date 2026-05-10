@retry(wait_exponential_multiplier=1000, wait_exponential_max=ONE_HOUR * 6)
def fetch(url):
    global s
    d = time.time() - s
    print('time: ' + str(d))
    s = time.time()
    try:
        with urlopen(url) as response:
            result = response.read().decode('utf8')
            print('Done fetching...')
            return result
    except urllib.error.URLError as e:
        print('Error: ' + str(e))
        raise e