import feedparser

class DirectPrint:

    def string_decoder(self, string, encoding, decoding):
        string = str(string)
        encoded_bytes = string.encode(encoding, 'replace')
        decoded_string = encoded_bytes.decode(decoding, 'replace')
        return decoded_string
    
    def get_logo(self, feedtype:str):
        if feedtype == 'news':
            x = '╔╗╔╔═╗╦ ╦╔═╗\n║║║║╣ ║║║╚═╗\n╝╚╝╚═╝╚╩╝╚═╝'
        if feedtype == 'weather':
            x = '╦ ╦╔═╗╔═╗╔╦╗╦ ╦╔═╗╦═╗\n║║║║╣ ╠═╣ ║ ╠═╣║╣ ╠╦╝\n╚╩╝╚═╝╩ ╩ ╩ ╩ ╩╚═╝╩╚═'
        return x

    def phisical_print(self, news_list:list, printer_path, printer_encoding, feedtype):
        with open(printer_path, 'w', encoding=printer_encoding) as printer:
            printer.write(self.get_logo(feedtype=feedtype))
            for news in news_list:
                printer.write("\n=========\n")
                for string in news.values():
                    decoded_string = self.string_decoder(string, printer_encoding, printer_encoding)
                    printer.write(f"{decoded_string}\n")

class ReadAndPrintRss(DirectPrint):

    def __init__(
        self,
        rss_feed,
        allow_tags,
        limit=100,
        printer_path='/dev/usb/lp0',
        printer_encoding='cp866',
        feedtype='news'
        ):
        NewsFeed = feedparser.parse(rss_feed)
        news_list = self.prepare_news(NewsFeed, allow_tags, limit)
        self.phisical_print(news_list, printer_path, printer_encoding, feedtype)

    def prepare_news(self, NewsFeed:object, allow_tags:list, limit):
        news_list = []
        for entry in NewsFeed.entries:
            news = {}
            for tag in entry.keys():
                if tag in allow_tags:
                    news[tag] = entry.get(tag)
            if 'image' in allow_tags:
                for link in entry.get('links'):
                    if 'image' in link.get('type'):
                        news['image'] = link.get('href')
            news_list.append(news)
            if len(news_list) >= limit:
                break
        return news_list


if __name__ == '__main__':

    allow_tags = ['id', 'title', 'author', 'published', 'summary']
    rss_feed=""
    d = ReadAndPrintRss(rss_feed=rss_feed, allow_tags=allow_tags, feedtype='news', limit=3)

    allow_tags = ['title', 'summary']
    rss_feed=""
    d = ReadAndPrintRss(rss_feed=rss_feed, allow_tags=allow_tags, feedtype='weather')

