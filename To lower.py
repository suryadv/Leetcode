def toLowerCase(self, str):

    alpha = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i',
         'J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s',
         'T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z' }

    z1 = list(str)
    for i in range(len(str)):
        if str[i] in alpha:
            z1[i] = alpha[str[i]]
    return ''.join(z1)



