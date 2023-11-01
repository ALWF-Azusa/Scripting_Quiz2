n = eval(input("請輸入金字塔高度："))
for i in range(1, n + 1, 2):
    """
    range (1 , n+1 , 2 )
    if n = 5 then the number will be (1,6,2)
    it means
    3 (1+2)
    5(3+2)
    7(5+2)
    so the number 7 is greater than 6 so the 7 won't be export
    So answer is 3,5
    """
    print(" " * ((n - i) // 2) + "*" * i)
    # input 9 it means Less than 10 so the i will be 1,3,5,7,9
    """
    stage 1 print("." * ((9 - 1) // 2) + "*" * i) it will print ....*
    stage 2 print("." * ((9 - 3) // 2) + "*" * i) it will print ...***
    stage 3 print("." * ((9 - 5) // 2) + "*" * i) it will print ..*****
    以此類推
    """

for i in range(n - 2, 0, -2):
    """
    range (n-2 , 0 , -2 )
    if n = 5 then the number will be (3,0,-2)
    it means
    1 (3-2)
    -1(1-2)
    so the number -1 is greater Less than 0 so the -1 won't be export
    So answer is 3,5
    """

    print(" " * ((n - i) // 2) + "*" * i)
    """
     i 7,5,3,1
     n 9,9,9,9
    stage 1 print("." * ((9 - 7) // 2) + "*" * i) it will print .*******
    stage 2 print("." * ((9 - 5) // 2) + "*" * i) it will print ..*****
    stage 3 print("." * ((9 - 3) // 2) + "*" * i) it will print ...***
    以此類推
    """
