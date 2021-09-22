import requests
from bs4 import BeautifulSoup


def scrapeUrl(url):
    # assuming url is well formed for now.
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    title_out = ""
    ingredients_out = []

    titleFromWebPage = soup.find_all(
        "h1", class_="post-header__title post-header__title--masthead-layout heading-1")

    title_out = removeHtml(titleFromWebPage)

    ingredientsFromWebPage = soup.find_all(
        "li", class_="pb-xxs pt-xxs list-item list-item--separator")
    ingredients_out = removeHtml(ingredientsFromWebPage)

    imageFromWebPage = soup.find_all("img", class_="image__img")
    image_out = scrapeForImage(imageFromWebPage, title_out)
    # print(image_out)

    return [title_out, ingredients_out, image_out]


def scrapeForImage(html, title):
    for i in html:
        if title in str(i):
            image_html = str(i)

    imageIndexSt = image_html.find('src="')
    imageIndexEn = image_html.index('?')

    return image_html[imageIndexSt+5:imageIndexEn]


def removeHtml(html):
    string_out = []
    for i in html:
        # print(i, "\n")
        i = str(i)
        sInd = int(i.index('>'))
        eInd = int(i.rindex('<'))
        # print(ind)
        i = (i[sInd+1:eInd])
        i = i.replace("<!-- -->", "")
        i = i.replace("½", "0.5")
        print(i)
        i = i.strip()
        i = i.split(",", 1)[0]
        print(i)
        if len(html) == 1:
            return i
        string_out.append(i)
    return string_out


# print(scrapeUrl("https://www.bbcgoodfood.com/recipes/oaty-katsu-chicken-dippers"))
