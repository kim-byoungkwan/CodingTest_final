def f_r_check(s):
    qu = []
    st = []
    for i in s:
        if i.isalpha():
            qu.append(i.lower())
            st.append(i.lower())

    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

print(f_r_check("Wow"))
print(f_r_check("Madam, I'm Adam."))
print(f_r_check("Madam, I am Adam."))
