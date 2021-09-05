while True:
    try:
        a=input()
        a=a.capitalize()
        a=list(a)
        
        boolean=True
        for i in range(len(a)):
               
            if a[i].isalpha():
                if boolean:
                    a[i]=a[i].upper()
                    boolean=False
                else:
                    a[i]=a[i].lower()
                    boolean=True
        
        b=""
        
        print(b.join(a))
    except EOFError:
        break