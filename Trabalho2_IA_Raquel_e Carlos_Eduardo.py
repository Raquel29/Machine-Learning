"""
Trabalho 2 - Regressao Linear
Instituto Federal de Brasília
Alunos: Raquel Pinheiro da Costa, Carlos Eduardo Pereira Santana
Compilado com python 3.6
"""
import csv #Utilizado para a leitura do arquivo
import random as rand #Utilizado para gerar um vetor de numeros aleatorios
import numpy as np  #Utilizados para realizar os calculos matriciais 

#Calcula função Custo
def Function_Cust (X,y,theta):
	J = 0
	m = len(y);
	J = J + sum(pow((np.dot(X,theta).shape-y),2)/(2*m))
#Calcula Gradiente Descendente
def Gradiete_Descedente(X,y,thetaI,alpha,inter):

	J_iter = np.zeros((inter,1)) #cria uma função para armazenar os valores da funçao custo
	theta = thetaI
	m = len(y) #m é o tamanho do vetor 

	for i in range(inter):
		temp1 = theta[0] -(alpha/m)*sum((np.dot(X,theta) - y))
		temp2 = theta[1] -(alpha/m)*sum((np.dot(X,theta) - y)*X[:,1])
		temp3 = theta[2] -(alpha/m)*sum((np.dot(X,theta) - y)*X[:,2])
		theta[0] = temp1
		theta[1] = temp2
		theta[2] = temp3
		J_iter[i] = Function_Cust(X,y,theta)

def main():
	L1 = []
	L2 = []
	y = []
	thet = []
	x0 = []
	
	#Faz leitura do arquivo e coloca os valores dentro da matriz e do vetor 
	with open ('data.csv') as csvfile:
		leitor_csv = csv.reader(csvfile, delimiter = ",")
		for linha in leitor_csv:
			L1.append(int(linha[1]))
			L2.append(int(linha[2]))
			y.append(int(linha[3]))
	#Preenche o vetor x0 com uns, e atribui valores aleatorios para o vetor theta
	for i in range(len(L1)):
		x0.append(1)
	for j in range(3):
		thet.append(rand.randint(1,100))

	X = np.array((x0,L1,L2)) #Converte de lista para array
	X = X.T        #Coloca X transposta em X
	y = np.array(y) #Converte de lista para array
	x0 = np.array(x0) #Converte de lista para array
	theta = np.array(thet) #Converte de lista para array
	Gradiete_Descedente(X,y,theta,0.00000001,2010) #Chama a funçao Gradiente		
	h = theta[0]+(theta[1]*28)+(theta[2]*25) #Hipotese
	print(h)

#Faz com que o programa entenda qual e p modulo principal
if __name__ == '__main__':
	main()