class Solution:
    def isValid(self, s: str) -> bool:

        s = s.replace(' ', '')
        par1 = '{}'
        par2 = "[]"
        par3 = "()"

        teste = ''

        for car in s:
            teste += car
            if par3 in teste:
                teste = teste.replace(par3,'')
            if par2 in teste:
                teste = teste.replace(par2, '')
            if par1 in teste:
                teste = teste.replace(par1, '')

        if len(teste) == 0:
            return True
        else:
            return False
            
            
#########################################################  
              ### Variação com listas ###
#########################################################
   
   class Solution:
    def isValid(self, s: str) -> bool:

        s = s.replace(' ', '')
        lis = ['{}', "[]", "()"]
        for car in s:
            if lis[0] in s:
                s = s.replace(lis[0],'')
            elif lis[1] in s:
                s = s.replace(lis[1], '')
            elif lis[2] in s:
                s = s.replace(lis[2], '')
        if len(s) == 0:
            return True
        else:
            return False
