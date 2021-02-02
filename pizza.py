def main():
    file_object= open("a_example.in","r+")
    li_new=[]
    c=0
    for i in file_object:
        if c==0:
            # print(i)
            li = list(i.split(" ")) 
            li = li[0:4]
            # list(map(lambda x:x.strip(),li))
            li_new.append(li)
            c=c+1
        else:
            li = list(i.split(" ")) 
            #li = li.remove(5)
            final_list = []
            for i in li:
                final_list.append(i.strip())
            # list(map(str.strip,li))
            li_new.append(final_list)
            c=c+1
    return li_new

if __name__=='__main__':
    a=main()
    print(a)