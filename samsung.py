from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("Samsung phones")
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
driver.find_element(By.XPATH,"//span[text()='Samsung']").click()
phonenames=driver.find_elements(By.XPATH,"//span[contains(@class,'a-color-base a-text-normal')]")
prices=driver.find_elements(By.XPATH,"//span[contains(@class,'price-whole')]")

myphone=[]
myprice=[]

for phone in phonenames:
    myphone.append(phone.text)

print("*"*50)

for price in prices:
    myprice.append(price.text)

finallist=zip(myphone,myprice)


print("Part1")

wb=Workbook()
wb['Sheet'].title='Samsung Data'
sh1=wb.active
sh1.append(['Name','Price'])
for x in list(finallist):
    sh1.append(x)
wb.save("FinalRecords.xlsx")
print("Part2")
