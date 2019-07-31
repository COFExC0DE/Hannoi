import timeit


def Hanoi(n,Fuente,Auxiliar,Destino):
    
    if(n == 1): 

        print (Fuente,"->",Destino)

    else: 

        Hanoi(n-1,Fuente,Destino,Auxiliar) 

        print (Fuente,"->", Destino) 

        Hanoi(n-1,Auxiliar,Fuente,Destino)
        
    

def main():
    
	hola = input("ingrese la cantidad de discos: ")


	start_time = timeit.default_timer()
	
	Hanoi(int(hola),"A","B","C")

	elapsed = timeit.default_timer() - start_time

	print(elapsed)
	
	if __name__ == "__main__":
    		main()
	



