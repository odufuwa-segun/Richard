# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:36:20 2020

@author: Admx
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:30:55 2020

@author: Admx
"""
#import libraries (Beautiful soup and the requests for making http calls)
import bs4
from bs4 import BeautifulSoup
import requests


url = 'https://ca.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DHGYZjLnRe6um2gI2SDUCDtCqnnGij240F4TviV07L3qO_aJVz1-sI2cw2aG4yYR8X6AyjiNTUlx7uMTqG0T3-ZNK52CA75_E--w4YJMlsfHCWR06eAAXe1x4lmhXfTpwOcb9yFdc5ciFSC_8TQVXq5vsUHdjEqKEAQVhiRSqki3QTEUEovL6Eb5ps7XKXEOnl3HToY-kSJA-bvf3fnnMgOf6Vo4SwetPIVnLHEOGSKyDxizf_x5Cm8yayH9Fs8NkpM8dVndRLQbkPblhss3SAsSrHqDjiN6CdlOFWl_wOaMApjlJpJ8aeO35ix47-v-kGMYPjE7BHlEfmcYwfCm1jsDDm7hE7isbq5B-2hTjW3y4OxCbrPD3XzirpO0gYscEiVaIdGxM7-QcY48lcq3paL0KrvZ_6Obp33F49LJryklh7Jx7-bxAT4gjJRrhKvIvUzI6WlADy84Zm3C09q-iS&p=1&fvj=1&vjs=3&tk=1epc533k5t4hk801&jsa=8613'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

content_wrap = soup.find(id='viewJobSSRRoot')

title_wrap = content_wrap.find(name='h1', attrs={'class': 'jobsearch-JobInfoHeader-title'})
description_wrap = soup.find(id='jobDescriptionText')
meta_wrap = soup.find(name='div', attrs={'class': 'jobsearch-InlineCompanyRating'})

# location_info = content_wrap.find(name='div', attr={'class': 'jobsearch-DesktopStickyContainer-companyrating'})
# print(soup.select('.jobsearch-InlineCompanyRating > div')[0].get_text())



job_title = title_wrap.get_text()
job_description = description_wrap.get_text()
job_posting_date = soup.select('.jobsearch-JobMetadataFooter > span')[0].get_text()
job_type = soup.select('.jobsearch-JobInfoHeader-subtitle > div')[1].get_text()
job_company = soup.select('.jobsearch-InlineCompanyRating > div')[0].get_text()



# job_company = 
print('Title: ', job_title)
print('Description: ', job_description)
print('Posting Date: ', job_posting_date)
print('Type: ', job_type)
print('Company: ', job_company)



# title  = title_wrap.text




# jobsearch-JobInfoHeader-title


# jobsearch-JobInfoHeader-title





# viewJobSSRRoot









# def getSearchPageResult(soup):
#     results = []
#     for div in soup.find_all(name='div', attrs={'class':'jobsearch-SerpJobCard'}):
#         print(div)



# url = 'https://ca.indeed.com/jobs?q=customer+service&l=Ottawa%2C+ON'

# page = requests.get(url)
# print(page.text)

# soup = BeautifulSoup(page.text, 'html.parser')


# results = getSearchPageResult(soup)



def scrapSearchPage(html_content):
    '''
    Scrap search page to fetch job posting

    Returns
    -------
    None.

    '''
    
    