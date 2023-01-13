import selenium
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

star_data = []
final_star_data = []
header = ["Star_name","Distance","Mass","Radius"]
def scrape2():
    url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    star_table = soup.find_all("table")
    table_rows = star_table[7].find("tbody")
    for table_row in table_rows.find_all("tr"):
        td_tags = table_row.find_all("td")
        temp_list = []
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.text.strip())
            except:
                temp_list.append("")
    
        star_data.append(temp_list)
        #print(star_data)

scrape2()

for i in range(1,len(star_data)):
    names = star_data[i][0]
    distance = star_data[i][5]
    mass = star_data[i][7]
    radius = star_data[i][8]
    collect = [names,distance,mass,radius]
    final_star_data.append(collect)

print(final_star_data)
#df = pd.DataFrame(final_star_data)

with open("result2.csv","w",encoding="utf8",newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(final_star_data)



