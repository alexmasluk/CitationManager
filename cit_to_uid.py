from uuid import uuid4

with open('blockchain.txt') as f:
    text = f.read()


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

num_citations = int(citations[-1:][0])

        
#citations = revised_citations[:-1 * num_citations]
references = citations[-1 * num_citations:]


print(references)

reference_ids = []
id_dic = {}
uid = uuid4()
for ref in references:
    while uid in reference_ids:
        uid = uuid4()
    id_dic[ref] = str(uid)
    reference_ids.append(uid)

print(reference_ids)

brack = []
current_citation = ''
start,end = -1,0
newtext = '' 
for x in range(len(text)):
    char = text[x]
    if len(brack) > 0:
        #print('len brack > 0')
        if char != ']':
            #print('char !- ]')
            if start < 0:
                #print('start < 0')
                start = x
        else:
            #print ('char == ]')
            brack.pop()
            end = x - 1
            citation = text[start:end+1]
            if '-' in citation:
                first,last = citation.split('-')
                #print('id:',reference_ids[first])
                first_rep = id_dic[first]
                last_rep = id_dic[last]
                newtext += '[{}-{}'.format(first_rep, last_rep)
            else:
                newtext += '[{}'.format(id_dic[citation])
            #print(citation)
            start = -1
    if len(brack) == 0:
        #print('len brack == 0')
        if char == '[':
            #print('char == [')
            brack.append(char)
        else:
            newtext += char
            
newtext += '%%%{}'.format(num_citations)
with open('blockchain_uid.txt', 'w+') as f:
    f.write(newtext)
    
