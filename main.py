import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
from website import create_app
from dotenv import load_dotenv, find_dotenv


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)