def main(input_string):
    reversed_string = {
        '(':')',
        '{':'}',
        '[':']'
    }
    
    for char in input_string:
        print(char)
    
    reversed_output = ''.join(reversed_string.get(char,char))
    print(reversed_output)
    

input_string= ':'
main(input_string)
