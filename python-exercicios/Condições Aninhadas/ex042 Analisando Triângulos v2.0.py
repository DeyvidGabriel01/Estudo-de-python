print(f"{' ANALISANDO TRIÂNGULOS ':=^42}")
primeiro_segmento = float(input("Digite a primeiro segmento: "))
segundo_segmento = float(input("Digite a segundo segmento: "))
Terceiro_segmento = float(input("Digite a terceiro segmento: "))
print("="*42)
if primeiro_segmento < segundo_segmento + Terceiro_segmento and segundo_segmento < primeiro_segmento + Terceiro_segmento and Terceiro_segmento < primeiro_segmento + segundo_segmento:
    print("Os segmentos acima PODEM FORMA UM TRIÂNGULO.")
    if primeiro_segmento == segundo_segmento == Terceiro_segmento:
        print("O triângulo acima é um TRIÂNGULO EQUILÁTERO.")
    elif primeiro_segmento != segundo_segmento != Terceiro_segmento != primeiro_segmento:
        print("O triângulo acima é um TRIÂNGULO ESCALENO.")
    else:
        print("O triângulo acima é um TRIÂNGULO ISÓSCELES.")
else:
    print("Os segmentos acima NÃO PODEM FORMA UM TRIÂNGULO!")
print("="*42)
