# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 12:25:11 2022

Website scraped: https://www.freetechbooks.com/
Credits: https://www.youtube.com/watch?v=ng2o98k983k

@author: hg19939
"""

# Imports:
import csv
import requests
from bs4 import BeautifulSoup

# Script:
def books_crawling():
    """
    Upon calling, this function will loop through the contents of
    the current web page, extract the name and links of all books
    presented, save them in a dictionary, and finally return it.
    
    Returns
    -------
    links : list
        A list of web links to scrape data from.
        
    @author: hg19939
    """
    
    links = []

    for book in soup.find_all("div", {"class": "col-xs-12"}):
        link = book.p.a["href"]
        links.append(link)
    
    return links
    


def books_scraping(books: list):
    """
    Uppon calling, this function will loop through a list of scraped
    books, extract the plots and download links, before returning them.
    Parameters
    ----------
    books : list
        A list of book webpage links to scrape.

    Returns
    -------
    titles: list
        A list of books' titles.
    plots : list
        A list of books' plots.
    download_links : list
        A list of links to access or download the book from.
        
    @author: hg19939
    """
    
    titles = []
    plots = []
    download_links = []

    for book in books:
        source = requests.get(book).text
        soup = BeautifulSoup(source, "lxml")
        
        title = soup.find("p", {"class": "media-heading lead"}).text
        plot = soup.find("p", "")
        link = soup.find("a", {"class": "btn btn-primary"})["href"]
        
        titles.append(title)
        plots.append(plot.text)
        download_links.append(link)
    
    return titles, plots, download_links


def save_as_csv(csv_file, titles: list, plots: list, links: list):
    """
    Upon calling, this function will save the scraped books' titles, 
    plots, and download links as a CSV file for convinient use.

    Parameters
    ----------
    csv_file : TYPE
        DESCRIPTION.
    titles : list
        Books' titles.
    plots : list
        Books' plots.
    links : list
        A list of links to access or download the book from.

    Returns
    -------
    None.

    @author: hg19939
    """
 
    if(len(titles) == len(links)):
        for i in range(len(titles)): csv_writer.writerow([titles[i], plots[i], links[i]])
    else:
        print("Number of titles do not match the number of links.")
    
    
# Create a CSV file to store the books:
csv_file = open("scraped_books.csv", "a", encoding="utf-8")
csv_writer = csv.writer(csv_file)

# Loop through all pages:
for page_num in range(1, 86):
    source = requests.get("https://www.freetechbooks.com/topics?page={}".format(page_num)).text    
    soup = BeautifulSoup(source, "lxml")
    
    links = books_crawling()
    titles, plots, download_links = books_scraping(links)
    save_as_csv(csv_file, titles, plots, download_links)

# Close the CSV file:
csv_file.close()
