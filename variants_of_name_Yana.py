from bs4 import BeautifulSoup
import requests
import re

res = requests.get("https://imya.com/female/%d0%af")
soup = BeautifulSoup(res.text, "html.parser")

n = soup.find_all("div", "one_name")  #divs with names' links

soup_hot = BeautifulSoup(str(n), "html.parser")
links = ["https://imya.com/" + link.get('href') for link in soup_hot.find_all("a")]  # links to names
# print(len(links))
names = []

for link in links:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    name_content = soup.find_all("div", "name_content")
    name_found = re.findall('Яна[^а-я]', str(name_content))
    if name_found:
        name = soup.h1.get_text().split()[1]
        names.append((name, link))

print("Found: ", len(names), "names")

with open("yana_names_soup.txt", "w") as f:
    for line in names:
        f.write(" ".join(line) + "\n")


