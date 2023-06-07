## Docker Overview
#### Why is Docker
Docker là một nền tảng mở để phát triển, vận chuyển và chạy các ứng dụng. Docker cho phép tách các ứng dụng của mình khỏi cơ sở hạ tầng để có thể phân phối phần mềm một cách nhanh chóng. Với Docker, việc quản lý cơ sở hạ tầng của mình giống như quản lý các ứng dụng của mình. Bằng cách tận dụng các phương pháp của Docker để vận chuyển, thử nghiệm và triển khai mã một cách nhanh chóng, ta có thể giảm đáng kể độ trễ giữa viết mã và chạy mã trong sản xuất.
#### What is Docker
Docker cung cấp khả năng đóng gói và chạy một ứng dụng trong một môi trường biệt lập lỏng lẻo được gọi là container. Sự cô lập và bảo mật cho phép bạn chạy đồng thời nhiều container trên một máy chủ nhất định. Các container rất nhẹ và chứa mọi thứ cần thiết để chạy ứng dụng, vì vậy ta không cần phải dựa vào những gì hiện được cài đặt trên máy chủ. Bạn có thể dễ dàng chia sẻ các vùng chứa trong khi làm việc và đảm bảo rằng mọi người được chia sẻ đều nhận được cùng một container hoạt động theo cùng một cách.

Docker cung cấp công cụ và nền tảng để quản lý vòng đời của các container:
- Phát triển ứng dụng của bạn và các thành phần hỗ trợ của nó bằng cách sử dụng vùng chứa.
- Container trở thành đơn vị phân phối và thử nghiệm ứng dụng của bạn.
- Khi bạn đã sẵn sàng, hãy triển khai ứng dụng của bạn vào môi trường sản xuất, dưới dạng bộ chứa hoặc dịch vụ được phối hợp. Điều này hoạt động giống nhau cho dù môi trường sản xuất của bạn là trung tâm dữ liệu cục bộ, nhà cung cấp đám mây hay kết hợp cả hai.
![scrum_work](../images/docker.PNG)

#### Why use Docker?
Docker cho phép các nhà phát triển truy cập các khả năng chứa riêng này bằng cách sử dụng các lệnh đơn giản và tự động hóa chúng thông qua giao diện lập trình ứng dụng (API) tiết kiệm công việc. So với LXC(LinuXContainers), Docker cung cấp:
- Tính di động của container được cải thiện và liền mạch: Mặc dù container LXC thường tham chiếu các cấu hình dành riêng cho máy, nhưng container Docker chạy mà không cần sửa đổi trên mọi môi trường máy tính để bàn, trung tâm dữ liệu và đám mây. 
- Trọng lượng thậm chí còn nhẹ hơn và cập nhật chi tiết hơn: Với LXC, nhiều quy trình có thể được kết hợp trong một container. Điều này cho phép xây dựng một ứng dụng có thể tiếp tục chạy trong khi một trong các bộ phận của ứng dụng đó bị gỡ xuống để cập nhật hoặc sửa chữa. 
- Tự động tạo container: Docker có thể tự động tạo container dựa trên mã nguồn ứng dụng. 
- Phiên bản container: Docker có thể theo dõi các phiên bản của hình ảnh vùng chứa, quay trở lại các phiên bản trước đó và theo dõi ai đã tạo phiên bản và cách thức. Nó thậm chí chỉ có thể tải lên các container giữa phiên bản hiện có và phiên bản mới. 
- Tái sử dụng container: Các container hiện có có thể được sử dụng làm hình ảnh cơ sở—về cơ bản giống như các mẫu để tạo container mới. 
- Thư viện container được chia sẻ: Nhà phát triển có thể truy cập sổ đăng ký nguồn mở chứa hàng nghìn container do người dùng đóng góp. 


#### Docker tools and terms
Một số công cụ, thuật ngữ và công nghệ khi sử dụng Docker bao gồm: 
- DockerFile: Mỗi Docker container bắt đầu bằng một tệp văn bản đơn giản chứa các hướng dẫn về cách xây dựng Docker container image. DockerFile tự động hóa quá trình tạo Docker image. Về cơ bản, đây là danh sách các command-line interface (CLI) mà Docker Engine sẽ chạy để lắp ráp hình ảnh. Danh sách các lệnh Docker rất lớn, nhưng được chuẩn hóa: Các hoạt động của Docker hoạt động giống nhau bất kể nội dung, cơ sở hạ tầng hay các biến môi trường khác. 
- Docker images: Docker images chứa mã nguồn ứng dụng có thể thực thi cũng như tất cả các công cụ, thư viện và phần phụ thuộc mà mã ứng dụng cần để chạy dưới dạng container. Khi bạn chạy Docker images, nó sẽ trở thành một phiên bản (hoặc nhiều phiên bản) của container. Có thể xây dựng Docker images từ đầu, nhưng hầu hết các nhà phát triển đều kéo chúng xuống từ các kho lưu trữ chung. Nhiều Docker images có thể được tạo từ một hình ảnh cơ sở duy nhất và chúng sẽ chia sẻ những điểm chung trong ngăn xếp của chúng. Docker images được tạo thành từ các lớp và mỗi lớp tương ứng với một phiên bản của hình ảnh. Bất cứ khi nào thực hiện các thay đổi đối với hình ảnh, một lớp trên cùng mới sẽ được tạo và lớp trên cùng này sẽ thay thế lớp trên cùng trước đó làm phiên bản hiện tại của hình ảnh. Các lớp trước đó được lưu để phục hồi hoặc được sử dụng lại trong các dự án khác.
- Docker containers: Docker container là phiên bản trực tiếp, đang chạy của Docker images. Trong khi Docker images là các tệp chỉ đọc, thì các container là nội dung có thể thực thi được. Người dùng có thể tương tác với chúng và quản trị viên có thể điều chỉnh cài đặt và điều kiện của họ bằng các lệnh Docker. 

#### Sự khác biệt của nó với chạy trên máy host or sử dụng virtual machine container
- Docker container khởi động trong vài mil giây thay vì một phút đối với máy ảo
- Tiết kiệm dung lượng ổ đĩa và các tài nguyên hệ thống 
- Không cần ảo hóa vì Docker chạy trực tiếp trên hệ điều hành của server
- Cô lập ở mức tiến trình kém an toàn hơn, ảo hóa cô lập hoàn toàn -> an toàn hơn 

#### Docker Image
Docker image là 1 phần được sử dụng để thực thi code trong Docker container. Docker images thực hiện 1 tập chỉ dẫn để xây dựng 1 mẫu docker container. Docker image đóng vai trò là điểm bắt đầu khi sử dụng Docker

#### Image layer
Docker image bao gồm rất nhiều layer. Mỗi layer sẽ được xây dưng ở trên 1 layer để tạo thành 1 loạt với images ở giữa. Sự sắp xếp được đảm bảo rằng mỗi layer phụ thuộc vào layer ngay trước nó. Sự sắp xếp layer trong hệ thống phân cấp là rất quan trọng. Nó cho phép ta đặt các payer thường xuyên thay đổi lên trên để có thể quản lý sự thay đổi của Images 1 cách hiệu quả.
#### Docker Container
Docker là một tiêu chuẩn của phần mềm đóng gói mã và tất cả phụ thuộc để ứng dụng chạy nhanh và đáng tin cậy từ môi trường này sang môi trường khác.

#### Docker         