# 문자열 자료형
string = "emotion"
# 문자 개수 세기(count)
print(string.count('m'))
# 위치 알려주기1(find)
print(string.find('m'))
# 위치 알려주기2(index)
print(string.index('m'))
# 문자열 삽입(join)
string_join = " ".join('emotion')
print(string_join)
# 소문자를 대문자로 바꾸기(upper)
string = string.upper()
print(string)
# 대문자를 소문자로 바꾸기(lower)
string_upper = "EMOTION"
print(string_upper.lower())
# 왼쪽 공백 지우기(lstrip)
string_srtip = ' emotion '
print(string_srtip.lstrip())
# 오른쪽 공백 지우기(rstrip)
print(string_srtip.rstrip())
# 양쪽 공백 지우기(strip)
print(string_srtip.strip())
# 문자열 바꾸기(replace)
srting_emotion = "emotion is god club"
srting_emotion.replace("god", "king god")
# 문자열 나누기(split)
print(srting_emotion.split())

# 리스트 자료형
odd = [1, 5, 3, 7, 9]
print(odd)
# 리스트에 요소 추가(append)
odd.append(11)
print(odd)
# 리스트 정렬(sort)
odd.sort()
print(odd)
# 리스트 뒤집기(reverse)
odd.reverse()
print(odd)
# 위치 반환(index)
print(odd.index(5))
# 리스트에 요소 삽입(insert)
odd.insert(0, 13)
print(odd)
# 리스트 요소 제거(remove)
odd.remove(13)
print(odd)
# 리스트 요소 끄집어내기(pop)
odd.pop()
print(odd)
# 리스트에 포함된 요소 x의 개수 세기(count)
odd.count(1)
# 리스트 확장(extend)
print(odd)
odd.extend([21,23])
print(odd)

# 튜플 자료형
t_int = (1, 2)
t_str = ('a', 'b')
# len(tuple) : 튜플의 전체 길이 (length)
print("int: ",len(t_int))
print("str: ",len(t_str))
# max(tuple) : 튜플 안에 있는 요소값 중 최대값 반환 (문자는 알파벳 기준)
print("int: ", max(t_int))
print("str: ", max(t_str))
# min(tuple) : 튜플 안에 있는 요소값 중 최소값 반환 (문자는 알파벳 기준)
print("int: ", min(t_int))
print("str: ", min(t_str))
# tuple(seq) : 리스트를 튜플로 변환 (converting a list into tuple)
print('list: ',odd)
tuple(odd)
print('tuple: ',tuple(odd))
# tuple.count() : 튜플 내 요소의 개수 세기
print(t_int.count(1))
# tuple.index(obj.) : 튜플 내 요소가 있는 위치 index 반환
print(t_int.index(1))

# 딕셔너리 자료형
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
# Key 리스트 만들기(keys)
print(dic.keys())
# Value 리스트 만들기(values)
print(dic.values())
# Key, Value 쌍 얻기(items)
print(dic.items())
# Key로 Value얻기(get)
print(dic.get("name"))
# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print("name" in dic)
# Key: Value 쌍 모두 지우기(clear)
dic.clear()
print(dic)

# 집합 자료형
s = set([1,2,3])
# 값 1개 추가하기(add)
s.add(4)
print(s)
# 값 여러 개 추가하기(update)
s.update([4, 5, 6])
print(s)
# 특정 값 제거하기(remove)
s.remove(2)
print(s)