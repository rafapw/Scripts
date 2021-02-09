import os,os.path,sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
import psutil

def navigate():
    options = Options()
    options.headless = False
    profile = FirefoxProfile()
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
    driver = webdriver.Firefox(firefox_profile=profile,options=options)

    print('Carregando')
    driver.get('https://2048game.com/pt/')

    input('ENTER para continuar...')

    calcs(driver,Keys)


def calcs(driver,Keys):
    n=0
    tile_ant=[]
    directions=[Keys.RIGHT,Keys.DOWN,Keys.LEFT,Keys.UP]
    
    while True:

        tile_map=[]
        tile_con=driver.find_element_by_class_name('tile-container')    
        tc=tile_con.find_elements_by_tag_name('div')
        try:
            for t in tc:
                tile_map.append(t.get_attribute('class'))
        except:
            pass

        #print(tile_map)
        #print(tile_ant)
        
        if tile_map!=tile_ant:
            driver.find_element_by_css_selector('body').send_keys(directions[0])
            tile_ant=tile_map
            n=1

        elif n==0:
            #if tile_ant==tile_map:
            while tile_ant==tile_map:
                n+=1
                driver.find_element_by_css_selector('body').send_keys(directions[n])

                tile_map=[]
                tile_con=driver.find_element_by_class_name('tile-container')    
                tc=tile_con.find_elements_by_tag_name('div')
                try:
                    for t in tc:
                        tile_map.append(t.get_attribute('class'))
                except:
                    pass

        n=0

def depois():
    input()
    for c in range(1,5):
        for r in range(1,5):
            try:

                print(driver.find_element_by_css_selector('div.grid-row:nth-child('+str(c)+') > div:nth-child('+str(r)+')').get_attribute('innerHTML'))
                
                #driver.find_element_by_class_name('tile tile-'+str(n)+' tile-position-'+str(c)+'-'+str(r))
                #print(str(c)+'-'+str(r)+': '+str(n))
            #except Exception as e:
                #print(e)
                #pass

            #try:
                #driver.find_element_by_class_name('tile tile-'+str(n)+' tile-position-'+str(c)+'-'+str(r)+' tile-new')
                #print(str(c)+'-'+str(r)+': '+str(n))
            #except Exception as e:
                #print(e)
                #pass

            #try:
                #driver.find_element_by_class_name('tile tile-'+str(n)+' tile-position-'+str(c)+'-'+str(r)+' tile-merged')
                #print(str(c)+'-'+str(r)+': '+str(n))
            #except Exception as e:
                #print(e)
                #pass
            except:
                pass

        #n*=2
navigate()
