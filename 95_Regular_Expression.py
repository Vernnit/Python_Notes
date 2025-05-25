# Regular expression is used to search and match particular patterns of text.

# r"string"  is for raw string which kills the power of escape characters like back slash \. Not to handle back slashes in any special way.

import re

text_to_search = '''
a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
0123456789

Ha HaHa

Meta characters (needs to be escaped) :

. ^ $ * + ? {} [] () | 

URL -
google.com     ( '.' needs to be escaped in url - google\.com)
    
321-555-4321
123.555.1234

Mr. Potter 
Mr  Weasley
Mrs Grenger
Mrs Ginny

Mr. X

'''

# Case Sensitive . Matches in a sequence only. No match for abc or cba.
pattern = re.compile('a b c')
pattern = re.compile()
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


'''                            Some special characters and what they match -

.  -   Any character except new line.
\d -   Digits (0-9)
\D -   Not a digit (0-9)
\w -   Word character (a-z , A-Z , 0-9 , _)
\W -   Not a word character.
\s -   White Spaces ( space , tab , newline)
\S -   Not White Spaces ( space , tab , newline)

'''
'''
\	Marks the next character as either a special character or a literal. For example, n matches the character n, whereas \n matches a newline character. The sequence \\ matches \ and \( matches (.

^	Matches the beginning of input.

$	Matches the end of input.

*	Matches the preceding character zero or more times. For example, zo* matches either z or zoo.

+	Matches the preceding character one or more times. For example, zo+ matches zoo but not z.

?	Matches the preceding character zero or one time. For example, a?ve? matches the ve in never.

.	Matches any single character except a newline character.

(pattern)	Matches a pattern and remembers the match. The matched substring can be retrieved from the resulting matches collection by using this code: Item [0]...[n]. To match parentheses characters ( ), use \( or \).

x|y	Matches either x or y. For example, z|wood matches z or wood. (z|w)oo matches zoo or wood.

{n}	n is a non-negative integer. Matches exactly n times. For example, o{2} does not match the o in Bob, but matches the first two os in foooood.

{n,}	In this expression, n is a non-negative integer. Matches the preceding character at least n times. For example, o{2,} does not match the o in Bob and matches all the os in foooood. The o{1,} expression is equivalent to o+ and o{0,} is equivalent to o*.

{n,m}	The m and n variables are non-negative integers. Matches the preceding character at least n and at most m times. For example, o{1,3} matches the first three os in fooooood. The o{0,1} expression is equivalent to o?.

[xyz]	A character set. Matches any one of the enclosed characters. For example, [abc] matches the a in plain.

[^xyz]	A negative character set. Matches any character that is not enclosed. For example, [^abc] matches the p in plain.

[a-z]	A range of characters. Matches any character in the specified range. For example, [a-z] matches any lowercase alphabetic character in the English alphabet.

[^m-z]	A negative range of characters. Matches any character that is not in the specified range. For example, 

[m-z] matches any character that is not in the range m through z.

\A	Matches only at beginning of a string.
\b	Matches a word boundary, that is, the position between a word and a space. For example, er\b matches the er in never but not the er in verb.
\B	Matches a non word boundary. The ea*r\B expression matches the ear in never early.
\d	Matches a digit character.
\D	Matches a non-digit character.
\f	Matches a form-feed character.
\n	Matches a newline character.
\r	Matches a carriage return character.
\s	Matches any white space including spaces, tabs, form-feed characters, and so on.
\S	Matches any non-white space character.
\t	Matches a tab character.
\v	Matches a vertical tab character.
\w	Matches any word character including underscore. This expression is equivalent to [A-Za-z0-9_].
\W	Matches any non-word character. This expression is equivalent to [^A-Za-z0-9_].
\z	Matches only the end of a string.
\Z	Matches only the end of a string, or before a newline character at the end.
'''
