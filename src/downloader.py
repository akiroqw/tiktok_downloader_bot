from config import *

class Downloader:

    def __init__(self):
        pass

    def download_video(self, url, output_name):

        session = requests.Session()
        server_url = 'https://musicaldown.com/'

        headers = {
            "Host": "musicaldown.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "TE": "trailers"
        }

        session.headers.update(headers)
        req = session.get(server_url)
        data = {}
        parse = bs4.BeautifulSoup(req.text, 'html.parser')
        get_all_input = parse.findAll('input')

        for i in get_all_input:
            if i.get("id") == "link_url":
                data[i.get("name")] = url
            else:
                data[i.get("name")] = i.get("value")

        post_url = server_url + "id/download"
        req_post = session.post(post_url, data=data, allow_redirects=True)

        get_all_blank = bs4.BeautifulSoup(req_post.text, 'html.parser').findAll(
            'a', attrs={'target': '_blank'})

        download_link = get_all_blank[0].get('href')
        get_content = requests.get(download_link)

        with open(output_name, 'wb') as fd:
            fd.write(get_content.content)