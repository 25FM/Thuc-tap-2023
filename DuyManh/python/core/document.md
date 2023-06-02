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

#### 3. Set
- Set được sử dụng để lưu trữ nhiều item trong 1 biến duy nhất
- Các phần tử trong set được sắp xếp, không thể thay đổi và không trùng giá trị
- 1 set có thể có nhiều kiểu dữ liệu:
set1 = {"abc", 34, True, 40, "male"}
#### 3.1 Function
- len(): xác định số item có trong set
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) -> 3
- set(): constructor để khởi tạo 1 set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
- type(): set có thể định nghĩa 1 object với kiểu dữ liệu là set
myset = {"apple", "banana", "cherry"} -> <class 'set'>

#### 4. Dictionary
- Dictionary là 1 tập hơp được sắp xếp, có thể thay đổi và không thể trùng lặp key
- 1 key - 1 value: 1 key đại diện có 1 value
- Có thể khởi tạo một dictionary bằng cách đặt các cặp key-value trong cặp dấu ngoặc nhọn {} hoặc sử dụng hàm dict().
- Truy cập giá trị trong dictionary bằng key tương ứng
- Để thay đổi giá trị trong dictionary thì ta có thể thông qua key để thực hiện
- Sử dụng cú pháp dictionary[key] = value để thêm một cặp key-value mới vào dictionary.
- Có thể sử dụng từ khóa del để xóa một cặp key-value hoặc sử dụng phương thức pop() để xóa và trả về giá trị tương ứng.
- Sử dụng vòng lặp for để lặp qua các key-value trong dictionary.
- Ngoài ra có 1 số keyword và function của dictionary: in, len(), copy(), clear(), keys(), values(), update()

## Package, Modules
#### 1. Modules
- modules giống như một thư viện code.
- là tệp chứa tập hợp các chức năng bạn muốn đưa vào ứng dụng của mình.
- tạo 1 module ta tạo 1 file .py và viết hàm bên trong file được tạo
- Để sử dụng module trong ứng dụng của mình, sử dụng import để thêm module