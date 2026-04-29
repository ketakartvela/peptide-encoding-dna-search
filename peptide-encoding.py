with open(r"peptide_encoding.txt","r") as f:
    lines=f.read().strip().split()
    amino=lines[1]
    string=lines[0]
    

def reverse_compliment(string):
    comp={"T":"A","G":"C","C":"G","A":"T"}
    rev=[]
    for i in string[::-1]:
        rev.append(comp[i])
    a="".join(rev)
    return a
        
def translate(text,graph):
    aa=[]
    for i in range(0,len(text),3):
        txt=text[i:i+3]
        codon=txt.replace('T','U')
        aa.append(graph[codon])
    return "".join(aa)
def dna(string,graph,amino):
    a=len(amino)
    k=3*a
    result=[]
    for i in range(len(string)-k+1):
        text=string[i:i+k]
        x=translate(text, graph)
        if x==amino:
            result.append(text)
    rc=reverse_compliment(string)
    for j in range(len(rc)-k+1):
        txt=rc[j:j+k]
        y=translate(txt,graph)
        if y==amino:
            key=reverse_compliment(txt)
            result.append(key)
    return " ".join(result)
            
        

            
       
    
    
        
            
            
            
    
    
    
    
    
   

graph={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
y=dna(string,graph, amino)
print(y)
