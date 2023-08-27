#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

float somar(float a, float b);
float subtrair(float a, float b);
float dividir(float a, float b);
float multiplicar(float a, float b);

float num1, num2, atual, resultado;
char operador, pergunta;
bool continuar = true;

int main(){
    printf("Bem vindo a Calculadora do Gabriel Dalposso\n");
// Faz a primeira operacao
    printf("Qual operacao voce deseja fazer?\n(+)Somar\n(-)Subtrair\n(*)Multiplicar\n(/)Dividir\n");
    scanf(" %c", &operador);
// Guarda o Primeiro numero
    printf("Digite o 1 valor: ");
    scanf(" %f", &num1);
// Guarda o Segundo numero
    printf("Digite o 2 valor: ");
    scanf(" %f", &num2);
// Faz a soma
    if(operador == '+'){
        atual = somar(num1, num2);
    }
// Faz a subracao
    if(operador == '-'){
        atual = subtrair(num1, num2);
    }
// Faz a multiplicacao
    if(operador == '*'){
        atual = multiplicar(num1, num2);
    }
// Faz a soma
    if(operador == '/'){
        atual = dividir(num1, num2);
    }

//  Mostra o Resultado
    printf("O resultado foi: %.2f\n", atual);

// Contuniua o Calculo
    do{
        printf("Voce deseja continuar?\ns = sim\nn = n\n");
        scanf(" %c", &pergunta);
            if(pergunta == 's'){
                continuar = true;
            }
            if(pergunta == 'n'){
                continuar = false;
            }
        if(pergunta == 's'){
            printf("Qual operacao deseja fazer agora? ");
            scanf(" %c", &operador);
        // Faz a soma

            if(operador == '+'){
            printf("Digite o valor que deseja somar: ");
            scanf(" %f", &num2);
                atual = somar(atual, num2);
            }
        // Faz a subracao
            if(operador == '-'){
            printf("Digite o valor que deseja subtrair: ");
            scanf(" %f", &num2);
                atual = subtrair(atual, num2);
            }
        // Faz a multiplicacao
            if(operador == '*'){
            printf("Digite o valor que deseja multiplicar: ");
            scanf(" %f", &num2);
                atual = multiplicar(atual, num2);
            }
        // Faz a soma
            if(operador == '/'){
            printf("Digite o valor pelo qual deseja dividir: ");
            scanf(" %f", &num2);
                atual = dividir(atual, num2);
            }
        }
    }while(continuar == true);

    // Printa o Resultado final
    printf("O resultado foi: %f", atual);





}

float somar(float a, float b){
    return a + b;
}
float subtrair(float a, float b){
    return a - b;
}
float multiplicar(float a, float b){
    return a * b;
}
float dividir(float a, float b){
    return a / b;
}