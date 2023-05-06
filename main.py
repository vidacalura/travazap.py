import pyautogui
import sys
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from tkinter import messagebox

driver = None
try:
    driver = webdriver.Chrome()
except:
    driver = webdriver.Firefox()

pyautogui.FAILSAFE = False

sleep_time = 1.5

def travazap(nome):
    while 1:
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div/p").click()
            pyautogui.write(nome)
            break

        except:
            sleep(2)

    sleep(sleep_time)
    for i in range(0, 20):
        try:
            span = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[1]/span/span")

            if span.text.lower() == nome.lower():
                span.click()

        except:
            pass

    sleep(sleep_time)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span").click()
    sleep(sleep_time)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[4]/div/span").click()
    sleep(sleep_time)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[2]/div/div[3]/div/div/div[1]/div/div[3]/span/span").click()
    sleep(4)

    for _ in range(0,1000):
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div/div/div[1]/div/span/img").click()
        sleep(0.8)

    sleep(120)

# main
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

messagebox.showinfo(title="Travazap.py", message="Insira su zap zap")

travazap(" ".join(sys.argv[1:]))
