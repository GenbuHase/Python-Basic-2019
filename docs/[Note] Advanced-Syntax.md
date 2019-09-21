# [Note] Advanced Syntax


## Formatted String Literal (v3.6以降)
* ### 1. 基本構文
  ```Python
  # 1. Using str.format method
  name = "hoge"
  print("My name is {}.".format(name)) # My name is hoge.

  # 2. Using f-string
  name = "foo"
  print(f"Your name is {name!r}.") # Your name is foo.
  ```

* ### 2. フォーマッター
  ```Python
  firstName = "fFo"
  lastName = "Hoge"
  name = { first: firstName, last: lastName }

  # All of the codes show "My name is Foo Hoge."
  "My name is {0} {1}.".format(firstName, lastName)
  "My name is {} {}.".format(firstName, lastName)
  "My name is {fName} {lName}.".format(fName = firstName, lName = lastName)
  "My name is {first} {last}.".format(**name)

  # My name is "Foo Hoge".
  "My name is {first+' '+last!r}.".format(**name)
  ```