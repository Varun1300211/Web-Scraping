from docx import Document

def highlight_text(filename):

    doc = Document(filename)
    for p in doc.paragraphs:
        if 'random' in p.text:
            inline = p.runs
            # print(inline)
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                # print((inline[i].text).encode('ascii'))
                if 'random' in inline[i].text:
                    x=inline[i].text.split('random')
                    inline[i].clear()
                    for j in range(len(x)-1):
                        inline[i].add_text(x[j])
                        y=inline[i].add_text('random')
                        y.highlight_color='YELLOW'
            # print (p.text)

    doc.save('t3.docx')
    return 1
if __name__ == '__main__':

    highlight_text('Sample.docx')