#!/usr/bin/env python
# coding: utf-8

# #1번.
# 
# 클래스와 모듈의 공통점과 차이점에 대해 설명하시오.

# 클래스 : 사용자가 직접 객체를 선언하고 객체 멤버를 구성하여 사용할 수 있다.
# 모듈 :  이미 완성되어 있는 것을 사용자가 가지고 온 후 그 모듈 객체와 객체 멤버를 끌어와서 사용한다.
# 
# 공통점 : 용도에 맞도록 구성한 객체 멤버들을 캡슐화 시킨 후 가져다 사용한다.
# 
# 차이점 : 모듈은 어디서나 접근이 자유로워 사용이 쉬운 반면, 클래스는 그 목적에 맞게 각 프로세스에서 상속하여 사용한다. 
# 모듈은 내부 멤버를 변경하여 사용할 수 없지만, 상속받은 클래스는 멤버를 자유롭게 변경할 수 있다. 

# #2번. 
# 다형성에 대해 설명하고 다형성을 보여주는 자신만의 파이썬 코드 예제를 제시하시오.

# 다형성 : 같은 형태의 코드가 서로 다른 동작을 하는 것
# 다향성을 통해 코드의 양을 줄이고 여러 객체 타입을 하나의 타입으로 관리가 가능하게 만들어 코드의 유지보수에 좋다.

# In[5]:


class Person :
    def __init__(self, name, ID) :
        self.name = name
        self.ID = ID
    
    def explain(self, name, ID) :
        print("[Person] %s : %s" %(self.name, self.ID))
        
class Student(Person) :
    def explain(self) :
        print("[Student] %s : %s" %(self.name, self.ID))
        
class Worker(Person) :
    def explain(self) :
        print("[Office Worker] %s : %s" %(self.name, self.ID))


# In[6]:


student1 = Student("Ahyeon", "2020136087")
worker1 = Worker("Dave", "1234567")
student1.explain()
worker1.explain()


# #3번.
# 다음 각 요구사항 모두를 만족시키는 Counter 클래스를 코딩하시오 (정답을 각 요구사항별로 입력할 필요 없이 3번 문제에 대해 1개의 클래스 정의 코드를 제시하면 된다.)
# 

# In[94]:


class Counter :
    def __init__(self, count, step = None) :
        if step == None :
            self.count = count
            self.step = 1
            return 
        self.count = count 
        self.step = step
        
    def __str__(self):
        return "[Count (step : %d)] %d"%(self.step, self.count)
    
    def incr(self) :
        sum = self.count + self.step
        self.count = sum
        return Counter(self.count)
    
    def __call__(self) : 
        self.incr()

    def __add__(self, other) :
        return Counter(self.count + other)
    
    def __sub__(self, other) :
        return Counter(self.count - other)
    
    def __gt__(self, y) :
        return self.count > y
    
    def __ge__(self, y) :
        return self.count >= y
    
    def __lt__(self, y) :
        return self.count < y
    
    def __le__(self, y) :
        return self.count <= y
    
    def __eq__(self, y) :
        return self.count == y
    
    def __ne__(self, y) :
        return self.count != y


# 요구사항 1. 생성자에 count 값과 step 값을 인자로 받을 수 있다.
# 
# 생성자를 통해 초기 값을 설정해준다. 
# step 값을 받지 않았을 때는 기본값을 1로 설정해준다.
# count, step 값을 모두 받았을 땐 받은 값을 기본값으로 설정한다.

# In[95]:


c = Counter(10)
d = Counter(10, 2)


# 요구사항 2. 다음과 같이 Counter의 인스턴스를 출력을 해주는 __str__() 메소드를 Counter 클래스 내에 구현하시오.
# 
# step과 count 값을 사용해 출력내용을 반환해준다.

# In[96]:


print(c)
print(d)


# 요구사항 3. 다음과 같이 step에 주어진 증분만큼 count를 증가시키는 incr() 메소드를 Counter 클래스 내에 구현하시오.
# 
# count값과 step값을 num 변수에 저장을 한다.
# 그 뒤 count값을 num으로 바꾸어준 뒤, 반환한다. 

# In[97]:


c()
d()
print(c)
print(d)


