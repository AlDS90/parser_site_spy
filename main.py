import requests as r
import bs4
import random as rnd
import time as t


def get_html(url: str = None,
             ua: dict = None,
             px: dict = None) -> str:
    return r.get(url, headers=ua, proxies=px).text


def get_ip(html: str = None) -> tuple:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    return ip, ua


def main():
    t_start = t.time()
    url = 'http://sitespy.ru/my-ip'
    with open('parser_data/user_agents.txt') as uas_file,\
         open('parser_data/proxies.txt') as pxs_file:
        uas = uas_file.read().split('\n')
        pxs = pxs_file.read().split('\n')
    while True:
        px = {'http': 'http://' + rnd.choice(pxs)}
        ua = {'User-Agent': rnd.choice(uas)}
        try:
            html = get_html(url, ua, px)
            print(get_ip(html))
            t_end = int((t.time() - t_start))
            print('--- %s sec ---' % t_end)
            exit()
        except Exception as ex:
            print('Request failed:',
                  px,
                  ua,
                  type(ex).__name__,
                  sep='\n',
                  end='\n--------------\n')
        t.sleep(rnd.uniform(3, 7))


if __name__ == '__main__':
    main()
