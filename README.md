# Primeiro Trabalho de IA - Buscas
&nbsp;&nbsp;&nbsp;Implementação de alguns algoritmos de busca genéricos, e aplicação para problemas especificados.

&nbsp;&nbsp;&nbsp;Feito para a disciplina de Inteligência Artificial (GBC063) pelos alunos:
<div>
	<p align="center">
		Bruno Sinhoroto - 
		<a href="https://github.com/">(GitHub)</a>
	</p>
	<p align="center">
		Lucas Pellegrini - 
		<a href="https://github.com/LucasGPellegrini">(GitHub)</a>
	</p>
	<p align="center">
		Silvano Junior - 
		<a href="https://github.com/">(GitHub)</a>
	</p>
</div>

&nbsp;&nbsp;&nbsp;UFU - Universidade Federal de Uberlândia;

&nbsp;&nbsp;&nbsp;FACOM - Faculdade de Computação;

## Dos problemas trabalhados:
### Problema 01: Quebra cabeça das 2N Fichas
- N fichas brancas + N fichas pretas.
	- Dispostas em uma lista com $\tt{2N+1}$ posições;
- **Início**: fichas brancas e pretas separadas pela posição vazia ao centro.
- **Meta**: dispor todas as fichas brancas no meio das pretas, ou vice-versa, de modo que a posição vazia fique na casa mais à esquerda ou mais à direita.
- **Ação**: fichas podem pular ou deslizar para a posição vazia quando a posição vazia estiver distante de no máximo N casas da posição da ficha.
	- **Custo**: distância entre a ficha movimentada e a posição vazia;
	- **Heurística adotada:** é dada pela soma entre:
		- a quantidade de fichas brancas isoladas por fichas pretas;
		- a quantidade de fichas pretas isoladas por fichas brancas;
		- a menor distancia entre a posicao vazia e um dos extremos;

### Problema 02: Escalonamento de Tarefas

## Dos algoritmos de busca implementados:
- Foram implementados os algoritmos genéricos de busca:
	- Busca de Profundidade Iterativa ($\tt{BPI.py}$);
	- Busca de Menor Custo ($\tt{BMC.py}$);
	- Busca A Estrela ($\tt{ASTR.py}$);
	- Subida de Encosta com Movimentos Laterais ($\tt{HCML.py}$);%    
