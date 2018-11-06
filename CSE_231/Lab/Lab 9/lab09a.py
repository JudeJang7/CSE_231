
import string

def build_word_set( input_file ):
    
    word_set = set()
    
    for line in input_file:

        # Making a list of every word in the line
        word_lst = line.strip().split()

        # Puts all of the word in lower case and gets rid of all punctuation
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        
        for word in word_lst:
            
            if word != "":

                # If the world is not an empty string, add it to the set of words
                word_set.add( word )
                
    return word_set


def compare_files( file1, file2 ):

    # Build two sets:
    #   all of the unique words in file1
    #   all of the unique words in file2
    set1 = build_word_set(file1)
    set2 = build_word_set(file2)

    # Display the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.
    unique_word_count = set1 | set2
    print("Total unique words:", len(unique_word_count))

    # Display the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.
    unique_word_in_both_count = set1 & set2
    print("Unique words that appear in both files:", len(unique_word_in_both_count))
  
     
######################################################################

f1 = open( "document1.txt" )
f2 = open( "document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()