# 요구사항 4. Counter 클래스 내에 관련 메소드를 추가하여 인스턴스 객체를 직접 호출(call)할 수 있도록 하시오. 인스턴스 객체를 직접 호출했을 때에 내부적으로 incr() 메소드를 호출하는 방법으로 구현하시오.
# 
# __call__ 함수는 인스턴스가 호출되었을 때 실행이 되는 것으로 클래스 객체도 호출되게 만들어준다.
# 이 함수에서 incr() 함수가 불리도록 구현한다. 

# In[98]:


c.incr()
d.incr()
print(c)
print(d)


# 요구사항 5. 다음과 같은 두 개의 산술 연산 (+, -)이 수행될 수 있도록 Counter 클래스 내에 관련 메소드를 추가하시오.
# 
# __add__ (연산자 : +) : 다른 클래스의 객체의 count값과 이 클래스 객체의 count값을 더한다. 
# 
# __sub__ (연산자 : -) : 다른 클래스의 객체의 count값과 이 클래스 객체의 count값을 뺀다. 

# In[99]:


c = c + 5
d = d - 5
print(c)
print(d)


# 요구사항 6. 다음과 같은 관계연산 (>, <, ==)이 수행될 수 있도록 Counter 클래스 내에 관련 메소드를 추가하시오.
# 
# __gt__ (연산자 : >) : >를 수행하게 될 때, 이 클래스 객체인 count값과 정수의 값을 비교한 후 반환한다. 
# 
# __ge__ (연산자 : >=) : >=를 수행하게 될 때, 이 클래스 객체인 count값과 정수의 값을 비교한 후 반환한다. 
# 
# __lt__ (연산자 : <) : <를 수행하게 될 때, 이 클래스 객체인 count값과 정수의 값을 비교한 후 반환한다. 
# 
# __le__ (연산자 : <=) : <=를 수행하게 될 때, 이 클래스 객체인 count값과 정수의 값을 비교한 후 반환한다. 
# 
# __eq__ (연산자 : ==) : ==를 수행하게 될 때, 이 클래스 객체인 count값과 정수의 값을 비교한 후 반환한다. 
# 
# __ne__ (연산자 : !=) : !=를 수행하게 될 때, 이 클래스 객체인 count값과 정수의 값을 비교한 후 반환한다. 

# In[100]:


print(c > 10)

print(d > 10)

print(c < 10)

print(d < 10)

print(c == 17)

print(d != 9)


# #4번. 다음은 내장 자료형 list를 서브클래싱하여 만든 MySet 클래스 정의 내용이다. 다음 클래스 정의에서 __init__(), __str()__(), elimicate_duplicate()의 세 개의 메소드 코드 내용을 자신이 다른 사람에게 가르친다고 생각하며 설명해보시오.
# 
# MySet은 집합(Set) 자료형을 정의하려는 의도하에 만들어진 클래스이다.

# In[8]:


class MySet(list):
    def __init__(self, l):
        for e in l:
            self.append(e)
        MySet.eliminate_duplicate(self)
    
    def __str__(self):
        result = "MySet: {"
        for e in self:
            result = result + str(e) + " ,"
        result = result[0:len(result)-2] + "}"
        return result
    
    @staticmethod    
    def eliminate_duplicate(l):
        s = []
        for e in l:
            if e not in s:
                s.append(e)
        l[:] = []
        for e in s:
            l.append(e)

    
if __name__ == "__main__":
    s = MySet([1, 2, 2, 3])
    print(s)
    t = MySet([2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 9])
    print(t)


# __init__ : 리스트 I에 있는 요소들을 클래스 객체의 인스턴스에 추가하고 기본값으로 설정한다.
# *elimainate_duplicate* 함수를 사용하여 이 인스턴스의 중복 요소들을 제거한다.
# 
# __str__ : MySet : {}형태로 나타내기 위해 사용하는 함수이다.
# 인스턴스 내에 있는 요소들을 문자열형태로 나타낸다.
# 
# eliminate_duplicate() : 중복 제거를 위한 함수이다.
# 리스트 I에 있는 요소들이 중복되지 않게 새로운 리스트 s에 옯긴다.
# 리스트 I를 초기화한 뒤 다시 리스트 s에 있는 요소들을 리스트 I로 옮긴다.
# 객체로의 접근이 아니어서 self를 사용할 수 없기 때문에, staticmethod로 간주한다.

