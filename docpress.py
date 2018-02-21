from bs4 import BeautifulSoup
from bs4 import element
from html.parser import HTMLParser
import datetime
import os
import codecs

def decodeHtml(input):
    h = HTMLParser()
    s = h.unescape(input)
    return s

def removeClass(tag):
    if('class' in tag.attrs):
        del tag['class']
    if len(tag.contents):
        for child in tag.contents:
            if isinstance(child, element.Tag):
                removeClass(child)

# input html
path = input('Input the html file name:')
file = open(path, 'r')
html = (file.read())
file.close()

soup = BeautifulSoup(html, 'html.parser')

# clear
soup.style.decompose()
removeClass(soup)

# code wrap
p = soup.p
while p:
    if '```' in p.text:
        language = p.text[3:]
        # print(language)
        codeHead = p
        p = p.find_next_sibling('p')
        content = ''
        while p and '```' not in p.text:
            content += p.text + '\n'
            temp = p
            p = p.find_next_sibling('p')
            temp.decompose()
        codeTail = p
        codeTail.decompose()

        codeTag = soup.new_tag('pre')
        codeTag['class'] = 'theme:vs2012-black font:consolas lang:'+language+' decode:true'
        codeTag.string = content
        codeHead.span.replace_with(codeTag)
    p = p.find_next_sibling('p')


print('Rename images meaningfully:')
# image rename
today = datetime.date.today()
urlPrefix = '%s//wp-content/uploads/%d/%d/' % (
    'https://openingsource.org',
    today.year,
    today.month
)
for img in soup.find_all('img'):
    src = img['src']
    dir = img['src'][0:img['src'].rindex('/') + 1]
    oldName = img['src'][img['src'].rindex('/') + 1:]
    suffix = oldName[oldName.rindex('.') + 1:]
    name = input(oldName + ' -> ')
    if '.' not in name:
        name = name + '.' + suffix

    if not os.access(src, os.F_OK):
        print('    ' + src + " doesn't exist")
    elif os.access(dir + name, os.F_OK):
        print('    ' + dir + name + " has exist")
    else:
        os.rename(src, dir + name)
    img['src'] = urlPrefix + name

outHtml = str(soup)
file = codecs.open(path + '.out.html', 'w', 'utf-8')
file.write(outHtml)
file.close()

print('Successfully saved at ' + path + '.out.html')
print('Please copy its content to your wordpress editor')
print('and upload renamed images')
s