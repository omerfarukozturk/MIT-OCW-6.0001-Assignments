# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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

    #delete this line and replace with your code here
    for idx in range(len(sequence)):
      if len(sequence) == 1 or len(sequence) == 0:
        return { sequence }

      first_char = sequence[:idx+1]
      remaining_string = sequence[idx+1:]
      permutations = get_permutations(remaining_string)

      all_items = []
      
      for perm in permutations:
        for idx in range(len(perm) + 1):
          val = perm[:idx] + first_char + perm[idx:]

          if val not in all_items:
            all_items.append(val)
     
      return all_items

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #delete this line and replace with your code here
      #TEST EXAMPLES
  example_input = 'abc'
  print('Input:', example_input)
  print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
  print('Actual Output:', get_permutations(example_input))
  print()
  
  example_input = 'nna'
  print('Input:', example_input)
  print('Expected Output:', ['nna', 'nan', 'ann'])
  print('Actual Output:', get_permutations(example_input))
  print()
  
  example_input = 'aaa'
  print('Input:', example_input)
  print('Expected Output:', ['aaa'])
  print('Actual Output:', get_permutations(example_input))
  print()
  
  example_input = 'hat'
  print('Input:', example_input)
  print('Expected Output:', ['hat', 'aht', 'ath', 'hta', 'tha', 'tah'])
  print('Actual Output:', get_permutations(example_input))
  print()

