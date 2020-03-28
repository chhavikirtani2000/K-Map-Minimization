# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Chhavi Kirtani
# Roll Number: 2018229
# Section: B
# Group: 6
# Date: 16-10-2018(DATE OF SUBMISSION)
import copy
def minFunc(numVar, stringIn):
	
    '''converting the input string into lists so that it could be processed '''    
    stringIn=stringIn.replace(" ","")
    stringIn=stringIn.replace("(","")
    stringIn=stringIn.replace(")","")
    
    k=stringIn.find("d")
    
    ones=stringIn[0:k]
    dont_care=stringIn[k+1:]
    
    s=ones.split(",")
    t=dont_care.split(",")
        
        
    

    '''converting the string type list into int type list'''    
    for i in range(len(s)):
           if s[i]!='':
              s[i]=int(s[i])
    for i in range(len(t)):
           if t[i]!='-':
              t[i]=int(t[i])     

    '''computing final list which would be used in step one of matching, considering the cases where 1.dont cares aren't specified 2.minterms aren't specified 3.both are specified'''
    '''or else the process of converting into binary form will create an error'''

    if t[0]=='-':
        final=s
    elif s[0]=='':
        final=t
    elif s[0]=='' and t[0]=='-':
        final=[]
    else:
        final=s+t

    
        
    minterms=copy.deepcopy(s)#copy of s created for future reference in the step in which we need to make prime implicant chart to find out essential prime implicant
    minterms2=copy.deepcopy(s)#copy of s created for future reference in the last step where if no minterms are provided, output should be '0'
    
        
    mylist=[]#stores the binary values of the minterms
        
    '''computing the binary form of the minterms entered by the user'''
    if numVar==4:    
    
        for i in range(len(final)):
          
              st=""
              if final[i]==0:
                  st="0000"    

              while final[i]//2!=0:
                    st=str(final[i]%2)+st
                    final[i]=final[i]//2

              if final[i]!=0:
                 st="1"+st
                      
                      
              
              while len(st)!=4:
                    st="0"+st 
              mylist.append(st)
    

    elif numVar==3:
        for i in range(len(final)):
          
              st=""
              if final[i]==0:
                  st="000"    

              while final[i]//2!=0:
                    st=str(final[i]%2)+st
                    final[i]=final[i]//2

              if final[i]!=0:
                 st="1"+st
                      
                      
              
              while len(st)!=3:
                    st="0"+st 
              mylist.append(st)  

    
    elif numVar==2:
        for i in range(len(final)):
          
              st=""
              if final[i]==0:
                  st="00"    

              while final[i]//2!=0:
                    st=str(final[i]%2)+st
                    final[i]=final[i]//2

              if final[i]!=0:
                 st="1"+st
                      
                      
              
              while len(st)!=2:
                    st="0"+st 
              mylist.append(st)  
      
    elif numVar==1:
        for i in range(len(final)):
          
              st=""
              if final[i]==0:
                  st="0"    

              while final[i]//2!=0:
                    st=str(final[i]%2)+st
                    final[i]=final[i]//2

              if final[i]!=0:
                 st="1"+st
                      
                      
              
              while len(st)!=1:
                    st="0"+st 
              mylist.append(st)  

   
                  
    g0=[]
    g1=[]
    g2=[]
    g3=[]
    g4=[]
    '''divivding minterms into groups based on number of ones'''    
    for i in range(len(mylist)):
          count=0
          for x in mylist[i]:
                if x=="1":
                   count=count+1
          if count==0:
             g0.append(mylist[i])
          elif count==1:
                g1.append(mylist[i])
          elif count==2:
                g2.append(mylist[i])
          elif count==3:
                g3.append(mylist[i])
          elif count==4:
                g4.append(mylist[i])

    g=[g0,g1,g2,g3,g4]
    
    

    mint=[]#stores the decimal equivalent of the binary numbers in g(already grouped according to number of ones)
    for i in range(len(g)):
            mint.append([])
            

    for i in range(len(g)):
            for j in range(len(g[i])):
                    s=g[i][j]
                    n=len(s)
                    sum_dec=0
                    for k in range(n):
                            sum_dec=int(s[k])*(2**(n-1-k))+sum_dec
                    mint[i].append(sum_dec)
                  
                            
    mark=[]#will contain the minterms which have been matched
     





    h=copy.deepcopy(g)
    d=copy.deepcopy(g)
    d.append([0])
    
    p=copy.deepcopy(d)#p is anything different from g!
    

    store=[]#list which keeps on storing binary forms in each and every step
    store_min=[]#list which keeps on storing minterms of the corresponding elements in store
    
    '''converting elements of mint list into string form(or else it would create problem afterwards)'''
    for i in range(len(mint)):
        for j in range(len(mint[i])):
            mint[i][j]=str(mint[i][j])
            
            

      
    
    while p!=g:#point where we need to stop further matching as there is no matching afterwards
          
          p=copy.deepcopy(g)#setting p as the old g so that the g coming out of the following loop when compared with p(which was the old g) if is not equal then only we will proceed
          m=copy.deepcopy(mint) 
          fl=[]
          st=copy.deepcopy(g)
          st_min=copy.deepcopy(mint) 
          store.append(st)
          store_min.append(st_min)
          
          for i in range(len(g)):
                 fl.append([])
                 
                                
          stop=0
          '''following is the process of matching'''
          for i in range(len(g)-1):
                 f=[] 
                  
                 
                 for k in range(len(g[i])):
                                      
                        for j in range(len(g[i+1])):
                                count=0

                                for t in range(len(g[i][k])):
                                        
                                        
                                                   
                                        if g[i][k][t]!=g[i+1][j][t]:
                                                count=count+1
                                                un_score=t
                                                
                                                matched1=g[i][k]
                                                matched2=g[i+1][j]
                                        
                                             
                                             
                                             
                                if count==1:
                                     
                                     
                                     l=str(mint[i][k])+","+str(mint[i+1][j])  
                                     fl[i].append(l) 
                                     f.append(g[i][k][0:un_score]+"_"+g[i][k][un_score+1:])
                                     '''for the purpose of including previously unmatched terms'''
                                     mark.append(matched1)
                                     mark.append(matched2)

                 
                 g[i]=copy.deepcopy(f)
                 mint[i]=copy.deepcopy(fl[i]) 
                 if len(f)==0:#the case where there is no further matching and we need to stop
                         stop=stop+1
                         
          if stop==(len(g)-1):#the case in which there is no further matching and we retain the previous g and mint
                  g=copy.deepcopy(p)
                  mint=copy.deepcopy(m)
                  
          w=g[0:len(g)-1]#removing the last element from the list as there is no need to carry it forward to the next step
          g=copy.deepcopy(w)
          

                
    
    '''matching is accomplished correctly'''
    
    
    unmarked=[]#stores the unmarked(finally we need to work with this only)
    unmarked_min=[]#stores the minterms of unticked or unmarked(finally we need to work with these only) 
    
        
        
        

    
    '''noting the unmarked terms from each step'''
    for j in range(len(store)):
           for k in range(len(store[j])):
                   for i in range(len(store[j][k])):
                          if store[j][k][i] not in mark:
                               unmarked.append(store[j][k][i])
                               unmarked_min.append(store_min[j][k][i]) 
                               
                               
                                    
                            
    
    
    unm_min=[] #contains the unticked minterms in list of list form 
    for i in range(len(unmarked_min)):
            l=unmarked_min[i].split(",")
            t=copy.deepcopy(l)
            unm_min.append(t)

    for i in range(len(unm_min)):#converting unticked minterms from string to int
            unm_min[i]=list(map(int,unm_min[i]))

    dic_prime={}        
    for i in range(len(unm_min)):
            dic_prime[unmarked[i]]=unm_min[i]
    

      
            

    
            

    for i in range(len(unm_min)):
            unm_min[i].sort()#sorting each element of the list unm_min so that the duplicate terms can be removed
            
    dic_prime={} #contains the binary form of the unticked minterms along with the corresponding minterms as values       
    for i in range(len(unm_min)):
            dic_prime[unmarked[i]]=unm_min[i]
            
            
    '''the list containing the lists storing the minterms of the unticked terms: unm_min'''         
             
            
            
    
    final_unm_list=[]
    for x in unm_min:
            if x not in final_unm_list:
                    final_unm_list.append(x)

    unm_min=copy.deepcopy(final_unm_list)#removed the duplicate minterms from unm_min                
                           
                            
    
    ls_s=[]#will contain the minterms which are matched with only one row in the last step of McCluskey theorem
    
    
    for i in range(len(minterms)):#minterms is a list of minterms as given by the user as input(defined at the starting of the code)
            count=0
            for j in range(len(unm_min)):
                    if minterms[i] in unm_min[j]:
                            count=count+1
            if count==1:
                    ls_s.append(minterms[i])

                   
    ess_prime=[] #will contain the minterms(which will form variable exp) corresponding to the terms from unm_min which are not reduntant
    
    for i in range(len(ls_s)):
            for j in range(len(unm_min)):
                    if ls_s[i] in unm_min[j]:
                            ess_prime.append(unm_min[j])
                            
    noted=[]#contains the minterms(columns) which are covered by essential primes and dont need any other prime implicant to cover them
    
    for i in range(len(minterms)):
            for j in range(len(ess_prime)):
                  if minterms[i] in ess_prime[j]:
                        noted.append(minterms[i])
                        break#once we get a row which contains the given minterm in a column, we will exit the loop with variable j
                    
                    
    
    not_matched=[]#will contain those minterms(columns) which are not ticked
    for i in range(len(minterms)):
            if minterms[i] not in noted:
                    not_matched.append(minterms[i])
                    

    leftout=[] #will contain a list of lists where each list is a collection of those minterms(rows) which can be used to cover the columns unticked
    
    for i in range(len(not_matched)):
            min_matched=[]
            for j in range(len(unm_min)):
                    if not_matched[i] in unm_min[j]:
                            min_matched.append(unm_min[j])
                            
            leftout.append(min_matched)
            
    ''' evaluating the prime implicants needed to be added along essential prime impicants to cover all 1's'''       
           

    for i in range(len(leftout)):#loop to remove all terms from leftout which can be covered by another term in leftout
          for j in range(len(leftout[i])):
                for k in range(i+1,len(leftout)):
                      if leftout[i][j] in leftout[k]:
                         leftout.remove(leftout[k])
    
    binary=[]#stores the binary format of the final essential primes
    
    
    
    temp=[]
    
    fs=list(dic_prime.keys())#list containing the keys of the dictionary (keys means the binary format)
    
    
    for j in range(len(leftout)):
          temp.append([])
          for i in range(len(fs)):
               if dic_prime[fs[i]] in leftout[j]:
                   temp[j].append(fs[i])
                   break
                   
            

    
    
                
    for i in range(len(temp)):#noting the prime implicants needed to cover some extra 1's
         if len(temp[i])>0:
             small=temp[i][0]
             for j in range(len(temp[i])):
                   if temp[i][j]<small:
                      small=temp[i][j]
             temp[i]=small

    

    for i in range(len(temp)):#adding those prime implicants into the list containing the final essential primes
        binary.append(temp[i])

         
            
    exp=list(dic_prime.keys())                        
    for i in range(len(exp)):
            if dic_prime[exp[i]] in ess_prime:
                    binary.append(exp[i])#adding the essential primes as computed from the prime implicant chart
                    
    
    str_list=[]#will contain the final list of terms which will form the expression (in variables form)
    
    for i in range(len(binary)):#evaluating the variable form
            string=''
            for j in range(len(binary[i])):#variable will be complemented
                    if binary[i][j]=='0':
                            if j==0:
                                string=string+"A'"
                            elif j==1:
                                     string=string+"B'"
                            elif j==2:
                                     string=string+"C'"
                            elif j==3:
                                     string=string+"D'"

                                     
                    elif binary[i][j]=='1':#variable will not be complemented
                            if j==0:
                               string=string+"A"
                            elif j==1:
                                     string=string+"B"
                            elif j==2:
                                     string=string+"C"
                            elif j==3:
                                     string=string+"D"
                                     
            str_list.append(string)
            
                            
                            
    
    
    stringOut=''#will store the final answer
    
    
    str_list.sort()#for obtaining in lexicographic order
    for i in range(len(str_list)):
          stringOut=stringOut+"+"+str_list[i]
          
    stringOut=stringOut[1:]#final after removing the starting'+'

    if stringOut=='' and minterms2[0]!='':#case in which every variable is reduced and the final output is 1
        return '1'
    elif minterms2[0]=='':#the case in which no minterms are specified and the final answer is 0
         return '0'
    else:
        return stringOut#case otherwise
    
    
    
#if __name__=="__main__":
         #print(minFunc(,"() d()"))
         
         
            
            
         


            
                    
                    
                    
                                    

            
                                    
                                    
            
                            
                    
            









            

            
            
                    
        
                                    
                                    
                            
                            
                            
                                            
                                
                                    
                                    

            
            
            
                                                                                                                                                                                                                                         
                                                     
                                                     
                       
                       
                         
                     
	

	
