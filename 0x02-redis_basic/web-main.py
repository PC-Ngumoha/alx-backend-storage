#!/usr/bin/env python3
import redis
import time

get_page = __import__('web').get_page


if __name__ == '__main__':
    url = 'http://slowwly.robertomurray.co.uk'
    # First Attempt at getting the page
    start = time.perf_counter()
    print(get_page(url)[:20])
    print('\nTime 1: {} seconds'.format(time.perf_counter() - start))
    time.sleep(3)
    print('\n\nAfter 3 seconds')
    # Second Attempt at getting the same page
    start = time.perf_counter()
    print(get_page(url)[:20])
    print('\nTime 2: {} seconds'.format(time.perf_counter() - start))
    time.sleep(15)
    print('\n\nAfter 15 seconds')
    start = time.perf_counter()
    print(get_page(url)[:20])
    print('\nTime 3: {} seconds'.format(time.perf_counter() - start))
    print('\n\n')

    r = redis.Redis()
    num_page_access = int(r.get('count:{}'.format(url)))
    print('The webpage: "{}" was accessed {} times'.format(
      url, num_page_access))