#### Data type

#### 1. List
###### 1.1 List Items
- List được bao quanh bởi []
- Các phần tử trong list được sắp xếp, có thể thay đổi và trùng giá trị
- các phần tử được đánh chỉ số, phần tử đầu tiên có chỉ số 0, phần tử tiếp theo có chỉ số 1 

###### 1.2 Function
list = [5]
list2 = [2,3,5]
- **append():** thêm vào cuối list một phần tử hoặc list
list.append(10) -> [5, 10]
list.append(list2) ->[5, 10, [2, 3, 5]]
list[2] -> [2, 3, 5] (toàn bộ list2 trở thành 1 phần tử của list)
- **extend():** duyệt từng phần tử được thêm vào, sau đó thêm vào cuối list ban đầu
list.extend(10) -> [5, 10]
list.extend(list2) ->[5, 10, 2, 3, 5]
list[2] -> 2 (từng phần tử của list2 trở thành phần tử của list)
- **insert():** thêm vào list tại vị trí được chỉ định
list.insert(0, 1) -> [1, 5]
list.insert(1, list2) -> [1, [2, 3, 5], 5]
- **remove():** xóa đi tất cả các phần tử có cùng giá trị và kiểu dữ liệu
list = [5, 2, 3, 7, 5]
list.remove(5) -> [2, 3, 7]
- **clear():** xóa tất cả các phần tử trong danh sách
list = [5, 2, 3, 7, 5]
list.clear() -> []
- Một số function khác của list: sort, reverse, ...
#### 2. Tuple
- Tuple được bao quanh bởi cặp ()
- Các phần tử trong tuple được sắp xếp, không thể thay đổi và trùng giá trị
- các phần tử được đánh chỉ số, phần tử đầu tiên có chỉ số 0, phần tử tiếp theo có chỉ số 1 
###### 2.1 Declare
- **Tuple rỗng:** tuple_empty = () | tuple_empty = tuple()
- **Tuple 1 phần tử:** cuối tuple cần có ", " để trình biên dịch hiểu rằng đó là 1 tuple, nếu không sẽ hiểu là 1 giá trị
\+ Single-element tuple
my_tuple = (1,)
print(type(my_tuple))  # Output: <class 'tuple'>
\+ Integer value without a comma
my_value = (1)
print(type(my_value))  # Output: <class 'int'>
- **Tuple >= 2 phần tử:** tuples = ("hello", ("python", "world"))
- Tuple có thể sử dụng chỉ số kép để truy cập giá trị của phần tử kép
Tuple = [(0, 1), (2, 3), (4, 5)]
Tuple[2][0] -> 4 (2 đại diện index thứ 2 trong tuple, 0 đại diện giá trị thứ 1)
Tuple[2][1] -> 5 (2 đại diện index thứ 2 trong tuple, 1 đại diện giá trị thứ 2) 
###### 2.2 Function
- len(tuple): Trả về độ dài hoặc số phần tử trong tuple.
- tuple(iterable): Tạo một bộ dữ liệu mới từ một bộ lặp có thể lặp lại, chẳng hạn như danh sách, chuỗi hoặc bộ dữ liệu khác.
my_list = [1, 2, 3, 4, 5]
new_tuple = tuple(my_list)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)
- tuple.count(element): Trả về số lần xuất hiện của một phần tử cụ thể trong tuple.
my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))  # Output: 3
- tuple.index(element): Trả về chỉ số của lần xuất hiện đầu tiên của một phần tử cụ thể trong bộ dữ liệu.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2
- sorted(): sắp xếp các 
tuple = ("a", "c", "b", "d", "f", "e")
sortedTuple = sorted(Tuple)
print (sortedTuple) # ("a", "b", "c", "d", "e", "f")

- Ngoài ra tuple có 1 số keyword: in, not in 