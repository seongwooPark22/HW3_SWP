
def reverse_words(input_str) :
    reversed_words_list = input_str.split()[::-1]
    return " ".join(reversed_words_list)

def main() :
    input1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    input2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    
    print("\nINPUT1:")
    print(input1,"\n\nOUTPUT :",reverse_words(input1))
    print("\nINPUT2:")
    print(input2,"\n\nOUTPUT :",reverse_words(input2))

if __name__ == "__main__" :
    main()

