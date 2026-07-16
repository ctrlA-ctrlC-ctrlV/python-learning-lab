# 1.4 Scope: where a variable lives

def compute():
    result = 42
    return result

compute()
# print(result) # NameError: 'result' is not defined out here