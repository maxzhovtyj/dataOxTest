import aiohttp
import asyncio
from bs4 import BeautifulSoup as BS
from schema import *
import re
from datetime import datetime

db = PostgresqlDatabase(host=host, user=user, password=password, database=db_name, port=port)


async def main():
    try:
        db.connect()
        db.create_tables([Article])

        client_session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))

        async with client_session as session:
            data = await parse_articles(session)

        with db.atomic():
            for article in data:
                Article.create(**article)

        print("[INFO] data was inserted into database")
    except Exception as ex:
        print("[WARNING] something went wrong", ex)
    finally:

        print("[INFO] database connection closed")


async def parse_articles(session):
    articles = []
    page = 1
    while page <= MAX_PAGES:
        print(f"request iteration on page = {page}")
        url = f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273"
        async with session.get(url) as resp:
            data = await resp.text()
            html = BS(data, 'html.parser')

            content = html.select('main > .container-results.large-images > .search-item > .clearfix')

            if len(content):
                for e in content:
                    img_url = e.select(".left-col > .image > picture > img")

                    # check whether article has an image or not
                    if len(img_url):
                        img_url = e.select(".left-col > .image > picture > img")[0]['data-src']
                    else:
                        img_url = None

                    price_selector = e.select(".info > .info-container > .price")[0].text.strip()

                    # check whether price wasn't specify
                    if has_numbers(price_selector):
                        currency = price_selector[0]
                        price = price_selector[1:]
                    else:
                        price = price_selector
                        currency = None

                    # remove duplicate whitespaces in beds string
                    beds = e.select(".rental-info > .bedrooms")[0].text
                    beds = " ".join(beds.split())

                    created_at = e.select(".info > .info-container > .location > span")[1].text.strip()
                    created_at = created_at.replace("/", "-")

                    # if article was created recently
                    if not created_at.find("<"):
                        current = datetime.now()
                        created_at = str(current.day) + "-" + str(current.month) + "-" + str(current.year)

                    item = {
                        "img_url": img_url,
                        "title": e.select(".info > .info-container > .title > .title")[0].text.strip(),
                        "currency": currency,
                        "price": price,
                        "city": e.select(".info > .info-container > .location > span")[0].text.strip(),
                        "created_at": created_at,
                        "description": e.select(".info > .info-container > .description")[0].text.strip(),
                        "beds": beds
                    }
                    articles.append(item)

                page += 1
            else:
                break

    return articles


def has_numbers(var):
    return bool(re.search(r'\d', var))


if __name__ == "__main__":
    asyncio.run(main())
