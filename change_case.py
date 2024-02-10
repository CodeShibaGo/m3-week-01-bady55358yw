def change_case(input_str, case):
    if case == 'upper':
        return input_str.upper()
    elif case == 'lower':
        return input_str.lower()
    else:
        print('case輸入有誤')

result = change_case("", "")
print(result)