# #5번. 4번 문제에 정의된 MySet 클래스에 메소드를 추가하여 다음 각 요구사항 모두를 만족시키는 코딩을 제시하시오.

# In[14]:


class MySet(list):
    def __init__(self, l):
        for e in l:
            self.append(e)
        MySet.eliminate_duplicate(self)
    
    def __str__(self):
        result = "MySet: {"
        for e in self:
            result = result + str(e) + ", "
        result = result[0:len(result)-2] + "}"
        return result

    @staticmethod    
    def eliminate_duplicate(l):
        s = []
        for e in l:
            if e not in s:
                s.append(e)
        l[:] = []
        for e in s:
            l.append(e)
    
    def __or__(self, other): # 합집합
        lst = []
        for e in self :
            lst.append(e)
        for i in other :
            if i not in lst :
                lst.append(i)
        return MySet(lst)
    
    def __and__(self, other) : #교집합
        lst = []
        for e in self :
            for i in other :
                if(i == e) : 
                    lst.append(i)       
        return MySet(lst)
    
    def __sub__(self, other) : # 차집합
        lst = []
        for e in self :
            lst.append(e)
        for i in other :
            if i in lst:
                lst.remove(i)
        return MySet(lst)

if __name__ == "__main__":
    s = MySet([1, 2, 2, 3])
    print(s)
    t = MySet([2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 9])
    print(t)


# 요구사항 1. | 연산으로 두 집합의 합집합을 반환한다.
# 
# __or__ (연산자 : |) : 객체의 인스턴스에 있는 요소들을 새로운 리스트 lst에 추가한다. 만일 다른 집합에 있는 요소와 lst에 있는 요소가 중복되지 않으면, 다른 집합에 있는 요소도 추가한다. 

# In[15]:


u = s | t
print(u)


# 요구사항 2. & 연산으로 두 집합의 교집합을 반환한다.
# 
# __and__ (연산자 : &) : 객체의 인스턴스에 있는 요소와 다른 집합의 요소 중 겹치는 요소가 있다면 lst에 추가한다.

# In[16]:


u = s & t
print(u)


# 요구사항 3. - 연산으로 두 집합의 차집합을 반환한다.
# 
# __sub__ (연산자 : -) : 객체의 인스턴스 내에 있는 모든 요소들을 lst에 추가한다.
# 여기서, 다른 집합에 있는 요소와 lst에 있는 요소가 겹칠 시 lst에 중복된 요소들을 제거한다.

# In[17]:


s = MySet([1, 2, 3])
t = MySet([3, 4, 5])
u = s - t
print(u)


# #6번. 5번 문제에서 정의한 MySet 클래스에 대해 다음 예제를 수행하면 오류없이 올바르게 동작하는 것을 확인할 수 있다. 다음 예제 내에 있는 len(), bool() 내장함수와 in 키워드 사용 예제가 별다른 메소드 정의를 하지 않았는 데도 올바르게 수행되는 이유를 설명하시오.

# In[18]:


s = MySet([1, 2, 3, 4, 5, 6])
print(len(s))
print(bool(s)) 
print(2 in s)


# len, bool은 파이썬 내에 존재하는 내장함수이기 때문에 별도로 정의를 하지 않아도 사용할 수 있다.
# 
# in도 마찬가지로 파이썬 내에 있는 연산자이므로 바로 사용가능하다. 

# #발전문제

# 1. Assignment 3 & Assignment 4의 Incremental Project 코드를 다시 확장/변형하여 다음과 같은 조건을 만족하도록 구현하시오 (CODE REFACTORING!!!).

# In[268]:


import requests
import re

