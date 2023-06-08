## Python
#### Tổng quan về Python


## II. Hướng đối tượng trong Python
#### 1. Class
Python là một ngôn ngữ lập trình hướng đối tượng. Hầu hết mọi thứ trong Python đều là một đối tượng, với các thuộc tính và phương thức của nó. Class giống như một hàm tạo đối tượng hoặc "bản thiết kế" để tạo đối tượng.

###### 1.1 Tổng quan về class
Một Class là một kế hoạch chi tiết hoặc nguyên mẫu do người dùng định nghĩa mà từ đó các đối tượng được tạo ra. Các Class cung cấp phương tiện kết hợp dữ liệu và chức năng lại với nhau. Việc tạo một Class mới sẽ tạo ra một loại đối tượng mới, cho phép tạo các thể hiện mới của loại đó. Mỗi thể hiện của Class có thể có các thuộc tính gắn liền với nó để duy trì trạng thái của nó. Các thể hiện của Clase cũng có thể có các phương thứcể sửa đổi trạng thái của chúng.

###### 1.2 Đối tượng của Class 
Một đối tượng là một thể hiện của một lớp. Một lớp giống như một bản thiết kế trong khi một thể hiện là một bản sao của lớp với các giá trị thực tế

Một đối tượng bao gồm:

**State:** Nó được đại diện bởi các thuộc tính của một đối tượng. Nó cũng phản ánh các thuộc tính của một đối tượng.
###### Behavior:  Nó được đại diện bởi các phương thức của một đối tượng. Nó cũng phản ánh phản ứng của một đối tượng với các đối tượng khác.
**DIdentity:** Nó cung cấp một tên duy nhất cho một đối tượng và cho phép một đối tượng tương tác với các đối tượng khác.

#### 2. Method
Method (phương thức): Trong Python, các phương thức là các hàm được liên kết với một đối tượng và có thể thao tác dữ liệu của nó hoặc thực hiện các hành động trên nó. Chúng được gọi bằng ký hiệu dấu chấm, với tên đối tượng theo sau là dấu chấm và tên phương thức. Các phương thức là một phần quan trọng của lập trình hướng đối tượng trong Python.


Trong Python, các tính chất của lập trình hướng đối tượng (OOP) được thể hiện thông qua cú pháp và các khái niệm:

**Encapsulation (Đóng gói)**: Đóng gói là tính chất cho phép gom nhóm các dữ liệu (thuộc tính) và các phương thức liên quan vào trong một đối tượng. Điều này giúp che dấu thông tin và cung cấp mức độ truy cập và tương tác phù hợp. Trong Python, các thuộc tính và phương thức của một lớp được đóng gói trong cùng một định nghĩa lớp.

**Inheritance (Kế thừa)**: Kế thừa cho phép lớp con (subclass) kế thừa các thuộc tính và phương thức của lớp cha (superclass). Lớp con có thể mở rộng và tái sử dụng mã nguồn của lớp cha. Trong Python, để kế thừa từ một lớp cha, bạn chỉ cần khai báo tên lớp cha trong định nghĩa lớp con.

**Polymorphism (Đa hình)**: Đa hình cho phép các đối tượng cùng kiểu có thể hiểu theo nhiều cách khác nhau. Điều này giúp cho việc sử dụng và tương tác với các đối tượng trở nên linh hoạt hơn. Trong Python, đa hình được thể hiện thông qua tính năng đa hình động, cho phép chúng ta gọi các phương thức cùng tên trên các đối tượng khác nhau.

**Abstraction (Trừu tượng)**: Trừu tượng là tính chất cho phép tạo ra các lớp trừu tượng và phương thức trừu tượng để che dấu chi tiết cài đặt và chỉ tập trung vào các khái niệm quan trọng. Trong Python, ta có thể sử dụng các lớp trừu tượng và phương thức trừu tượng bằng cách sử dụng module abc và decorator @abstractmethod.

**Interface (Giao diện)**: Python không có khái niệm interface như trong một số ngôn ngữ khác, nhưng ta có thể sử dụng các lớp trừu tượng và phương thức trừu tượng để tạo ra một hợp đồng (contract) cho các lớp con. Điều này đảm bảo các lớp con phải tuân thủ các phương thức đã được định nghĩa trong lớp cha.


