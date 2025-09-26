# 1° Trabalho APCII

Este é um projeto desenvolvido para a disciplina de **Algoritmos e Programação de Computadores (APC II)** da Univille, que simula um sistema de gerenciamento de informações. O objetivo é aplicar e integrar diversos conceitos fundamentais da programação em Python.

**Tema Escolhido**: Estacionamento

## Classe Veiculo
| Propriedade | Tipo   | Descrição                        | Visibilidade       |
|-------------|--------|----------------------------------|--------------------|
| placa       | String | Chave primaria do veículo		  |  Private           |
| modelo      | String | Modelo  do veículo		          |  Private           |
| cor         | String | Cor do veículo		              |  Private           |
| proprietario| String | Proprietário do veículo		  |  Private           |

### Subclasse Carro
| Propriedade | Tipo   | Descrição                        | Visibilidade       |
|-------------|--------|----------------------------------|--------------------|
| portas      | String | Quantidade de portas do carro	  |  Private           |

### Subclasse Moto
| Propriedade | Tipo   | Descrição                        | Visibilidade       |
|-------------|--------|----------------------------------|--------------------|
| Definir     |        | 	                              |                    | 

## Classe Vaga
| Propriedade  | Tipo    | Descrição                                             | Visibilidade       |
|--------------|---------|-------------------------------------------------------|--------------------|
| id           | String  | Identificador primario da vaga		                 |  Private           |
| tipo         | String  | Tipo da vaga (C - Carro / M - Moto)		             |  Private           |
| status       | Boolean | Status da vaga (True - Disponivel / False - Ocupada)  |  Private           |
| placaVeiculo | String  | Identificador estrangeiro do veículo que está na vaga |  Private           |

## Equipe

* Andrey Rebelatto
* Erick Anderson
* Eduardo Will
