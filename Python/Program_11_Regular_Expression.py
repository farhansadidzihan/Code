# || Findall Method ||
import re
# In Regular Expression, (^) - Carret means Starting & ($) means Ending 
number = "phone numbers :- 017 16077241, 000 00000000, 017 05287979, 013 03250830"
is_not = re.findall(r"01[356789]\s*\d{8}", number)
print(is_not)

# || Sub Method ||
import re
date = "22/07/2017, 20/01/2017, 01/01/2018"
modify = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", date)
# modify = re.sub(r"(\d{2})/(\d{2})/(\d{4})", "\g<3>-\g<2>-\g<1>", date) # Can Be written like \g<.>
print(modify)

