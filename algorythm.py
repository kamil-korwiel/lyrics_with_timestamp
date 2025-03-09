original_lyrics = """Passin' around, your blood and your body
No conversation to ease up your mind
And nobody seems to see the outside of it
Preoccupied, and nobody's hiding it
Preoccupied, nobody's hiding it
Preoccupied, nobody's hiding it
Opened your mind, filled it with bullshit 
Locked up your heart, without even knowing it
It must be a sign, the days that we're living in
Preoccupied, and nobody's hiding it
Preoccupied, and nobody's hiding it
Preoccupied, nobody's hiding it
Preoccupied, yeah, and nobody's hiding it
Preoccupied, and nobody's hiding it"""

gen_lyrics = """Passing around You're blind in your body
No conversation To ease up your mind
When nobody sings To see the outside of it 
Preoccupied Nobody's hiding it 
Preoccupied Nobody's hiding it 
Preoccupied Nobody's hiding it 
Opened your mind Filled it with bullshit 
Locked up your heart Without even knowing it 
Must be a sign The days that we're living in
Preoccupied And nobody's hiding it 
Preoccupied Nobody's hiding it 
Preoccupied Nobody's hiding it 
Preoccupied Nobody's hiding it 
Preoccupied Nobody's hiding it""" 

from pyphonetics import Soundex


def biggest_string_number(*args:list[str]):
    big = 0
    for the_list in args:
        if big < len(the_list.__str__()):
            big = len(the_list.__str__())
    return big

def show_phone(original:list[str], gen:list[str]):
    soundex = Soundex()

    arr_phon_org = [ soundex.phonetics(word) for word in original ]
    arr_phon_gen = [ soundex.phonetics(word) for word in gen ]

    print(arr_phon_org)
    print(arr_phon_gen)


def naive_spread_algorithm(original:list[str], gen:list[str]):
    len_gen = len(gen)
    len_original = len(original)

    SPREAD = 5

    def start(index:int):
        return SPREAD * index
    
    def end(index:int, length:int):
        return length - (length - SPREAD * index)

    slice = (start(0), end(0))

    for index_gen in range(len_gen):
        for index_original in range(slice[0],slice[1]):
            pass


def first_index_spread_algorithm(original:list[str], gen:list[str], spread:int = 3) -> list[tuple]:
    len_gen = len(gen)
    len_original = len(original)

    SPREAD = spread

    # index_balk = 0

    similar_words = []

    for index_original in range(len_original):
        word = original[index_original]
        for index_spread in range(index_original, SPREAD+index_original):
            if index_spread < len_gen:
                if word.lower() == gen[index_spread].lower():
                    similar_words.append((index_original, index_spread))
                    break
    
    return similar_words

def balk_spread_algorithm(original:list[str], gen:list[str], spread:int = 5) -> list[tuple]:
    len_gen = len(gen)
    len_original = len(original)

    SPREAD = spread

    index_balk = 0

    index_first_spread_target = 0

    similar_words = []

    for index_original in range(len_original):
        word = original[index_original]


        if SPREAD // 2 + index_balk > index_original: 
            index_first_spread_target = index_balk
        else:
            index_first_spread_target = index_original - SPREAD // 2

        for index_spread in range(index_first_spread_target, SPREAD+index_first_spread_target):
            if index_spread < len_gen:
                if word.lower() == gen[index_spread].lower():
                    similar_words.append((index_original, index_spread))
                    index_balk = index_spread + 1
                    break
    
    return similar_words

def main():
    # print(original_lyrics.replace('\n', ' ').split())
    # print(gen_lyrics.replace('\n', ' ').split())
    LENGTH:int

    gen_lines = gen_lyrics.split('\n')
    org_lines = original_lyrics.split('\n')
    

    if len(gen_lines) > len(org_lines):
        LENGTH = len(gen_lines)
    else:
        LENGTH = len(org_lines)

    for index in range(0 ,LENGTH):
        
        org_line = [word.strip(',') for word in org_lines[index].split()]
        gen_line = [word.strip(',') for word in gen_lines[index].split()]

        bsn = biggest_string_number(org_line,gen_line)
        
        print(" "*(bsn+4),"------------------")
        print('org:', org_line)
        print('gen:', gen_line)
        
        # indexes = balk_spread_algorithm(org_line, gen_line)
        # for org, gen in indexes:
        #     print(f'{org_line[org]} === {gen_line[gen]}', (org, gen))
        
        show_phone(org_line, gen_line)
        


if __name__ == "__main__":
    main()