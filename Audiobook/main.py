import pyttsx3
import pdfReader
book = open('Vienna2.pdf', 'rb')
pdfReader = pdfReader.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(1)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()