import requests
from bs4 import BeautifulSoup

req = requests.get(
    "http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000254739;r=11:528907-529659;t=ENST00000526431")
# print(req.content)
""" http://asia.ensembl.org/Homo_sapiens/Gene/Idhistory?g=ENSG00000236557 """
""" http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000254739;r=11:528907-529659;t=ENST00000526431 """
""" http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000255158;r=11:665910-678391;t=ENST00000527799 """

# soup = BeautifulSoup(req.content, "lxml")
# # print(soup.prettify())
# """ <h1 class="summary-heading">Gene: ENSG00÷00254739</h1> """
# # print(soup.find("div", id="main"))
# # _main = soup.find("div", id="main")
# _main = soup.find(name="div", id="main")
# # print(_main)
# _h1 = _main.find_all('h1')[0]
# # print(_h1.text[6:])  # ENSG00000254739
# ensg = _h1.text[6:]

# # ensmbl_panel_1 = _main.find(name="div", id="ensmbl_panel_1")
# # ensmbl_panel_1 = _main.find(name="div", attrs={"class"})
# # print(ensmbl_panel_1)

# # gene_type = _main.find_all(text="Gene")
# # print(gene_type)
# _panel = _main.find_all()
# # _p = _main[1].find_all('div')
# # for _ in _p:
# #     # print(_.attrs['class'][0])
# #     if _.attrs['class'][0] == 'row':
# #         # print(_.prettify())
# #         pass
# # print(_main[1].prettify())
