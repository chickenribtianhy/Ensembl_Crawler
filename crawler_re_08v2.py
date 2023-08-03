import requests
import re
import xlwt
import pandas as pd
import csv

""" 
examples:
http://asia.ensembl.org/Homo_sapiens/Gene/Idhistory?g=ENSG00000236557 
http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000254739;r=11:528907-529659;t=ENST00000526431 
http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000255158;r=11:665910-678391;t=ENST00000527799 
http://asia.ensembl.org/Homo_sapiens/Component/Gene/Summary/gene_summary?db=core;g=ENSG00000267529
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"
}
pattern_type = re.compile(
    '<div class="row"><div class="lhs">Gene type</div><div class="rhs"><p>(.*?)</p></div></div>')
# pattern2 = re.compile('</span>(.*?)</span>')
pattern_name = re.compile(
    '<div class="lhs">Name</div><div class="rhs"><p><a.*?>(.*?)</a>.*?</p></div>'
)
pattern_UniProtKB = re.compile(
    '<div class="lhs">UniProtKB</div><div class="rhs"><p>.*?<a .*?>(.*?)</a></p></div>'
)
pattern_description = re.compile(
    '<div class="lhs">Description</div><div class="rhs"><p>(.*?)</p></div>'
)


def find_gene(gene="ENSG00000254397"):
    # print("http://asia.ensembl.org/Homo_sapiens/Component/Gene/Summary/gene_summary?db=core;g="+gene)
    req = requests.get(
        url=f"http://asia.ensembl.org/Homo_sapiens/Component/Gene/Summary/gene_summary?db=core;g={gene}", headers=headers
    )
    req_des = requests.get(
        url=f"http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g={gene}", headers=headers
    )
    # with open("a.out", "w") as file:
    #     file.write(req.text)
    description = re.findall(pattern_description, req_des.text)
    name = re.findall(pattern_name, req.text)
    UniProtKB = re.findall(pattern_UniProtKB, req.text)
    geneType = re.findall(pattern_type, req.text)
    description = "".join(description) if len(description) > 0 else ""
    name = "".join(name) if len(name) > 0 else ""
    UniProtKB = "".join(UniProtKB) if len(UniProtKB) > 0 else ""
    geneType = "".join(geneType) if len(geneType) > 0 else ""
    print(description, name, UniProtKB, geneType)
    return description, name, UniProtKB, geneType


# ENSG00000210049
# testing...
# find_gene(gene="ENSG00000198899")
# find_gene(gene="ENSG00000267529")
# find_gene(gene="ENSG00000236557")


def file2title(file: str, sheet=0):
    title = pd.read_excel(file, sheet_name=sheet).iloc[:, :1].to_numpy()
    return title


workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('gene')

# table = xlrd.open_workbook(filename="./rna_list_2.xls")
# sheet = table.sheets()[0]
r_list1 = file2title("./rna_list_2.xls")
print(r_list1)
print(len(r_list1))
open("./rna_description2.csv", 'w')
M = 17000
for i, _ in enumerate(r_list1[M:]):
    print(_)
    description, name, UniProtKB, geneType = find_gene(_[0])
    # worksheet.write(i, 0, i)
    # worksheet.write(i, 1, _[0])
    # worksheet.write(i, 2, description)
    # worksheet.write(i, 3, name)
    # worksheet.write(i, 4, UniProtKB)
    # worksheet.write(i, 5, geneType)

    with open("./rna_description2.csv", 'a', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([i+M, _[0], description, name, UniProtKB, geneType])

    # if i % 200 == 0:
    #     print("%d done, saving..." % i)
    #     workbook.save("./rna_description.xlsx")


# workbook.save("./rna_description.xlsx")
