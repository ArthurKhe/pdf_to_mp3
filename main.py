import pdfplumber
from gtts import gTTS
from pathlib import Path


def pdf_to_mp3(filename, language):
    if Path(filename).is_file() and Path(filename).suffix == ".pdf":
        with pdfplumber.PDF(open(file=filename, mode="rb")) as file:
            pages = [page.extract_text() for page in file.pages]
            text = "".join(pages)
            text = text.replace("\n", "")
            audio = gTTS(text=text, lang=language)
            filename_audio = Path(filename).stem
            audio.save(f"{filename_audio}.mp3")
            return f"[+] mp3 file {filename_audio} successfully create"
    else:
        return "[-] FileNotFound"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = input("filename: ")
    language = input("language: ")
    print(pdf_to_mp3(filename=file, language=language))

