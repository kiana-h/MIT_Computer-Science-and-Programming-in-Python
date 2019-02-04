# Problem Set 4A
# Name: Kiana Hosseini

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    #base case: if the string is only 1 letter long, return itself
    if len(sequence) == 1:
        permutations=[sequence]
    
    else:
      for i,value in enumerate(sequence):
          #recursion: take out one charachter at a time and combine it with permutations
          #of the rest of the string.
          for j in get_permutations(sequence[:i] + sequence[i+1:]):
              permutations += [j+value]
    return permutations
    

    

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
                                          