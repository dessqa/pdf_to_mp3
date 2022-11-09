from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language='en'):
    try:
        assert Path(file_path).is_file()            #Проверяем наличие файла в директории
        assert Path(file_path).suffix == '.pdf'     #Проверяем формат файла

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        
        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        m_path = Path(f'{file_name}.mp3')

        return f'Файл {file_name}.mp3 готов!\nРазмер файла равен {m_path.stat().st_size} б.'

    except AssertionError:                          #assert выполняет проверку истинности выражения, елси нет - AssertionError
        return 'File not exist!'


def main():
    tprint('PDF TO MP3', font='block')
    file_path = input('Введите путь до файла: ')
    language = input('Введите язык для чтения (en или ru): ')
    print(pdf_to_mp3(file_path, language))
    

if __name__ == '__main__':
    main()