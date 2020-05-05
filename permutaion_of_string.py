'''
    Question : Permutations of a given string
    ------------------------------------------
    For example:
    ------------- 

    Input : ABC
    output : ABC ACB BAC BCA CBA CAB

'''
# if the length of string(N) is 3 then total permutation is 6 | ( n! )

output = [] 
  
def permutation_of_string(data, i, length):  
    if i == length:  
        output.append(''.join(data) ) 
    else:  
        for j in range(i, length+1):  
            data[i], data[j] = data[j], data[i]  
            permutation_of_string(data, i + 1, length)  
            data[i], data[j] = data[j], data[i] 
        return ' '.join(output)  

if __name__ == '__main__':
    data = input("Enter data : ")
    output_data = permutation_of_string(list(data), 0, len(data)-1)
    print(f'Output : {output_data}')

