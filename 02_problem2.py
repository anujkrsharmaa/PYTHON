letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>","Anuj").replace("<|Date|>","24 oct 2028>"))            