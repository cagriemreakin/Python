import sys
f = open("dosya.txt", "w")
sys.stdout,f = f,sys.stdout # changes the standard output location 

print("deneme metni", flush=True)
f,sys.stdout = sys.stdout,f # resets the output location to its original
print 'deneme'
