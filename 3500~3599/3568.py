# iSharp 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	3289	1377	1146	42.555%
# 문제
# 선영이는 C, C++, Java와는 다른 아주 세련된 언어를 만들었다. 선영이는 이 아름답고 예술적인 언어의 이름을 i#으로 정했다.

# i#은 기본 변수형과 배열([]), 참조(&), 포인터(*)를 제공한다. 배열, 참조, 포인터는 순서에 상관없이 혼합해서 사용할 수 있다. 즉, int의 참조의 참조의 배열의 포인터도 올바른 타입이다. int&&[]*

# i#은 여러 개의 변수를 한 줄에 정의할 수 있다. 공통된 변수형을 제일 먼저 쓰고, 그 다음에 각 변수의 이름과 추가적인 변수형을 쓰면 된다. 예를 들면 아래와 같다.

# int& a*[]&, b, c*;

# a의 타입은 int&&[]*, b는 int&, c는 int&*이 된다. 변수의 오른편에 있는 변수형은 순서를 뒤집어서 왼편에 붙일 수 있다. 따라서, int*& a는 int a&*와 같다.

# 변수의 선언이 보기 복잡하고 혼란스럽기 때문에, 앞으로는 한 줄에 변수를 하나씩 선언하려고 한다.

# i#의 변수 선언문이 주어진다. 이때, 각각의 변수의 오른편에 있는 변수형을 모두 왼쪽으로 옮기고, 한 줄에 하나씩 선언하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 i#의 변수 선언문이 주어진다. 이 선언문에는 변수가 여러개 포함되어 있을 수도 있다.

# 선언문의 가장 처음에는 기본 변수형이 주어진다. 그 다음에는 추가적인 변수형이 주어진다. 추가적인 변수형은 없을 수도 있다. 그 다음 공백 이후에는 변수 선언이 하나씩 주어진다. 변수 선언은 콤마와 공백으로 나누어져 있고, ;로 끝난다. 각 변수의 선언 처음에는 기본 변수명이 주어진다. 그 다음에는 추가적인 변수형이 주어진다. 추가적인 변수형은 없을 수도 있다.

# 기본 변수형과 변수명은 같지 않으며, 알파벳 소문자와 대문자로만 이루어져 있다. 각 줄의 길이는 120글자를 넘지 않는다.

# 출력
# 입력으로 주어진 변수 선언문을 문제의 조건에 맞게 변형한 뒤, 한 줄에 하나씩 출력한다. 변수형과 변수명 사이에는 공백이 하나 있어야 한다. 출력은 입력으로 주어진 변수 선언문에서 변수가 선언된 순서대로 출력한다.

# 예제 입력 1 
# int& a*[]&, b, c*;
# 예제 출력 1 
# int&&[]* a;
# int& b;
# int&* c;

words = input().replace(',', "").split(';')[0].split()

for index in range(1, len(words)):
    temp = ""
    print(words[0], end='')
    for i in range(len(words[index])-1, -1, -1):
        if not words[index][i].isalpha() :
            if  words[index][i] == '[' :
                print(']', end='')
            elif words[index][i] == ']' :
                print('[', end='')
            else :
                print(words[index][i], end='')
        else :
            temp += words[index][i]
    print(" ", end='')
    temp = list(temp)[::-1]
    temp = ''.join(temp) + ";"
    print(temp)