class SearchEngine(list) :
    def __init__(self, *args) :
        for i in args :
            self.append(i)

    def addUrl(self, url) :
        self.append(url)
        print(self)
    
    def removeUrl(self, url) :
        for i in self :
            if i == url :
                self.remove(i)
        print(self)
    
    def listUrls(self) :
        for i in self :
            print(i)
     
    def getWordsFrequency(self) :
        if self == None :
            return {}
        
        def Checkblock(link) :
            check = False  
            for i in range(len(link)) :
                if link[i] == '<' :
                    check = True
                    break           
                elif link[i] == '>' :
                    check = True
                    break              
                else :
                    continue          
            return check
        
        def Countblock(link) :    
            count = 0
            num = 0   
            for i in range(0, len(link)) : 
                if link[i] == '<'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != '>'  :
                            count += 1
                            continue
                        elif link[j] == '>' :
                            count += 1
                            break
                    break
                else :
                    continue            
            link = link[ : num] + link[num+count : ]
            return link    
            
        def DeleteHTML(link) :    
            HTML = Countblock(link) 
            while Checkblock(HTML) == True :      
                HTML = Countblock(HTML)       
                continue    
            return HTML
            
        def CheckVar(link) :   
            check = False    
            for i in range(len(link)) :       
                if link[i:i+3] == 'var' :
                    check = True
                    break            
                else :
                    continue            
            return check
            
        def CountVar(link) :    
            count = 0
            num = 0    
            for i in range(0, len(link)) :  
                if link[i:i+3] == 'var'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != ';' :
                            count += 1
                            continue
                        elif link[j] == ';':
                            count += 1
                            break
                    break
                else :
                    continue            
            link = link[ : num] + link[num+count : ]
            return link
            
        def DeleteVar(link) :    
            var_HTML = CountVar(link)    
            while CheckVar(var_HTML) == True :       
                var_HTML = CountVar(var_HTML)        
                continue    
            return var_HTML
            
        def CheckjsMVC(link) :    
            check = False    
            for i in range(len(link)) :        
                if link[i:i+5] == 'jsMVC' :
                    check = True
                    break
                else :
                    continue           
            return check
            
        def CountjsMVC(link) :    
            count = 0
            num = 0    
            for i in range(0, len(link)) :  
                if link[i:i+5] == 'jsMVC'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != ';' :
                            count += 1
                            continue
                        elif link[j] == ';':
                            count += 1
                            break
                    break
                else :
                    continue                
            link = link[ : num] + link[num+count : ]    
            return link
            
        def DeletejsMVC(link) :    
            jsMVC_HTML = CountjsMVC(link)    
            while CheckjsMVC(jsMVC_HTML) == True :       
                jsMVC_HTML = CountjsMVC(jsMVC_HTML)        
                continue   
            return jsMVC_HTML

        def CheckBigblock(link) :    
            check = False    
            for i in range(len(link)) :        
                if link[i] == '{' :
                    check = True
                    break
                else :
                    continue           
            return check
            
        def CountBigblock(link) :    
            count = 0
            num = 0    
            for i in range(0, len(link)) :  
                if link[i] == '{'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != '}'  :
                            count += 1
                            continue
                        elif link[j] == '}' :
                            count += 1
                            break
                    break
                else :
                    continue            
            link = link[ : num] + link[num+count : ]    
            return link   
            
        def DeleteBigHTML(link) :    
            Big_HTML = Countblock(link)    
            while CheckBigblock(Big_HTML) == True :        
                Big_HTML = CountBigblock(Big_HTML)        
                continue    
            return Big_HTML
            
        def CheckWindowblock(link) :   
            check = False    
            for i in range(len(link)) :        
                if link[i:i+6] == 'window' :
                    check = True
                    break
                else :
                    continue            
            return check
            
        def CountWindowblock(link) :    
            count = 0
            num = 0    
            for i in range(0, len(link)) :  
                if link[i:i+6] == 'window'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != ';'  :
                            count += 1
                            continue
                        elif link[j] == ';' :
                            count += 1
                            break
                    break
                else :
                    continue            
            link = link[ : num] + link[num+count : ]    
            return link  
            
        def DeleteWindowHTML(link) :    
            Finally_HTML = CountWindowblock(link)    
            while CheckWindowblock(Finally_HTML) == True :        
                Finally_HTML = CountFinallyblock(Finally_HTML)       
                continue    
            return Finally_HTML

        def checking(list) :   
            dictionary = {}  
            for text in list: 
                if text not in dictionary :
                    dictionary[text] = 1
                else :
                    dictionary[text] += 1        
            return dictionary
        
        sum_dict = {}
        
        for e in self :
            req = requests.get(e)
            source = req.text     
            
            New_HTML = DeleteHTML(source)
            Soon_HTML = DeleteVar(New_HTML)
            Maybe_HTML = DeletejsMVC(Soon_HTML)
            Final_HTML = DeleteBigHTML(Maybe_HTML)
            Finally_HTML = DeleteWindowHTML(Final_HTML)
            result = re.sub('[-=+,#/\?:^$.©@*\"※~&%ㆍ!』\\‘}|\(\)\[}\]\<\>`\'…》]', '', Finally_HTML)  
            result = result.split() 
            checking_result = checking(result)
            sum_dict.update(checking_result)
    
        return sum_dict
    
    def getMaxFreqencyWords(self) :

        a = self.getWordsFrequency()
        
        if a == {} :
            return None 
        
        dict_a = {}
        max = 0
        for j in a.values() :
            if max < j :
                max = j
            else :
                continue
                
        for key, value in a.items():
            if value == max :
                dict_a[key] = value
            else :
                continue
        return dict_a
    
    def searchUrlByWord(self, str) :
        a = self.getWordsFrequency()
        