#### Syntax(Cú pháp)  
Cú pháp khi viết code trong Python thể hiện các tính chất:
- Định nghĩa lớp (class): class ClassName:.
- Định nghĩa thuộc tính (attribute): self.attribute_name = value.
- Định nghĩa phương thức (method): def method_name(self, arguments):.
- Kế thừa từ lớp cha: class SubClassName(SuperClassName):.
- Sử dụng decorator @property cho getters, setters, và properties.
- Sử dụng decorator @classmethod cho class methods.
- Sử dụng decorator @staticmethod cho static methods.
- Sử dụng module abc và decorator @abstractmethod cho abstract classes và abstract methods.









Có ba loại phương thức cơ bản trong Python:
- Instance Method
- Class Method
- Static Method

Instance Method: Mục đích của các phương thức Instance là thiết lập hoặc nhận thông tin chi tiết về các thể hiện (đối tượng), là loại phương thức phổ biến nhất được sử dụng trong lớp Python. Chúng có một tham số mặc định - self, trỏ đến một thể hiện của lớp,  có thể thay đổi tên của tham số này. Ví dụ:
class My_class:
  def instance_method(self):
    return "This is an instance method."

**Class Method:** Mục đích của các phương thức Class là thiết lập hoặc lấy thông tin chi tiết (trạng thái) của lớp. Nó không thể truy cập hoặc sửa đổi dữ liệu phiên bản cụ thể. Chúng bị ràng buộc với lớp thay vì các đối tượng của chúng. Hai điều quan trọng về các phương thức của Class:

Để định nghĩa một phương thức Class, ta phải xác định rằng đó là một phương thức Class với sự trợ giúp của decorator @classmethod
Các phương thức lớp cũng nhận một tham số mặc định- cls, trỏ đến lớp. Một lần nữa, điều này không bắt buộc phải đặt tên cho tham số mặc định là “cls”. Nhưng tốt hơn hết là tuân theo các quy ước




#### Các tính chất của OOP trong Python
**Private, Protected, Public**
**Private (riêng tư)**: Trong Python, thuộc tính hoặc phương thức có thể được coi là riêng tư bằng cách sử dụng dấu gạch dưới đầu tên. Ví dụ: _private_variable.

**Protected (bảo vệ):** Trong Python, thuộc tính hoặc phương thức có thể được coi là bảo vệ bằng cách sử dụng hai dấu gạch dưới đầu tên. Ví dụ: __protected_variable.

**Public (công khai):** Thuộc tính hoặc phương thức không có quy ước đặc biệt và có thể truy cập từ bất kỳ nơi nào. Ví dụ: public_variable.


#### Static Method và Class Method
Static Method (phương thức tĩnh): Là phương thức thuộc về class và không truy cập được đến thuộc tính hoặc phương thức của class thông qua từ khóa self. Để khai báo một static method trong Python, ta sử dụng decorator @staticmethod. Ví dụ:
class MyClass:
    @staticmethod
    def my_static_method():
        # code của static method

**Class Method:** là phương thức thuộc về class và có thể truy cập được đến thuộc tính và phương thức của class thông qua từ khóa cls. Để khai báo một class method trong Python, ta sử dụng decorator @classmethod. Ví dụ:

**Getters, Setters và Property**
**Getter:** Là các phương thức được sử dụng để lấy giá trị của thuộc tính. Để khai báo một getter trong Python, ta sử dụng decorator @property. Ví dụ:
class MyClass:
    @property
    def my_property(self):
        return self._my_property

**Setters:** Là các phương thức được sử dụng để gán giá trị cho thuộc tính. Để khai báo một setter trong Python, ta sử dụng decorator @my_property.setter. Ví dụ:
class MyClass:
    @property
    def my_property(self):
        return self._my_property
    
    @my_property.setter
    def my_property(self, value):
        self._my_property = value


from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

Property (thuộc tính): Kết hợp getter và setter để tạo ra một thuộc tính ảo. Ví dụ:
