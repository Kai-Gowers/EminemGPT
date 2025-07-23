def remove_bracketed_text(text):
    result = ''
    inside_brackets = False
    
    for c in text:
        if c == '[':
            inside_brackets = True
        elif c == ']':
            inside_brackets = False
        elif not inside_brackets:
            result += c
            
    return result

with open('eminem_raw.txt', 'r') as f:
    raw_lyrics = f.read()
    
cleaned_lyrics =  remove_bracketed_text(raw_lyrics)

cleaned_lyrics = "\n\n".join([line.strip() for line in cleaned_lyrics.splitlines() if line.strip()])

with open('eminem_cleaned.txt', 'w') as f:
    f.write(cleaned_lyrics)
    