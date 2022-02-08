from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


                


def main():
    items_amount = input("How many items do you want to list? ")
    number_of_images= input("enter the number you would start from: ") 
    royalties_amount = input("Enter the royalties amount: ")
    item_price = input("Enter your item price in ETH: ")
    
    while int(number_of_images) < items_amount: 
        keyboard = Controller()
        opt=Options()
        opt.add_experimental_option("debuggerAddress","localhost:8989")
        driver = webdriver.Chrome(executable_path="C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe",chrome_options=opt)
        
        #uploading the file to Rarible 
        file_input = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/input')
        file_input.send_keys("F:\\2022 projects\\ALIEN\\1000 renders\\00",number_of_images,".jpeg") #getting the file path 
        
        driver.implicitly_wait(10) #10 seconds delay 
        price = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[4]/div/div[2]/div[1]/input') #setting up the price 
        price.send_keys(str(item_price))#entering the item price


        driver.implicitly_wait(10) #setting a 10 seconds delay 

        name = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[8]/div/div[2]/div/input')
        name.send_keys("#0" + str(number_of_images))         #the name of the item 

        royalties = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[10]/div/div[2]/div[1]/input') #xpath of royalties section 
        royalties.clear()
        royalties.send_keys("2.5")

        
        
        create_element = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[12]/div/div/button')
        create_element.click()  #clicking on creating element button in the ui of Rarible

        #wait for initializing 
        wait = WebDriverWait(driver,100) 
        #waiting for minting proccess to start
        mint = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div')))
        #adding a 5 sec delay  
        time.sleep(5)

        #Signing the transaction on metamask
        keyboard.press(Key.tab)    #clicking on tab
        keyboard.release(Key.tab)
        time.sleep(0.1)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        #Signing the transaction to sell the item 
        finish= wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div/div/div/div/div[2]/div/div[4]/div[1]/div[1]/div')))
        #5 seconds delay 
        time.sleep(5)

        #Signing the transaction on metamask
        keyboard.press(Key.tab)    #clicking on tab
        keyboard.release(Key.tab)
        time.sleep(0.1)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
        time.sleep(5)


        #creating another item
        creat_another=driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div/div/div/div/div[3]/div/div[3]/button[2]')
        creat_another.click()
        #increasing the number of the item by 1 after each cycle
        number_of_images=number_of_images+1 
        
if __name__ == "__main__":
    main()
