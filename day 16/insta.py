# import getpass
# my_password=getpass.getpass("what is your password?\n")

# print(my_password)
from urllib.prase import urlprase
import os
import time
import requests
from conf import INSTA_USERNAME,INSTA_PASSWORD
from selenium import webdrivers
browser=webdriver.Chrome()

url="http://www.instagram.com"
browser.get(url)

time.sleep(2)
username_el=browser.find_element_by_name("username")
username_el.send_keys(INSTA_USERNAME)

password_el=browser.find_element_by_name("password")
password_el.send_keys(INSTA_PASSWORD)

time.sleep(1.5)
submit_btn_el=browser.find_element_by_css_selector("button[type='submit']")

submit_btn_el.click()
body_el=browser.find_element_by_css_selector("body")
html_text=body_el.get_attribute("innerHTML")

# print(html_text)

"""
<button class="_5f5mN jIbKX  _6VtSN yZn4P">Follow</button>
"""
# browser.find_elements_by_css_selector("button")
# xpath
# my_button_xpath="//button"
# browser.find_element_by_xpath(my_button_xpath)
def clik_to_follow(browser):
    # my_follow_btn_xpath="//a[contains(text(),'Follow')][not(contains(text(),'Following'))]
    # follow_btn_elements=browser.find_element_by_xpath(my_follow_btn_xpath)

    # my_follow_btn_xpath="//button[contains(text(),'Follow')][not(contains(text(),'Following'))]
    # follow_btn_elements=browser.find_element_by_xpath(my_follow_btn_xpath)


    my_follow_btn_xpath="//*[contains(text(),'Follow')][not(contains(text(),'Following'))]"
    follow_btn_elements=browser.find_element_by_xpath(my_follow_btn_xpath)

    for btn in follow_btn_elements:
        time.sleep(2) # self-throttle
        try:
            btn.click()
        except:
            pass    

# new_user_url="http://www.instagram.com/ted/"    
# browser.get(new_user_url)
# clik_to_follow(browser)
# browser.get(new_user_url)
time.sleep(2)
the_rock_url="http://www.instagram.com/therock/"
browser.get(new_rock_url)


post_url_pattern="http://www.instagram.com/p/<post-slug-id>"
post_xpath_str="//a[contains(@href,'/p/')]"
post_links=browser.find_elements_by_xpath(post_xpath_str)
post_link_el=None
for len(post_links)>0:
    post_link_el=post_links[0]
if post_link !=None:
    post_href=post_link_el.get_attribute("href")
    browser.get(post_link)    

video_els=browser.find_element_by_xpath("//video") 
images_els=browser.find_element_by_xpath("//img")    

base_dir=os.path.dirname(os.path.abspath(__file__))
data_dir=os.path.join(base_dir,"data")
os.makedirs(data_dir,exist_ok=True)

#PIL to verify the size of any gi
def scrape_and_save(elements):
    for el in elements:
        # print(img.get_attribute('src'))
        url=el.get_attribute('src')
        base_url=urlprase(url).path
        filename=os.path.basename(base_url)
     
        filepath=os.path.join(img_dir,filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url,stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath,'wb')as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)    
"""
LONG TERM Goal:
use machine learning to classify the post's
image or video
and then comment in a relevent fashion
"""