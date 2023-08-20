def count_local_variables():
    var1 = 10
    var2 = "hello"
    var3 = [1, 2, 3]
    var4 = {"a": 1, "b": 2}
    
    local_variables = locals()
    return len(local_variables)

num_local_variables = count_local_variables()
print("Number of local variables:", num_local_variables)
