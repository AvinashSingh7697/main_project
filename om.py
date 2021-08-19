class A:
    a=2
    b=3
    def __init__(idea,a,b):
        idea.a=a
        idea.b=b
        


if __name__=="__main__":
    obj = A(4,6)
    print(obj.a)