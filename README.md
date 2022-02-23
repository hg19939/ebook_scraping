# Scraping free tech-related e-books

## Project's goal
This project was developed during the first two weeks of the author's Frontrunners internship at the [University of Essex's CSEE department](https://www.essex.ac.uk/departments/computer-science-and-electronic-engineering) as a research assistant. The goal is to crawl the [FreeTechBooks](https://www.freetechbooks.com/) website, collecting data such as titles, plots, and download links about the presented books. The data is then saved as an Elasticsearch index for maximum efficiency uppon querying.

## Technologies used
The author took advantage of the following technologies to develop the project:
- Language: [Python](https://www.python.org/downloads/)
- Modules: [csv](https://docs.python.org/3/library/csv.html), [requests](https://docs.python-requests.org/en/latest/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Database: [Elasticsearch's Python API](https://elasticsearch-py.readthedocs.io/en/v8.0.0/)

## What is Web Crawling?
According to the following Wikipedia [article](https://en.wikipedia.org/wiki/Web_crawler), Web crawling is the process of indexing the Web by a bot (often called crawler or spider). The process is usually operated by a search engine. This procedure is often times followed by Web scraping, which aims to extract data from a given page, in our case e-books' titles, plots, and download links. Refer to this [link](https://en.wikipedia.org/wiki/Web_scraping) for more information about Web scraping.

## Code explanation
The code of this project is divided in two separate *.py* files: *bot.py* and *index.py*.

### bot.py
This file is home of the crawling and scraping functionality which is the hearth of the project. The first function, called *web_crawling()*, aims to craw the contents of the forementioned website and extract the link to every book's sub-page. The links are then saved in a [list](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) which is returned by the function.
```
def web_crawling():
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
```
Logically, the next thing to do would be to scrap the data from these sub-pages, which is exactly what the *web_scraping()* function does.
```
def web_scraping(books: list):
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
```
The function initializes a set of lists to store the relevant books' information. Then a [for loop](https://docs.python.org/3/tutorial/controlflow.html#for-statements) is used to go through each one of them. Inside the loop's body, the title, plot, and link are extracted using the BeautifulSoup module and appended to the relevant lists, before those lists are returned. A relatively straightforward function to save the data as a CSV file is also developed. Finally, the functions are called from within a for loop which is used to go through all of the book catalouge's pages (85 in number). An [HTTP GET request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) is made to each one of them, getting the [HTML](https://en.wikipedia.org/wiki/HTML) structure.

### index.py
The CSV file produced by the script contains all 1261 presented in the website. This CSV file is later used to create an index (simply a collection of documents). The database of choice is Elasticsearch, because of its flexibility and built-in text analysers which allow us to manipulate the text efortlessly. The index implementation can be found within the *index.py* file.

## Conclusion
The written code aims to contribute towards the overall project's goal.
