
   a = driver.non_married("MATCH (p: Person) WHERE p.marraige = False RETURN p.name AS name, p.born AS born, p.died AS died, p.place AS place, p.marraige AS marraige, p.parents AS parents, ID(p) AS id")

    b = driver.married("MATCH (p: Person) WHERE p.marraige = True RETURN p.name AS name, p.born AS born, p.died AS died, p.place AS place, p.marraige AS marraige, p.parents AS parents, p.marriedTo AS marriedTo, ID(p) AS id")

    comb = a + b
    # fixedArr = []
    # for i in range(len(comb)):
    #     arr = comb[i]

    #     #Parents
    #     if (arr[5] == None):
    #         #Married
    #         if (arr[4] == True):
                
    #             #Death
    #             if (arr[2] == None):
                    
    #                 #These people Do not have parents, are married and are not dead
    #                 pass
    #             else:

    #                 #These people Do not have parents, are married and are dead
    #                 fixedArr.append({"id": arr[7], "pids": arr[6], "Name": arr[0], "Born": arr[1], "Died": arr[2], "Place": arr[3], "Married": arr[4]})
    #         else:

    #             #Death
    #             if (arr[2] == None):
                    
    #                 #These people Do not have parents, are not married and are not dead
    #                 pass
    #             else:

    #                 #These people Do not have parents, are not married and are dead
    #                 pass

    #     else:

    #         #Married
    #         if (arr[4] == True):
                
    #             #Death
    #             if (arr[2] == None):
                    
    #                 #These people have parents, are married and are not dead

    #                 fixedArr.append({"id": arr[7], })
    #             else:

    #                 #These people have parents, are married and are dead
    #                 pass
    #         else:

    #             #Death
    #             if (arr[2] == None):
                    
    #                 #These people have parents, are not married and are not dead
    #                 pass
    #             else:

    #                 #These people have parents, are not married and are dead
    #                 pass


    return comb