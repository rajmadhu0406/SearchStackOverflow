import SearchSO

try:
    a = 5 + 'str'
except Exception as e:
    SearchSO.checkError(e)