def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

def checksubs(x):
    l1 = len(x)
    for i in range(l1+1):
        print(i)


in1  = input()
subs = get_all_substrings(in1)
print(subs)
k = checksubs(subs)
print(k)
