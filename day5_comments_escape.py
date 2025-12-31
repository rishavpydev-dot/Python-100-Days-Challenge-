#day 5 comments, escape squence ans print statement
#jab hume koi line lekhna ho aur hum ye chahte ho ki wo line raha par hum chahe to usse execute  na ho to hum use karenge comments"#" ka
#'Ram is a good boy' # ke sath jo lekha jaya hain wo sab comments hain
#multiline comment ke liye ''' ya """lagana hoga aur uske bech mai lekh sakte hain kuch bhi wo kisi kaam ka nahi hoga ex:-
'''
ram is a good boy
he plays football
she dances
'''
#note:-multiline '#' koi statement ke baad suru  uss  line ke samne se suru nahi hota ex:-
print("ram") '''
tiger is dangerous
gta5
'''
#syntax error batayega line 11 main
print("Marry is a serious person 
And Marry is also a boy ") 
#yah  incorrect hain kyonki maine enter daba diya kyonki mai chahta tha ki 'And Marry is also a boy ' correct code ye hoga- 
print('Marry is a serious person \nAnd Marry is also a boy') #yah code sahi hain kyonki mai chahta tha 'And Marry is also a boy' ko alag line mai ho to maine backslash\n ka use kiya
#note:- agar \'N' ho  to error aayega
# result=
'''
Marry is a serious person
And Marry is also a boy
'''               
print( "Lord Ram is a great "And" Brave")
#is line mai hum and ko quotes ke andar highlight karna chhate the par ye statement galat hain kyonki maine and se pahle laga diya quote lekin hume pata hain ki quote khatam ho raha hain brave par lekin python confuse hota hain correct statement ye hoga
	
print("Lord Ram is a great \"And\" Brave")#ya
print('Lord Ram is a great \'And\' Brave' )
#ye dono sahi hain kyonki maine backslash ke sath single-quote ya Double-quotes lagaya hain
'''
result=
(1)Lord Ram is a great "And" Brave
(2)Lord Ram is a great 'And' Brave
'''
#backslash \t ka use 
print('name:-\t Rishav')#result=(name:-      Rishav'
#note:- agar \'T' ho  to error aayega

# hum print ke andar multiple value bhi print kar sakte hain ex:-
print('7','8','9')
#sep se join 

print("6", "7", "8", sep="-" )
print("python", "java", "c", sep="/")
print('car', 'bus', 'truck' ,sep=' , ')
#bina commas lagaye python samjh lega ek hi sep kaam nahin karega line  
 
# end parameter 
print("Ram is a good boy",'', end = '009\n')
print("dog") 

"""
 its result 
Ram is a good boy 009
dog

"""
print('ram is a god',end='also')
print('warrior')
#result=ram is a godalsowarrior
