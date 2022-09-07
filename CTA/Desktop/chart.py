# from seleniumbase import BaseCase

# class MyChartMakerClass(BaseCase):
#     def test_chart_maker(self):
#         self.create_presentation()
#         self.begin_presentation(filename="report.html")
#         self.create_pie_chart(title="Automated Tests")
#         self.add_data_point("passed", 8, color="#95d96f")
#         self.add_data_point("warning", 2, color="#eaeaea")
#         self.add_data_point("failed", 1, color="#f1888f")
#         self.add_slide("<p>Pie Chart</p>" + self.extract_chart())
        



from bs4 import BeautifulSoup
import re

file = open("report.html", "r")
contents = file.read()
 
soup = BeautifulSoup(contents, 'html.parser')
pattern = "class"
# print(soup)

text1 = soup.findAll("<span>")
print(text1)