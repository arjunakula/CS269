from practnlptools.tools import Annotator

annotator=Annotator()

fp = open("input_captions.txt","r")
fw = open("output_captions.txt","w")
data = fp.read().strip().split("\n")

for caption in data:
    out = annotator.getAnnotations(caption,dep_parse=True)
    pos = out['pos']
    ner = out['ner']
    srl = out['srl']

    replace_phrase = ''
    for i in srl:
        if 'A0' in i:
            replace_phrase = i['A0']
        elif 'A1' in i:
            replace_phrase = i['A1']
        break

    if len(replace_phrase) == 0:
        continue

    if caption.startswith(replace_phrase) == False:
        continue

    filler1 = 'What'
    filler2 = 'What is'
    filler3 = 'Who'
    filler4 = 'Who is'

    is_animate = False
    for i in ner:
        if 'PER' in i:
            is_animate = True

    words = caption.lower().strip().split(" ")
    for i in words:
        if i == 'man' or i == 'woman' or i == 'people' or i == 'person' or i == 'child' or i == 'children' or i == 'adult':
            is_animate = True

    has_VBZ = False
    has_VBG = False

    for i in pos:
        if 'VBZ' in i:
            has_VBZ = True
        elif 'VBG' in i:
            has_VBG = True

    modified_caption = ''
    if is_animate and has_VBZ and has_VBG:
        modified_caption = filler3
    elif is_animate and has_VBZ == False and has_VBG:
        modified_caption = filler4
    elif is_animate == False and has_VBZ == False and has_VBG:
        modified_caption = filler2
    elif is_animate:
        modified_caption = filler3
    else:
        modified_caption = filler1


    
    print pos,ner,srl

    if modified_caption:
        fw.write(caption.replace(replace_phrase, modified_caption)+"\n")
