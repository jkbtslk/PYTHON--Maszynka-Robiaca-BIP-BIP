import requests, ezsheets, bs4

ss = ezsheets.Spreadsheet("1htV1nVCpSvkQLaVGS0Cda1rvnEzVViPC7OzbBjXIIhw")
rbk_res_o = requests.get("https://bip.um.rybnik.eu/Default.aspx?Page=31")
rbk_res_o.raise_for_status()
print("Połączono z BIP Rybnik.")
rbk_soup_o = bs4.BeautifulSoup(rbk_res_o.text, "html.parser")
rbk_data_o = rbk_soup_o.find_all("td", class_="text-nowrap text-center")
table_body_o = rbk_soup_o.find_all("tbody")

rbk_link_o = rbk_soup_o.find_all("a", class_="btn btn-primary")
rbk_link_pre_o = "https://bip.um.rybnik.eu/"
rbk_links_o = []
for link in rbk_link_o:
	rbk_link_post = rbk_link_pre_o+link.get("href")
	rbk_links_o.append(rbk_link_post)

print("Aktualizuję ogłoszenia urzędowe...")
rbk_sheet_o = ss[0]
for i, j in zip(range(3, 28), range(0, 25)):
	rbk_sheet_o[1, i] = rbk_data_o[j].text
	rbk_sheet_o[3, i] = rbk_links_o[j]
print("Ogłoszenia urzędowe zaktualizowane")

# Zarządzenia prezydenta
rbk_res_p = requests.get("https://bip.um.rybnik.eu/Default.aspx?Page=214")
rbk_res_p.raise_for_status()
rbk_soup_p = bs4.BeautifulSoup(rbk_res_p.text, "html.parser")
rbk_data_p = rbk_soup_p.find_all("td", class_="text-nowrap text-center")
table_body_p = rbk_soup_p.find_all("tbody")

rbk_link_p = rbk_soup_p.find_all("a", class_="btn btn-primary")
rbk_link_pre_p = "https://bip.um.rybnik.eu/"
rbk_links_p = []

for link in rbk_link_p:
	rbk_link_post_p = rbk_link_pre_p+link.get("href")
	rbk_links_p.append(rbk_link_post_p)

print("Aktualizuję zarządzenia prezydenta...")
for i, j in zip(range(3, 28), range(0, 25)):
	rbk_sheet_o[5, i] = rbk_data_p[j].text
	rbk_sheet_o[7, i] = rbk_links_p[j]
print("Zarządzenia prezydenta zaktualizowane.")


# Uchwały RM
rbk_res_rm = requests.get("https://bip.um.rybnik.eu/Default.aspx?Page=247")
rbk_res_rm.raise_for_status()
rbk_soup_rm = bs4.BeautifulSoup(rbk_res_rm.text, "html.parser")
rbk_data_rm = rbk_soup_rm.find_all("td", class_="text-nowrap text-center")
table_body_rm = rbk_soup_rm.find_all("tbody")

rbk_link_rm = rbk_soup_rm.find_all("a", class_="btn btn-primary")
rbk_link_pre_rm = "https://bip.um.rybnik.eu/"
rbk_links_rm = []

for link in rbk_link_rm:
	rbk_link_post_rm = rbk_link_pre_rm+link.get("href")
	rbk_links_rm.append(rbk_link_post_rm)

print("Aktualizuję uchwały Rady Miasta...")
for i, j in zip(range(31, 59), range(0, 25)):
	rbk_sheet_o[1, i] = rbk_data_rm[j].text
	rbk_sheet_o[3, i] = rbk_links_rm[j]
print("Uchwały Rady Miasta zaktualizowane.")

# rcb_res_rm = requests.get("https://www.bipraciborz.pl/kadencja-2018-2023")
# rcb_res_rm.raise_for_status()
# rcbk_soup_rm = bs4.BeautifulSoup(rcb_res_rm.text, "html.parser")
# rcb_data_rm = rcbk_soup_rm.find_all("span", class_="prawoAkt")
#
# print(rcb_data_rm)
# rbk_link_o = rbk_soup_o.find_all("a", class_="btn btn-primary")
# rbk_link_pre_o = "https://bip.um.rybnik.eu/"
# rbk_links_o = []
# for link in rbk_link_o:
# 	rbk_link_post = rbk_link_pre_o+link.get("href")
# 	rbk_links_o.append(rbk_link_post)
#
# rbk_sheet_o = ss[0]
# for i, j in zip(range(3, 28), range(0, 25)):
# 	rbk_sheet_o[1, i] = rbk_data_o[j].text
# 	rbk_sheet_o[3, i] = rbk_links_o[j]
