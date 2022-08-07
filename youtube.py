import logging
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from pytube import YouTube

# Metadata
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
logging.basicConfig(level=logging.INFO)

PATH = os.getenv('CHROMEDRIVER_PATH', 'INSERT PATH HERE')

IMPLICITLY_WAIT = os.getenv('IMPLICITLY_WAIT', 5)
INPUT_FILE = os.getenv('INPUT_FILE', 'input.txt')
MAX_SECONDS = os.getenv('MAX_SECONDS', 59)
MAX_MINUTES = os.getenv('IMPLICITLY_WAIT', 0)
DOWNLOAD_LOCATION = os.getenv('DOWNLOAD_LOCATION', f'{datetime.now().strftime("%d-%m")}')

logging.info('Get onto youtube. Accept cookies.')

driver = webdriver.Chrome(PATH)
driver.get("http://www.youtube.com")
driver.implicitly_wait(IMPLICITLY_WAIT)

accept_button = driver.find_element(
    by=By.CSS_SELECTOR,
    value='#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.eom-buttons.style-scope.ytd-consent-bump-v2-lightbox > div:nth-child(1) > ytd-button-renderer:nth-child(2)'
)
accept_button.click()

time.sleep(5)

logging.info('Start with alg training.')

with open(os.path.join(__location__, INPUT_FILE), encoding='utf-8') as file:
    for index, youtube_link in enumerate(file):
        logging.info(f'Start with link {index}.')
        driver.get(youtube_link.rstrip())
        while True:
            logging.info('looking for advert')

            advert = []
            advert = driver.find_elements(
                by=By.CLASS_NAME,
                value='ytp-ad-skip-button-container'
            )

            if not len(advert):
                print('break')
                logging.info('No advert found.')
                break

            try:
                button = driver.find_element(
                    By.CLASS_NAME,
                    'ytp-ad-skip-button-container'
                )
                logging.info('Skipping the advert.')
                button.click()
                break
            except (NoSuchElementException, ElementNotInteractableException):
                pass
        time.sleep(1)

logging.info('Done with alg training.')

logging.info('Start with video download.')

driver.get("http://www.youtube.com")
time.sleep(5)
logging.info('Find every thumbnail on the page.')
videos = driver.find_elements(
    by=By.CSS_SELECTOR,
    value='#thumbnail'
)

for index, video in enumerate(videos):
    logging.info('Loop through all thumbnails.')
    link = video.get_attribute('href')
    if link is None:
        logging.debug(f'Thumbnail has no link ({link}). Skipping thumbnail.')
        continue

    span = video.find_elements(by=By.XPATH, value='.//div[@id="overlays"]//ytd-thumbnail-overlay-time-status-renderer//span')

    if len(span) > 0:
        video_length = span[0].get_attribute('innerHTML')
        if len(video_length) < 9:

            time = video_length.split(':')
            if int(time[1]) <= MAX_SECONDS and int(time[0]) <= MAX_MINUTES:
                yt = YouTube(link)
                ys = yt.streams.get_highest_resolution()
                logging.debug(f'Downloading video ({link})...')
                ys.download(DOWNLOAD_LOCATION)
                logging.debug("Download completed!")
