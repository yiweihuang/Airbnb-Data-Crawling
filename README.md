# Airbnb-Data-Crawling
Scrape informations from
- [Inside Airbnb](http://insideairbnb.com/get-the-data.html)

Get started
==
### Install python package!
```
$ pip install scrapy
```

### Scrapy Tutorial

```
## 1. Creating a project
$ scrapy startproject [project name]

## 2. How to run our spider
$ scrapy crawl [Spider]

## 3. Storing the scraped data
$ scrapy crawl [Spider] -o [spider.json]

```


### Usage
**1. Crawl the website of Inside Airbnb**
```python
scrapy crawl airbnb_site
```
