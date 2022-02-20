import requests
from bs4 import BeautifulSoup
import re

female_names = {}
male_names = {}

def get_female_names_links(link):
    # link = "https://imya.com/"
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    female_letters_block = soup.find_all("div", "female_letters")
    soup_hot = BeautifulSoup(str(female_letters_block), "html.parser")
    female_letters_links = ["https://imya.com/" + link.get('href') for link in soup_hot.find_all("a")]  # links to names
    return female_letters_links


def get_links_for_certain_letter(link):
    '''
    This method takes a link to a page where names starting with a certain letter are listed, e.g., letter "a" names,
    and returns a list of links to all the names on this page in the "one_name" block, e.g.,
    all names starting with "a" links list
    :param link:
    :return: list of names links
    '''

    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    n = soup.find_all("div", "one_name")  #divs with names' links
    soup_hot = BeautifulSoup(str(n), "html.parser")
    links = ["https://imya.com/" + link.get('href') for link in soup_hot.find_all("a")]  # links to names
    return links


def get_name_origins(link):
    '''
    This method takes a link to an individual name and retruns a tuple with list of names' origins and the current name
    :param link:
    :return:
    '''
    # print(link)
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    current_name = soup.h1.get_text().split()[1]
    name_content = soup.find_all("div", "name_content")
    print(name_content)
    root_name_extracted = re.findall(
        '[фФ]орм[а]* (.*?им[её]+н[и]*[:]* .+?</a>)[/,]*(.*)<*/*a*>*|[Пп]роизводное (.*?им[её]+н[и]*[:]* .+?</a>)[/,]*(.*)<*/*a*>*|[Оо]бразовано от (.*?им[её]+н[и]*[:]* .+?</a>)[/,]*(.*)<*/*a*>*',
        str(name_content))
    print(root_name_extracted)
    name_origins = []
    for extract in root_name_extracted:
        for extract_item in extract:
            if "мужского" in extract_item or len(extract_item) == 0:
                continue
            parent_names = re.findall(">(.+?)</a>", extract_item)
            name_origins.extend(parent_names)
    return name_origins, current_name

def write_name_and_origins(param: tuple):
    name_origins, current_name = param
    for name in name_origins:
        if name not in female_names:
            female_names[name] = list()
        female_names[name].append(current_name)





