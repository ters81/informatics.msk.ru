# Задача №113658.
# https://informatics.msk.ru/mod/statements/view3.php?id=26735&chapterid=113658#1

# Дана строка, содержащая только маленькие английские буквы.
# Сформировать новую строку путем «сокращения» одинаковых букв, находящихся на симметричных местах
# (то есть если на одинаковом расстоянии от центра строки находятся 2 одинаковые буквы, то их нужно убрать из строки).
# Если длина строки нечетна, то среднюю букву сокращать не нужно.
#
# Входные данные
# Вводится строка ненулевой длины. Известно также, что длина строки не превышает 1000 знаков.
#
# Выходные данные
# Вывести строку, которая получится после "сокращений". Тесты подобраны таким образом, что после сокращений будет оставаться непустая строка.
#
# Примеры
# входные данные
# ptijoydrgfrudwekryneqaiodorathnljczynykmjkwuhqfiuljznpocwgtmnsmkbvfbxyxvbkcnlfvijzkwgudwdhherdmnpjlrrletkqmwkicsnhvahxfnzssjmhgqfaolymmfauwffzhtxqtxjldppwkonqplktrycxtrojfalvpbrkirhsgetksrqalouapifysbmuaunrpjrfejdahqhonlhdxcrugvzpqbezyqeardkydmtbxjonvgvdimxzwqgsqctijgjpnkgcwuqqfcwgntzsyefexrfqhasaojfrxaplvwkhrlpovjthwavuqgxhhxgsuvywhtxvtpfrlkwvlpaxjajoasahqfrxehevszunrwcpidmwcgknpjvxiwgqsgqwzxaiuvyvnthxbtmiygtraewfzebqpzvgulcxdclnohqcazjefrzprnuaumbsybipauoqaqrxktevshkhkrwpvsafjoltxcyrtklpunokwmpfluxtzxphnflwyyammyltafqghmjssznfxhavluscakweqkteqrrljpnmdwehjlqdughkzjovfliqkbvlyxbfvbamsnyvgkpoynujbuifqquwkjmnneyzcjlnzparoqoaaqenwrnexdurfgrdyoxiag

# выходные данные
# ptjwkyidthnykhlzpcwtmkxcniwwdhrlminhofaufztqjdpqrlbirgslfjdhhryqdkdjogdmctjguqqfgtyffrhlojaqsyxtfljahvurpidmvxwgauythigtwflcczzbqxvkhwslumfuzpnlyyatluaeqwjlqhoiqlayvkpyubqnnezpqawnxxag




def stroka(s):
    if len(s) == 1 or len(s) == 0:
        return s
    elif len(s) == 2 and s[0] != s[-1]:
        return s
    elif s[0] == s[-1]:
        s = s[1:-1]
        return stroka(s)
    return s[0] + stroka(s[1:-1]) + s[-1]


print(stroka(input()))