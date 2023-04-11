### By: `Cristian Cázares`
### April 10th 2023
<br>

# Python + Selenium String recognition
As a form of web scrapping, in this small project I am going to do a string recognition on a web page to look for the content of `h2` and `span` tags. The script can be used for any text-related HTML tags.

To achieve this, I am going to take advantage of the ease of use of Python and the robust set of tools of Selenium.
Therefore let's initialized the project by installing it.
## Initialization
```bash
pip install Selenium
```
__I am going to be using Python 3.8 and Selenium 4.8.3!__

This are the followings tools from Selenium that are going to be used:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
```

## Encapsulation
To have a cleaner and more reusable structure I am going to create an object called `WebScrap`:
```python
class WebScrap:
	def  __init__(self, url:  str):
		pass
	def  checkTag(self, tag:  str):
		pass
	def quit(self):
		pass
```
This object will create a new web session by using a web driver. The idea is to use initialize the object with a string detonating the URL of the web page to check and then use the `checkTag` method to look for a tag by passing a string with its name.
```python
ws = WebScrap("https://es.wikipedia.org/wiki/Wikipedia:Portada")
ws.checkTag("h2")
ws.checkTag("span")
ws.quit()
```

## Implementation
Now that we have a general structure, let's implement the methods of the class.
### __init__(self,  url: str)
The constructor of the class is only going to take an string with the web's URL to use.
```python
def  __init__(self, url:  str):
	self.url = url
```
We need to set a web driver. To do this let's first initialized some `Options()`
```python
	chrome_options = Options()
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
```
This options are only meant to avoid some long warning logs that for now are irrelevant.

We can now initialized the driver to use for the session. I am going to be using the Chrome one.
```python
	self.driver = webdriver.Chrome(options=chrome_options)
	self.driver.get(self.url)
```
All together:
```python
def  __init__(self, url:  str):
	self.url = url
	chrome_options = Options()
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	self.driver = webdriver.Chrome(options=chrome_options)
	self.driver.get(self.url)
```

### checkTag(self, tag: str)
```python
def checkTag(self, tag: str):
    tags = self.driver.find_elements(By.TAG_NAME, tag)
```
Is pretty straight forward to retrieve all the tags by its name.This returns a list of Selenium objects with multiple valuable attributes.

Now let's check if this list was indeed created and its length is over zero.

If either of this conditions are meet, let's abort. 
```python
    if (not tags or len(tags) < 1):
        print(f"No <{tag}> tags found!")
        return
```
Once we are sure that tags were found. Let's provide the user with the option of show them or not in case that there are too much results:
```python
    print(f"Found <{len(tags)}> {tags[0].tag_name} tags.")
    if input("Show them? (y/n): ") not in set(['y', 'Y']):
        return
```
If the user decided to see the results, let's use a `for` loop to print, from each tag object, its label.
```python
    for tag in tags:
        print(f"\t<{tag.tag_name}>{tag..text}<{tag.tag_name}>")
    print("(end of list)\n\n")
```
All together:
```python
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
```

## quit(self)
To end things up, let's just make a presentable exiting method in which we just print that the program is in fact exiting, since sometimes this process actually takes quite a few seconds.
```python
def quit(self):
    print("Exiting . . .")
    self.driver.quit()
```

## Execution screenshots:
Right when the execution is started a web browser is launched:
![Execution Image 1](https://raw.githubusercontent.com/CristianCazares/SeleniumStringRecognition/main/exec1.png)

Then in this screenshot, we can see how the user already interacted with the program and it is already finished (which closes the web browser).
![Execution Image 2](https://raw.githubusercontent.com/CristianCazares/SeleniumStringRecognition/main/exec2.png)
