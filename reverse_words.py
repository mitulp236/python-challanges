'''
    Question : Reverse words in a given string
    ------------------------------------------
    For example:
    ------------- 

    Input : Hello my name is mitul
    output : mitul is name my Hello

'''

# AIM : Return reverse words of specific string 
def reverse_words(data):
    data = data.split()
    return  " ".join(data[::-1])
    


if __name__ == '__main__':
    data = input("Enter data : ");
    output_data = reverse_words(data)
    print(f'Output : {output_data}')

