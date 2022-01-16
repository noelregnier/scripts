import requests
import re

res = requests.get("https://imya.com/female/%d0%af")

content = res.text
# print(content)

# links = re.findall('.*<a .*href="(.+?)">Я.+?', content)
links = re.findall('<div class="one_name">.*<a .*href="(.+?)">Я.+?</div>', content)
print(links)
links = ["https://imya.com/" + link for link in links]
print(len(links))
derivatives = []
names = []
for k, link in enumerate(links):
    print(k, link)
    if "name" not in link:
        continue
    res_link = requests.get(link)
    # print("trying ", link)
    content_link = res_link.text
    pages_body_text = re.findall('<div class="pages_body_text">(.*Яна.*)</div>', content_link)
    if pages_body_text:
        name = re.findall("<h1>(.+?)</h1>", content_link)
        names.append((name[0], link))
        print(name, link)
for i in names:
    print(i)
    # print(pages_body_text)
#     if "Яна" in content_link:
#         derivatives.append(link)
#         print("it suits")
#         name = re.findall("<h1>(.+?)</h1>", content_link)
#         print(name)
#
# print("derivatives are:")
# print(derivatives)
