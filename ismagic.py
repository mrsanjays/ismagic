def IsMagic(num):
    while num>9:
        sum=0
        while num:
            sum+=num%10
            num//=10
        num=sum
    if num==1:
        return 1
    return 0

if __name__ == '__main__':
    num=int(input())
    print(IsMagic(num))

    """
    Given a number A, check if it is a magic number or not.

A number is said to be a magic number if the sum of its digits is calculated till a 
single digit recursively by adding the sum of the digits after every addition.
 If the single digit comes out to be 1, then the number is a magic number.
    """