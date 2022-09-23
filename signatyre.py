import requests
#virus_signature = []
#dict_virus_signature = {}
#virus_signature_2 = []
#virus_signature_3 = []
#virus_name = ['virus_1','virus_2','virus_3','virus_4']
#a = 0
#b = ""
def test():
    print ("hi")
def create_signature():
    virus_signature = []
    dict_virus_signature = {}
    virus_signature_2 = []
    virus_signature_3 = []
    virus_name = ['virus_1',"virus_2","virus_3","virus_4"]
    a = 0
    b = ""
    c = ""
    path = 'https://rawcdn.githack.com/RockInMyHead/virus_signature_23_09_2022/e8b78abb338c3ff76d0476333abaaaf17a3e386c/virus_signature.txt'
    response = requests.get(path)
    words = response.text
#with open (path,'r') as f1:
#    words = f1.read()
    words = words.replace("'","")
    #print (words)
    for item in words:
        #print (item)
        b += item
        if (item ==','):
            b = b.replace(",","")
            virus_signature_2.append(b)
            b = ''
    for items in virus_signature_2:
        #print (items)
        if (items == "|||"):
            #dict_virus_signature = {str(virus_signature_3):virus_name[1]}
            #dict_virus_signature = dict.fromkeys([str(virus_signature_3)],virus_name[0])
            c = virus_name[0]
            dict_virus_signature = dict.fromkeys([c],[virus_signature_3])
            del virus_name[0]
            virus_signature.append(dict_virus_signature)
            virus_signature_3 = []
        else:
            virus_signature_3.append(items)
    return virus_signature
c = create_signature()
#print (c)
#print (virus_signature)
#print (a)
#print (dict_virus_signature) 