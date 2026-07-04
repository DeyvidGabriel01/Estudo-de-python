from math import sin, cos, tan, radians
angulo = float(input("Digite o ângulo que você deseja: "))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)
print(f'O ângulo de {angulo:.1f} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo:.1f} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo:.1f} tem a TANGENTE de {tangente:.2f}')
