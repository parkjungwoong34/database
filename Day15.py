def find_and_insert_data(friend,k_count) :
    findPos = -1
    for i in range(len(pokemons)):
        pair = pokemons[i]
        if k_count >=pair[1]:
            findPos = i
            break
    if findPos == -1 :
            findPos = len(pokemons)

    insert_data(findPos, (friend, k_count))

def insert_data(position, pokemon) :
    if position < 0 or position > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)
    kLen = len(pokemons)

    for i in range(kLen -1, position, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[position] = pokemon

pokemons = [['피카츄', 500], ['라이츄', 150], ['파이리', 300], ['꼬부기', 70], ['버터풀', 45]]

if __name__ == "__main__":

    while True :
        data = input("추가할 포켓몬 -->")
        count = int(input("생성 체력 -->"))
        find_and_insert_data(data, count)
        print(pokemons)

# 3장 연습문제

# 1. 선형리스트
# 2. 1
# 3. 4231
# 4. katok.append(None)
# 5. del(katok[2])
# 6.
# katok.append(None)
#     def add_data(friend):
#     kLen = len(katok)
#     katok[kLen] = friend
# 7.4
# 8.4