from bs4 import BeautifulSoup
import requests
import json

# Function to scrape PDF links from a webpage
def scrape_pdf_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = []
    content_block = soup.find('div', class_='conteudo_simples', attrs={'rel': '2015'})
    if content_block:
        table = content_block.find('table')
        if table:
            links = table.find_all('a', href=True)
            for link in links:
                if link['href'].endswith('.pdf'):
                    pdf_links.append(link['href'])
    return pdf_links

# Main function
def main():
    try:
        # URL of the webpage containing the PDF links
        url = 'https://www.globo.com/'
        
        # Scrape PDF links
        pdf_links = scrape_pdf_links(url)

        if pdf_links:
            # Write PDF links to a JSON file
            with open('pdf-links-2015.json', 'w') as file:
                json.dump(pdf_links, file, indent=2)
            print('Os links PDF foram salvos em pdf-links.json!')
        else:
            print('Nenhum link PDF correspondente foi encontrado.')
    except Exception as e:
        print('Ocorreu um erro:', e)

if __name__ == "__main__":
    main()
