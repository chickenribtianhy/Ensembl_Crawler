import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwt

headers = {
    "User-Agent": "My User Agent"
}


def find_gene(gene="ENSG00000254397"):
    url = f"http://asia.ensembl.org/Homo_sapiens/Component/Gene/Summary/gene_summary?db=core;g={gene}"
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    description = soup.find("div", class_="description").get_text(strip=True)
    name = soup.find("div", class_="rhs").find("a").get_text(strip=True)
    uniprot_link = soup.find("div", class_="uniprot").find("a")
    uniprot_kb = uniprot_link.get_text(strip=True) if uniprot_link else ""
    gene_type = soup.find("div", class_="gene_type").find(
        "p").get_text(strip=True)

    return description, name, uniprot_kb, gene_type


def file2title(file: str, sheet=0):
    title = pd.read_excel(file, sheet_name=sheet).iloc[:, :1].to_numpy()
    return title


workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('gene')

r_list1 = file2title("./rna_list_2.xls")
print(len(r_list1['A']))
for i, _ in enumerate(r_list1.iter_rows(values_only=True)):
    print(_[0])
    description, name, UniProtKB, geneType = find_gene(_[0])
    worksheet.cell(row=i+1, column=1, value=_[0])
    worksheet.cell(row=i+1, column=2, value=description)
    worksheet.cell(row=i+1, column=3, value=name)
    worksheet.cell(row=i+1, column=4, value=UniProtKB)
    worksheet.cell(row=i+1, column=5, value=geneType)
    if i % 200 == 0:
        print("%d done, saving..." % i)
        workbook.save("./rna_description.xlsx")

workbook.save("./rna_description.xlsx")
