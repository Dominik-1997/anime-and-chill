import time

from selenium import webdriver
from selenium.webdriver.common.by import By


PATH = "C:\\Users\\domin\\Desktop\\Path\\chromedriver.exe"  # paths will vary
driver = webdriver.Chrome(executable_path=PATH)

driver.implicitly_wait(30)

# we load page, and wait 15s, in this time I had to login

driver.get("https://www.anime-planet.com/anime/all?bvm=list?page=1")
time.sleep(15)

# for every page (1-610) had to press dropdown menu and choose: watched 35 times

for j in range(1, 610):

    time.sleep(5)
    my_elements = []
    my_options = []

    newURL = f"https://www.anime-planet.com/anime/all?page={j}?bvm=list"
    driver.get(newURL)

    my_elements = driver.find_elements(By.CLASS_NAME, "changeStatus")
    my_options = driver.find_elements(By.XPATH, "//select[@class='changeStatus']/option[@value=1]")

    for i in range(0, 36):
        try:

            selected = my_elements[i]
            # time.sleep(1)
            selected.click()
            selected = my_options[i]
            selected.click()

        except:
            pass


time.sleep(20)
print("Done!")

