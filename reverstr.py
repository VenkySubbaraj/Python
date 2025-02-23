def replacement_fn(replacement_char, string):
    print("replacement_char:", replacement_char)
    print("org_string:", string)
    
    vowels_string = "aeiou"
    vowels_combined_string = vowels_string.lower() + vowels_string.upper()
    print(vowels_combined_string)
    
    count = 0
    last_index = -1
    
    for i in range(len(string)):
        if string[i] in vowels_combined_string:
            last_index = i
            print(last_index)
    
    string = string[::-1]
    print(string)
    
    last_index_plus = string[last_index + 1:]
    print(last_index_plus)
    replace_string = (string[:last_index] + replacement_char + string[last_index + 1:])
    print(replace_string)
    

def main():
    replacement_char = "*"
    string = "rifaz"
    replacement_fn(replacement_char, string)

if __name__ == "__main__":
    main()
