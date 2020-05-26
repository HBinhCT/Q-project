import re

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"
m = re.findall(fr'(?<=[{consonants}])([{vowels}]{{2,}})[{consonants}]', input(), flags=re.I)
print('\n'.join(m or ['-1']))
