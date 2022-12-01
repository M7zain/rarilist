from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
import time 

frame = tk.Tk()
frame.title("RariList")
frame.geometry('400x250')


def listing():
    x = 0
    items_amount = int(items_amount_input.get(1.0,"end-1c"))
    number_of_images= int(number_of_images_input.get(1.0,"end-1c")) 
    royalties_amount = royalties_amount_input.get(1.0,"end-1c")
    item_price = item_price_input.get(1.0,"end-1c")
    
    while x < items_amount: 
        keyboard = Controller()
        opt=Options()
        opt.add_experimental_option("debuggerAddress","localhost:8989")
        driver = webdriver.Chrome(executable_path="C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe",chrome_options=opt) #chromedriver dir
        
        #uploading the file to Rarible 
        file_input = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/input')
        file_input.send_keys("F:\\2022 projects\\ALIEN\\1000 renders\\00",number_of_images,".jpeg") #Set the file path and format to your images
        
        
        price = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[4]/div/div[2]/div[1]/input') #setting up the price 
        price.clear()
        price.send_keys(str(item_price))#entering the item price


        

        name = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[8]/div/div[2]/div/input')
        name.clear()
        name.send_keys("#0" + str(number_of_images))         #the name of the item 

        royalties = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[10]/div/div[2]/div[1]/input') #xpath of royalties section 
        royalties.clear()
        royalties.send_keys("2.5")

        
        
        create_element = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[12]/div/div/button')
        create_element.click()  #clicking on creating element button in the ui of Rarible

         
        #if an error occurs it clicks on the try again button 
        if (EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/button')) == True):
            try_again_button =driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/button')
            try_again_button.click()
            
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
        #printing the last item number
        print("#0" + str(number_of_images) +" was listed")
        #increasing the number of the item by 1 after each cycle
        number_of_images = number_of_images+1 
        x = x+1

'''

        UI starts here 

'''
#starting image number input box 
number_of_images_input= tk.Text(frame,height=1,width=5)
number_of_images_input.place(x=150,y=20)

number_of_images_label= tk.Label(frame,text="Number of images:")
number_of_images_label.place(x=40,y=20)

#items amount input box 
items_amount_input = tk.Text(frame,height=1,width=5)
items_amount_input.place(x=150,y=60)
items_amount_label= tk.Label(frame,text="Items amount:")
items_amount_label.place(x=40,y=60)

#royalties amount input box 
royalties_amount_input= tk.Text(frame,height=1,width=5)
royalties_amount_input.place(x=150,y=100)
royalties_amount_label= tk.Label(frame,text="Royalties amount:")
royalties_amount_label.place(x=40,y=100)

#item price input box  
item_price_input = tk.Text(frame,height=1,width=5)
item_price_input.place(x=150,y=140)
item_price_label= tk.Label(frame,text="Item price:")
item_price_label.place(x=40,y=140)

#currency label 
curr = tk.Label(frame,text="ETH")
curr.place(x=200,y=140)

#photos directory input box 
photos_dir= tk.Text(frame,height=1,width=30)
photos_dir.place(x=150,y=180)
photos_dir_label= tk.Label(frame,text="photos directory:")
photos_dir_label.place(x=40,y=180)
#start button 
start= tk.Button(frame,text="Start listing",command = listing)
start.place(x=300,y=50)

#Exit button 
exit = tk.Button(frame,text="Exit",command=frame.destroy)
exit.place(x=350,y=210)


frame.mainloop()