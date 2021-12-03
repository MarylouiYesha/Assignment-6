#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8


to_count=input("Enter your sentence:").lower()


_wcount=len(to_count.split())
print(f"Number of Words:" + str (_wcount))


vowels="AaEeIiOoUu"
_vcount=0
for vwl in to_count:
    if vwl in vowels:
        _vcount= _vcount+ 1
print(f"No. of vowels:" + str (_vcount))

_ccount=0
cons="BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
for cn in to_count:
    if cn in cons:
        _ccount= _ccount + 1
print(f"No. of consonants:" + str (_ccount))
