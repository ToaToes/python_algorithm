# python_algorithm
learn python basics and to solve leetcode

## 1. mapping in python:
```
translation = {

  "abc": 1,
  "sdf": 2,
  "ert": 3,

  ...
}

num = translation["abc"]
```
_____
```
# Create a translation table for characters
translation_table = str.maketrans("abc", "123")

# Translate a string using the table
original_string = "abcde"
translated_string = original_string.translate(translation_table)

print(translated_string)  # Output: "123de"

```

## How to slice a string
str[:5]: This will return the first five characters. </br>
str[5:]: This will return the string starting from the sixth character to the end. </br>
str[1:5]: This will return the characters from index 1 to index 4 (not including index 5). </br>
