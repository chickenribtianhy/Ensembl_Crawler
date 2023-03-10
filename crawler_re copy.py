import requests
import re
import xlrd
import xlwt

""" 
examples:
http://asia.ensembl.org/Homo_sapiens/Gene/Idhistory?g=ENSG00000236557 
http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000254739;r=11:528907-529659;t=ENST00000526431 
http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000255158;r=11:665910-678391;t=ENST00000527799 
http://asia.ensembl.org/Homo_sapiens/Component/Gene/Summary/gene_summary?db=core;g=ENSG00000267529
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"}
pattern = re.compile(
    '<div class="row"><div class="lhs">Gene type</div><div class="rhs"><p>(.*?)</p></div></div>')
pattern2 = re.compile('</span>(.*?)</span>')

def find_gene(gene="ENSG00000254397"):
    # print("http://asia.ensembl.org/Homo_sapiens/Component/Gene/Summary/gene_summary?db=core;g="+gene)
    req = requests.get(
        url="http://asia.ensembl.org/Homo_sapiens/Component/Gene/Summary/gene_summary?db=core;g="+gene, headers=headers)
    # with open("a.out", "w") as file:
    #     file.write(req.text)
    _match = re.findall(pattern, req.text)
    if len(_match) == 0:
        _match = ["none"]
    print(_match)
    return _match

# testing...
# find_gene(gene="ENSG00000267088")
# find_gene(gene="ENSG00000267529")
# find_gene(gene="ENSG00000236557")

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('gene type')

table = xlrd.open_workbook(filename="./pp2.xlsx")
# table = xlrd.open_workbook(filename="./rna_list.xlsx")
sheet = table.sheets()[0]
r_list1 = sheet.col_values(0)[1:]
# print(r_list1)
for i, _ in enumerate(r_list1):
    print(_)
    _match = find_gene(_)
    worksheet.write(i, 0, _)
    worksheet.write(i, 1, _match)
    if i % 200 == 0:
        print("%d done, saving..."%i)
        workbook.save("./gene_type_list_2.xlsx")


# r_list2 = sheet.col_values(2)[1:]
# for i, _ in enumerate(r_list2):
#     print(_)
#     _match = find_gene(_)
#     worksheet.write(i, 2, _)
#     worksheet.write(i, 3, _match)
#     if i % 200 == 0:
#         print("%d done, saving..."%i)
#         workbook.save("./gene_type_list_2.xlsx")


workbook.save("./gene_type_list_2.xlsx")
