# The below code will like all the blogs whichever are added
# Enter the number of times you want to open the browser for likes
for j in range(2): 
    from selenium import webdriver
    from selenium.webdriver.edge.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.edge.options import Options
    import time

#Change the service path according to the edge driver saved on your PC 
# Do not forget to change to replace the "\" to "/"
    service = Service("C:/Users/KD00821059/Documents/KD Auto/Edge driver/msedgedriver.exe")
    option = Options()
    option.add_argument("-private")
    driver = webdriver.Edge(service=service, options=option)

    driver.get("https://www.fibilabs.tech/blog")
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0,10000)")
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,10000)")
    time.sleep(5)

    likebtn = driver.find_elements(By.XPATH,"//div[@class='like-button LtaU1R']")

    for i in likebtn:
        # time.sleep(2)
        driver.implicitly_wait(20)
        driver.execute_script("window.scrollBy(0,10000)")
        time.sleep(3)
        # c = likebtn.count(i)
        i.click()
        # print(c)
    
    time.sleep(10)
    driver.close
    

