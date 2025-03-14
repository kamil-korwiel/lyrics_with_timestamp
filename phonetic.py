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


from pyphonetics import RefinedSoundex




def main():
    lines_original = original_lyrics.split('\n')
    lines_gen = gen_lyrics.split('\n')

    rs = RefinedSoundex()
    
    index = 8

    original = lines_original[index].split()
    generating = lines_gen[index].split()
    
    if(len(original) == len(generating)):
        print(original)
        list_phon_org = [ rs.phonetics(word) for word in original ]
        print(list_phon_org)

        print(generating)
        list_phon_gen = [ rs.phonetics(word) for word in generating ]
        print(list_phon_gen)


        list_dist =[]
        for org, gen in zip(original, generating):
            list_dist.append(rs.distance(org,gen))
        
        print(list_dist)
    else:
        print("Not the same length")
    
    print(rs.distance("fuck","you"))


        


if __name__ == "__main__":
    main()


