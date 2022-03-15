class Main:
    def lcs(self,s1,s2):
        n1,n2=len(s1),len(s2)
        if n1<n2:s1,s2=s2,s1
        for i in range(n2,-1,-1):
            for j in range(n2):
                if i+j>n1:break
                if s1[j:i+j] in s2:print(s1[j:i+j]);return i                
    
if __name__=='__main__':
    obj=Main()
    print(obj.lcs(input('Enter string-1: '),input('Enter string-2: ')))
