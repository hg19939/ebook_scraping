# Scraping free tech-related e-books

## Project's goal
This project was developed during the first two weeks of the author's Frontrunners internship at the [University of Essex's CSEE department](https://www.essex.ac.uk/departments/computer-science-and-electronic-engineering) as a research assistant. The goal is to crawl the [FreeTechBooks](https://www.freetechbooks.com/) website, collecting data such as titles, plots, and download links about the presented books. The data is then saved as an Elasticsearch index for maximum efficiency uppon querying.

## Technologies used
The author took advantage of the following technologies to develop the project:
- Language: Python
- Libraries: csv, requests, BeautifulSoup
- Database: Elasticsearch's Python API

## What is Web Crawling?
According to the following Wikipedia [article](https://en.wikipedia.org/wiki/Web_crawler), Web crawling is the process of indexing the Web by a bot (often called crawler or spider). The process is usually operated by a search engine. This procedure is often times followed by Web scraping, which aims to extract data from a given page, in our case e-books' titles, plots, and download links. Refer to [this](https://en.wikipedia.org/wiki/Web_scraping) article for more information about Web scraping.
