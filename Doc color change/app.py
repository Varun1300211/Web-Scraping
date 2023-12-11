from docx import Document
from docx.enum.text import WD_COLOR_INDEX
def highlight_text(filename):
    doc = Document(filename)
    for paragraph in doc.paragraphs:
        if 'excellent' in paragraph.text:
            for run in paragraph.runs:
                if 'excellent' in run.text:
                    x = run.text.split('excellent')
                    run.clear()
                for i in range(len(x)-1):
                    run.add_text(x[i])
                    run.add_text('excellent')
                    run.font.highlight_color = WD_COLOR_INDEX.YELLOW

    doc.save('t2.docx')
    return 1
if __name__ == '__main__':

    highlight_text('D:\Web Scraping Tute\Doc color change\Sample1.docx')