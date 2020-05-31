import re
'''
regular expression
.           -> any character
*           -> zero or more
+           -> one or more
?           -> zero or one
[a-zA-Z]    -> any word
[0-9]       -> any digit
\W          -> every non alpha and non numaric excliding '_'
\w          -> every alpha and numaric
\D          -> non digit character
\d          -> digit character
$           -> end of string or line
\Z          -> end of string
\s          -> white space
^           -> beginning of string or the opposite to this exp
{}          -> number of repetation like 0{1,3} >> 000 
\.          -> dot character 
re.match
re.search
re.findall
re.sub
'''
## PATTRENS
email = '[a-zA-Z]+(\w|\.)*\@[a-z]+\.([a-z]{1,4})'
    