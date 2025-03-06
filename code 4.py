var = "Global variable"

def test_scope():
    
    var = "Local variable"
    print("Inside function (local):", var)

print("Outside function (global):", var)

test_scope()