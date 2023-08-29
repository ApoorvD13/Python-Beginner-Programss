class Solution:
    def romanToInt(self):
        counti=0
        countv=0
        countx=0
        countl=0
        countc=0
        countd=0
        countm=0
        r=input("Ente Roman: ")
        r1=r.lower()
        for i in r1:
            if(i=='i'):
                counti+=1
            elif(i=='v'):
                countv+=1
            elif(i=='x'):
                countx+=1
            elif(i=='l'):
                countl+=1
            elif(i=='c'):
                countc+=1
            elif(i=='d'):
                countd+=1
            elif(i=='m'):
                countm+=1
        n=counti+countv*5+countx*10+countl*50+countc*100+countd*500+countm*1000
        print(n)

obj=Solution()
obj.romanToInt()

