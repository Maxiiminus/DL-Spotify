from bs4 import BeautifulSoup
import re
import sys

def download_transcript(file_name):
    DOWNLOAD_PATH = f'data/{file_name}.html'
    OUTPUT_PATH = f'transcriptions/{file_name}.txt'
    html_content = open(DOWNLOAD_PATH, 'r', encoding = 'utf-8').read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extraire tous les éléments span ayant la classe spécifique
    # Utiliser une expression régulière pour correspondre à la partie commune des classes de l'élément <span>
    pattern = re.compile("Text__TextElement-.*encore-text-body-small")

    # Sélectionner les éléments <span> basés sur le pattern de classe et l'attribut dir="auto"
    text_elements = soup.find_all('span', class_=pattern, attrs={"dir": "auto"})
    # Extraire et afficher le texte de chaque élément trouvé
    transcription = ' '.join(element.text for element in text_elements)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as file:
        file.write(transcription)

    print(f"Transcription sauvegardée avec succès dans {OUTPUT_PATH}!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        download_transcript(file_name)
    else:
        print("Veuillez fournir le nom du fichier sans l'extension comme argument.") 