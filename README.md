# Hệ thống điều khiển xe robot bằng giọng nói

### 1. Mục tiêu nghiên cứu
Nghiên cứu sẽ tập trung vào việc xác định khả năng của các phương pháp học sâu trong việc nhận diện, phân loại và đánh giá các đặc trưng tín hiệu âm thanh có liên quan đến điều khiển tự động, nhằm tạo ra các mô hình dự đoán và điều chỉnh chính xác cho quá trình điều khiển. Bằng cách này, mục tiêu cuối cùng là cung cấp những công cụ phân tích tiên tiến, giúp tối ưu hóa hoạt động của hệ thống điều khiển tự động thông qua việc áp dụng học sâu vào việc xử lý tín hiệu âm thanh.

### 2. Phương pháp nghiên cứu
Trong nghiên cứu này, tôi thực hiện phân tích các tín hiệu âm thanh với mục tiêu là có thể điều khiển một thiết bị điện tử, ở đây là một xe robot với các lệnh đơn giản như Lên, Xuống, Trái, Phải.
- Dữ liệu đầu vào: Các tệp âm thanh, tệp ghi âm trong khuôn dạng .wav được thu thập từ giọng nói của nhiều người với môi trường bên ngoài khác nhau.
- Kết quả đầu ra: Thực hiện phân tích các tín hiệu âm thanh bằng cách sử dụng các kỹ thuật trích chọn đặc trưng, nhận dạng và phân loại để từ đó chuyển đổi từ tín hiệu âm thanh sang văn bản, hỗ trợ điều khiển thiết bị điện tử.

Đầu tiên, chúng tôi thu thập dữ liệu tín hiệu âm thanh từ môi trường thực tế bên ngoài. Dữ liệu này được tiền xử lý để loại bỏ nhiễu và chuẩn hóa trước khi đưa vào mô hình học sâu. Sau đó, chúng tôi tiến hành trích chọn đặc trưng của các tín hiệu âm thanh. Tiếp theo, chúng tôi huấn luyện mô hình sử dụng dữ liệu đã dược trích chọn và gán nhãn để mô hình có thể học và nhận diện các mẫu âm thanh tương ứng với các tình huống điều khiển cụ thể. Quá trình huấn luyện này cần sự tinh chỉnh của các siêu tham số để tối ưu hóa hiệu suất của mô hình.
	
Sau khi hoàn thành quá trình huấn luyện, chúng tôi đánh giá hiệu suất của mô hình thông qua các thước đo đánh giá như độ chính xác, độ nhạy, độ đặc hiệu. Đồng thời, chúng tôi cũng thực hiện việc áp dụng mô hình đã huấn luyện vào các tình huống thực tế để kiểm tra và xác nhận tính khả dụng và hiệu quả của nó trong ứng dụng thực tế.

### 3. Tiền xử lý dữ liệu
Trước khi có thể trích chọn các đặc trưng từ các mẫu dữ liệu, ta cần thực hiện các bước tiền xử lý để đảm bảo rằng dữ liệu đều có cùng một định dạng và các thông số chung. Cụ thể, các thông số cần được chuẩn hóa gồm:
- Tần số lấy mẫu (sample\_rate): Đảm bảo rằng tất cả các tệp WAV đều sử dụng cùng một tần số lấy mẫu là 16 kHz.
- Độ bit: Tất cả các tệp WAV có cùng độ bit là 16-bit.
- Kênh âm thanh: Các tệp âm thanh phải là đơn kênh (mono), và đảm bảo rằng tất cả các tệp WAV có cùng số lượng kênh.
- Độ dài: Mỗi tệp có độ dài 1 giây, ta có thể thêm khoảng lặng để đảm bảo độ dài của tất cả các tệp âm thanh là như nhau.

![alt text](https://github.com/Raggza/hinh/blob/main/hinh28.JPG)

Các file âm thanh này có thể tìm thấy trong thư mục [sound - robot](https://github.com/Raggza/Voice_control_system/tree/main/sound%20-%20robot).

### 4. Trích chọn đặc trưng với MFCC
Sau quá trình chuẩn hóa dữ liệu, tôi tiến hành trích chọn các đặc trưng sử dụng phương pháp MFCC. Như đã được đề cập trước đó, với bài toán nghiên cứu có số lượng nhãn cần phân loại ít (4 nhãn), tôi quyết định chỉ trích chọn 13 đặc trưng MFCC từ tín hiệu âm thanh. Quyết định này nhằm mục đích giảm chiều dữ liệu và tối ưu hóa tài nguyên tính toán, đồng thời vẫn giữ được thông tin quan trọng cần thiết cho quá trình phân loại và nhận diện. Các đặc trưng được lưu vào file data_sound.json trong thư mục [model_robot](https://github.com/Raggza/Voice_control_system/tree/main/model_robot).

![alt text](https://github.com/Raggza/hinh/blob/main/hinh41.png)

### 5. Mô hình học sâu
Trong nghiên cứu này, tôi sử dụng mô hình Hybrid (kết hợp cả hai mô hình CNN và LSTM) để huấn luyện cho máy tính. Mô hình được biểu diễn dưới dạng sơ đồ như dưới đây:

![alt text](https://github.com/Raggza/hinh/blob/main/hinh32.png)

Xem chi tiết về các tham số trong file [MFCC_Hybrid.ipynb](https://github.com/Raggza/Voice_control_system/blob/main/MFCC_Hybrid.ipynb)

### 6. Hệ thống phần cứng
Hệ thống phần cứng sử dụng Raspberry Pi làm bo mạch điều khiển của xe. Hệ thống được kết nối theo mô hình dưới đây:

![alt text](https://github.com/Raggza/hinh/blob/main/hinh39.png)

Kết quả:

![alt text](https://github.com/Raggza/hinh/blob/main/hinh42.jpg)
![alt text](https://github.com/Raggza/hinh/blob/main/hinh43.jpg)

Hệ thống bao gồm:
- Thành phần 1: Nguồn 12V - 2A được sử dụng để cấp nguồn cho 4 motor DC 3-6V và module L298N.
- Thành phần 2: Module L298N được sử dụng để thay đổi tốc độ và chiều quay của bánh xe.
- Thành phần 3,4,5,6: Motor DC 3-6V.
- Thành phần 7: Bo mạch Raspberry được kết nối với module L298N để điều khiển các động cơ.
- Thành phần 8: Nguồn 5V - 2A được sử dụng để cấp nguồn cho bo mạch.

### 6. Kết nối Socket
Hệ thống sử dụng kết nối Socket để chuyển câu lệnh từ thiết bị điều khiển đến xe. Bo mạch Raspberry Pi nhận câu lệnh và điều khiển xe tương ứng.

### 7. Kết quả hoạt động
Xem kết quả hoạt động của hệ thống qua [video](https://drive.google.com/file/d/11b4lwMeoq329lyWYXWpnNy1ROzNczhhh/view?usp=sharing) dưới đây
