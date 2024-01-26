def abbrev_name(name):

  # 用 split() 將各單字拆成一個 List (範例：["John", "Smith"])
  nameList = name.split()

  # firstLetter 為 List 的第一個位置 (範例："John")
  firstLetter = nameList[0]

  # secondLetter 為 List 的第二個位置 (範例："Smith")
  secondLetter = nameList[1]

  # 取出 firstLetter 的第一個字的位置 (範例："J") 和 secondLetter 第一個字的位置 (範例："S")
  ans = f"{firstLetter[0]}.{secondLetter[0]}"

  return ans

print(abbrev_name("John Smith"))



