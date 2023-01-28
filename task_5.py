# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, 
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

# Введем следующие события:
# а) Событие A1 - -вышла из строя первая деталь -вероятность этого события P(A1)=0.1;
# б) Событие A_1 - противоположное событию A1 первая деталь не вышла из строя, вероятность этого события: 
# P(A_1) = 1 - P(A1) = 1 - 0.1 = 0.9;
# в) Событие A2 - -вышла из строя первая деталь -вероятность этого события P(A2)=0.2;
# г) Событие A_2 - противоположное событию A1 первая деталь не вышла из строя, вероятность этого события: 
# P(A_2) = 1 - P(A2) = 1 - 0.2 = 0.8;
# д) Событие A3 - -вышла из строя первая деталь -вероятность этого события P(A3)=0.25;
# е) Событие A_3 - противоположное событию A3 первая деталь не вышла из строя, вероятность этого события: 
# P(A_3) = 1 - P(A3) = 1 - 0.25 = 0.75;

# а) Для того, чтобы произошло событие "вышли из строя все детали", необходимо, чтобы одновременно произошли 
# события A1, A2, A3, вероятность P(a) равна
Pa=0.1*0.2*0.25
print(f'а) Вероятность того, что из строя выйдут все детали Р(a) = {Pa: .4f}')
# б) Для того, чтобы произошло событие "вышли из строя 2 детали", необходимо что бы случилось одна из следующих 
# комбинаций событий:
# 1. Произошли события A1, A2, A_3;
# 2. Произошли события A1, A3, A_2;
# 3. Произошли события A2, A3, A_1;
# А вероятностью этого события P(b) будет суммой вероятностей этих комбинаций событий.
# P(b) = P(A1) * P(A2) * P(A_3) + P(A1) * P(A3) * P(A_2) + P(A2) * P(A3) * P(A_1)
Pb=0.1*0.2*0.75+0.1*0.25*0.8+0.2*0.25*0.9
print(f'б) Вероятность того, что из строя выйдут только 2 детали Р(b) = {Pb: .4f}')

# в) Событие "выйдет из строя хотя бы одна деталь" 
# можно рассмотреть как противоположное событию "не вышло из строя ни одной детали".
# Пусть P(c) вероятность события "не вышло из строя ни одной детали". 
# Данное событие может произойти при одновременном наступлении событий A_1, A_2, A_3
# P(c) = P(A_1) * P(A_2) * P(A_3)
Pc=0.9*0.8*0.75
print(f'в) Вероятность того, что из строя не выйдет ни одной детали Р(c) = {Pc: .4f}')

# г) Событие "из строя выйдут от одной до двух деталей" произойдет при наступлении события 
# "из строя выйдет одна деталь" или из строя выйдут 2 детали, следовательно его вероятность 
# будет равна сумме вероятностей этих событий: 
# P(a,b) = P(d) + P(b)
# P(b) = 0.08, P(d) = 
Pd=0.1*0.8*0.75+0.2*0.9*0.75+0.25*0.9*0.8
print(f'Вероятность того, что выйдет из строя одна деталь Р(d) = {Pd: .4f}')
