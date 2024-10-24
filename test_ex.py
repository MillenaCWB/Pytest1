def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b


def test():
    assert soma(8,9) == 17
    assert soma(10,5) == 15
    assert soma(8,5) == 13

def test_sub ():

    assert subtracao(5,3) == 2
    assert subtracao(3,3) == 0
    assert subtracao(5,4) == 1
            

def test_sub ():

    assert multiplicacao(4,4) == 16
    assert multiplicacao(5,10) == 50
    assert multiplicacao(7,9) == 63
            

            
def test_sub ():

    assert divisao(8,4) == 2
    assert divisao(120,4) == 30
    assert divisao(90,2) == 45
            