# This script requires Selenium 4.8.3!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class WebScrap:
    def __init__(self, url: str):
        self.url = url
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.url)

    def checkTag(self, tag: str):
        tags = self.driver.find_elements(By.TAG_NAME, tag)

        if (not tags or len(tags) < 1):
            print(f"No <{tag}> tags found!")
            return

        print(f"Found <{len(tags)}> {tags[0].tag_name} tags.")
        if input("Show them? (y/n): ") not in set(['y', 'Y']):
            return

        for tag in tags:
            print(
                f"\t<{tag.tag_name}>{tag.text}<{tag.tag_name}>")
        print("(end of list)\n\n")

    def quit(self):
        print("Exiting . . .")
        self.driver.quit()


#ws = WebScrap("https://cristiancazares.github.io/")
ws = WebScrap("https://es.wikipedia.org/wiki/Wikipedia:Portada")
ws.checkTag("h2")
ws.checkTag("span")
ws.quit()
