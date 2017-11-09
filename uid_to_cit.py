with open('blockchain_uid.txt') as f:
    text = f.read()
text, num_cit = text.split('%%%')

brack = []
current_citation = ''
citations = []
for char in text:

    if len(brack) > 0:
        if char != ']':
            current_citation += char
        else:
            brack.pop()
            citations.append(current_citation)
            current_citation = ''
    if len(brack) == 0:
        if char == '[':
            brack.append(char)

num_citations = int(num_cit)
#num_citations = 22
references = citations[-1 * num_citations:]

cit_index = {}
for x, ref in enumerate(references):
    text = text.replace(ref, str(x+1))

with open('blockchain_cit.txt', 'w+') as f:
    f.write(text)
