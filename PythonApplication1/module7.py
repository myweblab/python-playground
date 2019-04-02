import pickle

dictl = {'a':100,
         'b':200,
         'c':300}

listl = [400,'C',"text"]

output = open("smy.pkl","wb")

pickle.dump(dictl,output)
pickle.dump(listl,output)
output.close()

input = open("smy.pkl","rb")
dictl = pickle.load(input)
listl = pickle.load(input)

input.close()

print(dictl)
print(listl)