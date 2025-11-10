#Calculadora de dos números
print("Hola! Soy una calculadora de dos números ^^")
x=int(input("Proporciona un número: "))
y=int(input("Proporciona otro número: "))
print(f"la suma de {x} + {y} es: {x + y}")
print(f"la resta de {x} - {y} es: {x - y}")
print(f"la multiplicación de {x} * {y} es:  {x * y}")
print(f"la división de {x} / {y} es:  {x / y}")
print(f"el módulo de {x} % {y} es:  {x % y}")
print(f"el exponente de {x} ** {y} es:  {x ** y}")
#Asignaciónes y operaciones de booleano
a=int(input("\nDame otro número (a): "))
b=int(input("Dame otro número más (b): "))
a+=2
print("\nAsignación suma de a +=5 es: ", a)
b-=13
print("Asignación resta de b -=5 es: ", b - 13)
print("¿a es igual a b?", a == b)
print("¿a es diferente de b?", a != b)
print("¿a es mayor que b?", a > b)
print("¿a es menor que b?", a < b)
#tablas de verdad 
print("\nTablas de verdad")
p = True
q = False
print("\nTabla de verdad AND")
print("AND (0,0): ", q and q)
print("AND (0,1): ", q and p)
print("AND (1,0): ", p and q)
print("AND (1,1): ", p and p)

print("\nTabla de verdad OR")
print("AND (0,0): ", q or q)
print("AND (0,1): ", q or p)
print("AND (1,0): ", p or q)
print("AND (1,1): ", p or p)

print("\n Tabla de verdad NOT")
print("AND (0): ", not p);
print("AND (1): ", not q);

print("\nMuchas gracias por ejecutar ^^ \nBy Alex1217z")