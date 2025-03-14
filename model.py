import json
from dataclasses import dataclass

@dataclass
class Word:
    content:str
    start:float
    end:float
    confidence:float




if __name__ == "__main__":
    array_words = []
    
    with open("./gen_lyrics.json", 'r') as file:
        json_lyrics:dict = json.loads(file.read())

        segments:list = json_lyrics.get('segments')
        one_line_text:str = json_lyrics.get('text')
        
        full_words_lyrics = one_line_text.split()
        
        for seg in segments:
            for word_json in seg['words']:
                word = Word(
                    content=word_json['text'],
                    start=word_json['start'],
                    end=word_json['end'],
                    confidence=word_json['confidence']
                )
                array_words.append(word)
        
        print(len(full_words_lyrics), len(array_words))
        
        
        

                