w1 = SearchEngine('http://www.cnn.com', 'http://www.times.com', 'https://www.amazon.com')
w2 = SearchEngine('http://www.cnn.com', 'http://www.times.com')
w3 = SearchEngine()

w1.addUrl('https://github.com')
w3.addUrl('http://stackoverflow.com')
w1.removeUrl('http://www.cnn.com')
w2.removeUrl('http://stackoverflow.com')
w1.listUrls()
# In[269]:


Example = SearchEngine('http://www.kakao.com', 'http://www.seventeen-17.com/')
Exception = SearchEngine()
print(Exception.getWordsFrequency())
print(Example.getWordsFrequency())


# In[270]:


print(Exception.getMaxFreqencyWords())
print(Example.getMaxFreqencyWords())


# 위 1번 문제에서 정의한 SearchEngine 클래스를 상속하여 SearchEngineWithOrderedWebWords 클래스를 정의하고 슈퍼클래스에 정의된 getWordsFrequency() 메소드를 오버라이드하여 단어 출현 빈도를 내림 차순으로 정렬하여 리스트로 출력하시오.

# In[318]:


class SearchEngineWithOrderedWebWords(SearchEngine) :
    
    def getWordsFrequency(self, reverse = None) :
        
        if reverse == None :
            self.reverse = False
        
        elif reverse == True :
            self.reverse = True
            
        if self == None :
            return {}
        
        def Checkblock(link) :
            check = False  
            for i in range(len(link)) :
                if link[i] == '<' :
                    check = True
                    break           
                elif link[i] == '>' :
                    check = True
                    break              
                else :
                    continue          
            return check
        
        def Countblock(link) :    
            count = 0
            num = 0   
            for i in range(0, len(link)) : 
                if link[i] == '<'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != '>'  :
                            count += 1
                            continue
                        elif link[j] == '>' :
                            count += 1
                            break
                    break
                else :
                    continue            
            link = link[ : num] + link[num+count : ]
            return link    
            
        def DeleteHTML(link) :    
            HTML = Countblock(link) 
            while Checkblock(HTML) == True :      
                HTML = Countblock(HTML)       
                continue    
            return HTML
            
        def CheckVar(link) :   
            check = False    
            for i in range(len(link)) :       
                if link[i:i+3] == 'var' :
                    check = True
                    break            
                else :
                    continue            
            return check
            
        def CountVar(link) :    
            count = 0
            num = 0    
            for i in range(0, len(link)) :  
                if link[i:i+3] == 'var'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != ';' :
                            count += 1
                            continue
                        elif link[j] == ';':
                            count += 1
                            break
                    break
                else :
                    continue            
            link = link[ : num] + link[num+count : ]
            return link
            
        def DeleteVar(link) :    
            var_HTML = CountVar(link)    
            while CheckVar(var_HTML) == True :       
                var_HTML = CountVar(var_HTML)        
                continue    
            return var_HTML
            
        def CheckjsMVC(link) :    
            check = False    
            for i in range(len(link)) :        
                if link[i:i+5] == 'jsMVC' :
                    check = True
                    break
                else :
                    continue           
            return check
            
        def CountjsMVC(link) :    
            count = 0
            num = 0    
            for i in range(0, len(link)) :  
                if link[i:i+5] == 'jsMVC'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != ';' :
                            count += 1
                            continue
                        elif link[j] == ';':
                            count += 1
                            break
                    break
                else :
                    continue                
            link = link[ : num] + link[num+count : ]    
            return link
            
        def DeletejsMVC(link) :    
            jsMVC_HTML = CountjsMVC(link)    
            while CheckjsMVC(jsMVC_HTML) == True :       
                jsMVC_HTML = CountjsMVC(jsMVC_HTML)        
                continue   
            return jsMVC_HTML

        def CheckBigblock(link) :    
            check = False    
            for i in range(len(link)) :        
                if link[i] == '{' :
                    check = True
                    break
                else :
                    continue           
            return check
            
        def CountBigblock(link) :    
            count = 0
            num = 0    
            for i in range(0, len(link)) :  
                if link[i] == '{'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != '}'  :
                            count += 1
                            continue
                        elif link[j] == '}' :
                            count += 1
                            break
                    break
                else :
                    continue            
            link = link[ : num] + link[num+count : ]    
            return link   
            
        def DeleteBigHTML(link) :    
            Big_HTML = Countblock(link)    
            while CheckBigblock(Big_HTML) == True :        
                Big_HTML = CountBigblock(Big_HTML)        
                continue    
            return Big_HTML
            
        def CheckWindowblock(link) :   
            check = False    
            for i in range(len(link)) :        
                if link[i:i+6] == 'window' :
                    check = True
                    break
                else :
                    continue            
            return check
            
        def CountWindowblock(link) :    
            count = 0
            num = 0    
            for i in range(0, len(link)) :  
                if link[i:i+6] == 'window'  :
                    num = i
                    for j in range(i, len(link)) : 
                        if link[j] != ';'  :
                            count += 1
                            continue
                        elif link[j] == ';' :
                            count += 1
                            break
                    break
                else :
                    continue            
            link = link[ : num] + link[num+count : ]    
            return link  
            
        def DeleteWindowHTML(link) :    
            Finally_HTML = CountWindowblock(link)    
            while CheckWindowblock(Finally_HTML) == True :        
                Finally_HTML = CountFinallyblock(Finally_HTML)       
                continue    
            return Finally_HTML

        def checking(list) :   
            dictionary = {}  
            for text in list: 
                if text not in dictionary :
                    dictionary[text] = 1
                else :
                    dictionary[text] += 1        
            return dictionary
        
        sum_dict = {}
        
        for e in self :
            req = requests.get(e)
            source = req.text     
            
            New_HTML = DeleteHTML(source)
            Soon_HTML = DeleteVar(New_HTML)
            Maybe_HTML = DeletejsMVC(Soon_HTML)
            Final_HTML = DeleteBigHTML(Maybe_HTML)
            Finally_HTML = DeleteWindowHTML(Final_HTML)
            result = re.sub('[-=+,#/\?:^$.©@*\"※~&%ㆍ!』\\‘}|\(\)\[}\]\<\>`\'…》]', '', Finally_HTML)  
            result = result.split() 
            checking_result = checking(result)
            sum_dict.update(checking_result)
    
        most_data = []
        for (i, j) in sum_dict.items():
            most_data.append((i,j))
        most_data = sorted(most_data, key=lambda x: x[1], reverse = self.reverse)
        return most_data
    
    def iter_method(self) :
        c = self.getWordsFrequency()
        a = input() 
        b = input()
        if a[0:9] == 'for i in ' :
            return True


# In[319]:


w4 = SearchEngineWithOrderedWebWords('http://www.kakao.com', 'http://www.seventeen-17.com/','https://www.gn.go.kr/' )
print(w4.getWordsFrequency())
print(w4.getWordsFrequency(reverse=True))


# 3. 다음과 같은 코딩이 가능하도록 SearchEngineWithOrderedWebWords안에 반복자와 관련된 메소드를 추가하시오

# In[323]:


w4.iter_method()


# 소감 : 발전문제가 너무 어려웠다. 몇시간을 했지만, 답이 잘 안나온다. 2번문제에서 가장 최대 값이 나오지를 않는데, 그 이유를 잘 모르겠다.
# 그래도 클래스에 적응한 것 같아서 유익했다.
