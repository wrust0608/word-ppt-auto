import os
import sys

# Ensure UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Import docx builder functions from build_final_submission
from build_final_submission import build_docx_from_lines

CAU_1 = """## CÂU 1. Phân tích các nhiệm vụ chủ yếu của quản lý dự án.

### 1. Khái quát vấn đề
Quản lý dự án đầu tư xây dựng là quá trình lập kế hoạch, tổ chức, điều phối và kiểm soát các nguồn lực nhằm đưa công trình về đích đúng mục tiêu đã đề ra. Các mục tiêu này thường bao gồm việc hoàn thành đúng tiến độ, trong giới hạn ngân sách hoặc dự toán được duyệt, đạt yêu cầu chất lượng theo hồ sơ thiết kế và giữ an toàn lao động, vệ sinh môi trường. Để hiện thực hóa mục tiêu chung đó, người quản lý dự án phải thực hiện đồng thời nhiều nhiệm vụ chuyên môn chủ yếu xuyên suốt vòng đời công trình.

### 2. Các nhiệm vụ quản lý chủ yếu

#### 2.1. Quản lý phạm vi công việc
Nhiệm vụ này xác định rõ ranh giới những phần việc cần làm và những phần việc nằm ngoài dự án, thường được cụ thể hóa bằng cấu trúc phân chia công việc (WBS). Khi phạm vi được phân định rành mạch, các bên dễ thống nhất khối lượng trách nhiệm, từ đó có căn cứ chính xác để lập tiến độ và dự toán chi phí. Nếu khâu này thực hiện không tốt, dự án rất dễ phát sinh việc tự ý bổ sung hạng mục ngoài kế hoạch, dẫn đến kéo dài thời gian thi công và vượt tổng mức đầu tư ban đầu.

#### 2.2. Quản lý tiến độ
Đối với tiến độ, người quản lý cần xác định thứ tự thực hiện, thời điểm bắt đầu, kết thúc và thời lượng từng công việc, thông thường sử dụng sơ đồ ngang Gantt hoặc phương pháp đường găng (CPM). Việc theo dõi sát tiến độ hiện trường giúp phát hiện sớm các công việc bị chậm trễ, nhất là các mắt xích nằm trên đường găng. Nếu để xảy ra trễ hạn ở các vị trí này, toàn bộ thời điểm hoàn thành công trình sẽ bị đẩy lùi, kéo theo các chi phí chờ đợi của nhân công và máy móc.

#### 2.3. Quản lý chi phí
Công tác quản lý chi phí bao gồm việc kiểm soát dòng tiền từ tổng mức đầu tư ban đầu, dự toán gói thầu cho đến nghiệm thu thanh toán khối lượng hoàn thành và quyết toán vốn. Người quản lý phải thường xuyên đối chiếu chi phí thực tế với kế hoạch để nhận diện sớm nguy cơ vượt ngân sách. Nếu quản lý chi phí lỏng lẻo, công trình dễ rơi vào tình trạng đội vốn, thất thoát hoặc thiếu hụt kinh phí giữa chừng khiến việc thi công bị ngưng trệ.

#### 2.4. Quản lý chất lượng
Chất lượng công trình được kiểm soát thông qua chuỗi công việc liên tục: kiểm tra nguồn gốc và chứng chỉ vật tư đầu vào (như thép, cát, đá, xi măng, bê tông), giám sát sự tuân thủ quy trình kỹ thuật tại hiện trường, và tổ chức nghiệm thu từng công việc trước khi cho phép chuyển bước thi công. Cách làm này giúp phát hiện ngay các sai sót kết cấu từ sớm, ngăn ngừa việc phải đập bỏ sửa chữa khi cấu kiện đã hoàn thành và giữ cho công trình vận hành an toàn, bền vững.

#### 2.5. Quản lý nguồn lực (nhân lực và thiết bị thi công)
Quản lý nguồn lực tập trung vào việc bố trí đội ngũ kỹ sư, công nhân kỹ thuật và máy móc chuyên dụng phù hợp với nhu cầu của từng giai đoạn thi công. Việc huy động quá sớm khi chưa có mặt bằng sẽ làm tăng chi phí lưu bãi và thời gian máy móc nằm chờ, trong khi huy động chậm lại ảnh hưởng trực tiếp đến nhịp độ thi công ngoài hiện trường. Vì vậy, người quản lý cần điều phối nhịp nhàng để thiết bị và nhân lực phát huy tối đa công suất làm việc.

#### 2.6. Quản lý hợp đồng
Hợp đồng xây dựng là văn bản pháp lý ràng buộc quyền lợi và nghĩa vụ của các bên về khối lượng, thời gian, đơn giá, tạm ứng, bảo lãnh và xử lý các phát sinh. Giám sát chặt chẽ việc thực hiện hợp đồng giúp duy trì kỷ cương làm việc trên công trường, đồng thời hạn chế các tranh chấp kéo dài giữa chủ đầu tư và nhà thầu khi điều kiện thi công có sự thay đổi.

#### 2.7. Quản lý an toàn lao động và bảo vệ môi trường
Nhiệm vụ này bao gồm việc ban hành nội quy, trang bị bảo hộ, kiểm tra biện pháp thi công tại các vị trí nguy hiểm (như hố móng sâu, làm việc trên cao, nguồn điện, cẩu lắp cấu kiện nặng) và kiểm soát bụi, tiếng ồn, nước thải xung quanh công trường. Bất kỳ sự cố tai nạn nào xảy ra cũng có thể khiến công trình bị đình chỉ để phục vụ điều tra, gây tổn thất lớn về con người, làm gián đoạn tiến độ và phát sinh chi phí xử lý.

#### 2.8. Quản lý rủi ro và thông tin dự án
Người quản lý cần chủ động nhận diện trước các yếu tố bất lợi có thể xảy ra như biến động thời tiết, sai khác địa chất so với hồ sơ khảo sát hay biến động giá vật liệu trên thị trường để chuẩn bị sẵn phương án ứng phó. Song song đó, luồng thông tin và bản vẽ thiết kế cần được quản lý thống nhất, tránh tình trạng đội thi công sử dụng bản vẽ cũ chưa cập nhật các chỉ thị kỹ thuật mới nhất từ tư vấn.

### 3. Nhận xét và kết luận
Các nhiệm vụ quản lý nêu trên luôn gắn kết chặt chẽ và tác động qua lại lẫn nhau, thể hiện rõ ở sự cân đối giữa ba yếu tố: tiến độ, chi phí và chất lượng. Việc rút ngắn thời gian thi công thường đòi hỏi tăng ca hoặc bổ sung thiết bị, làm tăng chi phí thực hiện. Ngược lại, nếu chỉ tập trung ép giảm chi phí, nguy cơ suy giảm chất lượng vật liệu và an toàn công trình sẽ gia tăng. Do đó, người quản lý không nên theo đuổi một mục tiêu đơn lẻ một cách cực đoan mà cần nhìn nhận bức tranh tổng thể để cân đối hài hòa giữa các nhiệm vụ trong từng thời điểm."""

CAU_2 = """## CÂU 2. Phân tích sự thay đổi nhiệm vụ quản lý theo các giai đoạn dự án.

### 1. Khái quát vấn đề
Vòng đời của một dự án đầu tư xây dựng công trình trải qua ba giai đoạn liên tục: chuẩn bị dự án, thực hiện dự án và kết thúc xây dựng đưa công trình vào khai thác sử dụng. Do đặc điểm công việc, mức độ bất định và quy mô giải ngân vốn ở mỗi thời điểm rất khác nhau, các nhiệm vụ quản lý không giữ nguyên một khuôn mẫu cố định mà có sự dịch chuyển trọng tâm rõ rệt theo từng giai đoạn nhằm đáp ứng yêu cầu thực tế của công trình.

### 2. Sự thay đổi trọng tâm quản lý qua các giai đoạn

#### 2.1. Giai đoạn chuẩn bị dự án: Tập trung vào nghiên cứu tính khả thi, lựa chọn giải pháp và hoàn thiện thủ tục pháp lý
Ở giai đoạn khởi đầu, các công việc chủ yếu diễn ra trên bàn giấy và khảo sát hiện trường: đo đạc địa hình, khoan thăm dò địa chất sơ bộ, lập Báo cáo nghiên cứu khả thi, đề xuất các phương án thiết kế cơ sở, xác định tổng mức đầu tư và xây dựng phương án bồi thường, hỗ trợ tái định cư.

Trọng tâm quản lý lúc này là kiểm soát độ tin cậy của số liệu khảo sát, đánh giá tính hợp lý của các giải pháp kỹ thuật, và hoàn thiện các thủ tục pháp lý với cơ quan nhà nước về quy hoạch, đất đai, môi trường và phòng cháy chữa cháy. Giai đoạn này có đặc điểm là nguồn vốn thực tế giải ngân chưa nhiều, nhưng mức độ bất định lại rất lớn. Các quyết định lựa chọn về quy mô, công nghệ hay tuyến hướng công trình ở giai đoạn này sẽ định hình toàn bộ chi phí và quá trình vận hành của dự án sau này.

#### 2.2. Giai đoạn thực hiện dự án: Trọng tâm chuyển sang điều hành thi công, kiểm soát chi phí và chất lượng hiện trường
Bước sang giai đoạn thực hiện, hoạt động chuyển từ việc lập phương án sang triển khai thực tế ngoài hiện trường. Các công việc chính bao gồm: lập và phê duyệt thiết kế bản vẽ thi công kèm dự toán, tổ chức lựa chọn nhà thầu, tiếp nhận mặt bằng, thi công xây lắp các hạng mục, giám sát kỹ thuật và nghiệm thu thanh toán theo từng kỳ.

Nhiệm vụ quản lý ở giai đoạn này tập trung cao độ vào việc theo dõi tiến độ thi công bám sát các mốc đường găng, kiểm soát chất lượng vật tư đưa vào công trường, giám sát an toàn lao động và kiểm soát chi phí giải ngân không vượt dự toán gói thầu. Đồng thời, người quản lý phải xử lý liên tục các vướng mắc phát sinh thực tế như vướng mắc giải phóng mặt bằng cục bộ, xử lý sai khác địa chất khi đào móng hoặc điều phối giao diện thi công giữa nhiều nhà thầu cùng làm việc trên một khu vực. Đây là giai đoạn chiếm phần lớn thời gian, tập trung đông đảo nhân lực, thiết bị và giải ngân phần lớn nguồn vốn đầu tư của dự án.

#### 2.3. Giai đoạn kết thúc xây dựng đưa công trình vào khai thác: Chuyển sang công tác nghiệm thu, quyết toán và bàn giao
Khi các hạng mục xây lắp cơ bản hoàn thành, trọng tâm quản lý dịch chuyển sang việc đánh giá sự phù hợp của công trình và khép lại các nghĩa vụ pháp lý, tài chính. Công việc chủ yếu gồm: tổ chức nghiệm thu hoàn thành toàn bộ công trình, phối hợp với cơ quan quản lý chuyên ngành kiểm tra công tác nghiệm thu, lập hồ sơ hoàn công, bàn giao tài sản cho đơn vị quản lý sử dụng, thực hiện quyết toán hợp đồng với các nhà thầu, quyết toán vốn đầu tư dự án và theo dõi công tác bảo hành.

Nhiệm vụ quản lý lúc này đòi hỏi sự cẩn trọng về mặt hồ sơ chứng từ: đối chiếu khối lượng thi công thực tế với các biên bản nghiệm thu và hợp đồng đã ký để chốt giá trị thanh quyết toán; rà soát tính đầy đủ, hợp lệ của hồ sơ hoàn công; đồng thời đôn đốc nhà thầu thực hiện đầy đủ nghĩa vụ sửa chữa các khiếm khuyết phát sinh trong thời hạn bảo hành công trình.

### 3. Quy luật dịch chuyển và bài học trong quản lý dự án
Sự thay đổi nhiệm vụ quản lý qua các giai đoạn phản ánh rõ quy luật mối quan hệ giữa chi phí và khả năng tác động (quy luật Paulson). Trong giai đoạn chuẩn bị, khả năng can thiệp để thay đổi quy mô, công năng hay phương án kết cấu là lớn nhất với chi phí bỏ ra thấp nhất. Khi dự án đã bước sâu vào giai đoạn thi công, khả năng can thiệp giảm dần, trong khi chi phí sửa đổi sai sót thường tăng đáng kể khi dự án đã bước sâu vào giai đoạn thực hiện do khối lượng xây lắp đã thi công buộc phải phá dỡ, làm lại.

Cùng một nhiệm vụ quản lý nhưng nội dung và cách thức thực hiện cũng biến đổi theo từng bước:
- *Về chi phí:* Giai đoạn chuẩn bị quản lý thông qua việc xác định tổng mức đầu tư mang tính khái toán; sang giai đoạn thực hiện chuyển thành kiểm soát dự toán gói thầu và thanh toán theo khối lượng nghiệm thu; đến giai đoạn kết thúc là quyết toán hợp đồng và quyết toán vốn đầu tư.
- *Về chất lượng:* Giai đoạn đầu kiểm soát qua việc thẩm định phương án thiết kế; giai đoạn thi công kiểm tra chất lượng vật liệu và nghiệm thu cấu kiện tại hiện trường; giai đoạn cuối đánh giá toàn diện khả năng chịu lực của công trình để đưa vào khai thác sử dụng.

### 4. Nhận xét và kết luận
Sự chuyển dịch nhiệm vụ quản lý đòi hỏi người quản lý phải linh hoạt trong việc bố trí nhân sự phù hợp với đặc thù từng thời kỳ: khâu chuẩn bị cần cán bộ có chuyên môn sâu về quy hoạch, thiết kế và pháp lý; khâu thực hiện cần những kỹ sư hiện trường có kinh nghiệm điều hành và kiểm soát thi công; khâu kết thúc lại cần những nhân sự tỉ mỉ, nắm chắc các quy định về hồ sơ nghiệm thu và kiểm toán thanh quyết toán. Bài học kinh nghiệm thực tế là cần đầu tư kỹ lưỡng cho công tác chuẩn bị ngay từ đầu, hạn chế tình trạng hồ sơ thiết kế sơ sài dẫn đến việc phải liên tục điều chỉnh trong quá trình thi công."""

CAU_3 = """## CÂU 3. Đánh giá vai trò phối hợp giữa các bên tham gia.

### 1. Khái quát vấn đề
Dự án xây dựng là môi trường làm việc có sự tham gia của nhiều chủ thể độc lập về mặt pháp lý nhưng lại gắn kết mật thiết trong một quy trình công nghệ: Chủ đầu tư (hoặc Ban Quản lý dự án), Tư vấn thiết kế, Tư vấn giám sát, Nhà thầu thi công, các đơn vị Cung ứng vật tư thiết bị, cùng sự tham gia của Cơ quan quản lý nhà nước và Chính quyền địa phương. Mỗi bên đảm nhận một chức năng riêng với những mục tiêu và lợi ích cụ thể. Vì vậy, việc thiết lập mối quan hệ phối hợp nhịp nhàng giữa các bên có ý nghĩa quan trọng để dự án triển khai thuận lợi và đạt được mục tiêu chung.

### 2. Đánh giá các mối quan hệ phối hợp trong dự án

#### 2.1. Bản chất sự phụ thuộc lẫn nhau trong dây chuyền xây dựng
Công trình xây dựng thường trải qua nhiều công đoạn nối tiếp hoặc gối đầu: khảo sát, thiết kế, giải phóng mặt bằng, cung ứng vật tư, thi công nền móng, kết cấu phần thân, hoàn thiện và nghiệm thu bàn giao. Trong chuỗi liên kết này, sản phẩm của khâu trước chính là điều kiện đầu vào của khâu sau. Tiến độ bàn giao mặt bằng của địa phương quyết định thời điểm nhà thầu có thể đưa máy móc vào công trường; chất lượng bản vẽ của tư vấn thiết kế ảnh hưởng trực tiếp đến việc đặt hàng vật tư và quá trình thi công của nhà thầu. Chỉ cần một khâu gặp trục trặc, sự chậm trễ sẽ lan sang các công việc tiếp theo và ảnh hưởng đến toàn bộ tiến độ dự án.

#### 2.2. Trách nhiệm phối hợp của từng nhóm chủ thể
- **Chủ đầu tư / Ban Quản lý dự án:** Giữ vai trò đầu mối điều phối chung của toàn dự án; chịu trách nhiệm thu xếp nguồn vốn tạm ứng và thanh toán theo hợp đồng, phối hợp nhận bàn giao mặt bằng sạch, phê duyệt các đề xuất kỹ thuật và xử lý các vướng mắc, mâu thuẫn nảy sinh giữa các đơn vị.
- **Tư vấn thiết kế:** Chịu trách nhiệm về giải pháp kỹ thuật và an toàn công trình; thực hiện giám sát tác giả, giải thích kịp thời các chỉ dẫn trên bản vẽ và phối hợp xử lý các điều chỉnh khi phát hiện sai khác địa chất tại hiện trường để công trường không phải dừng chờ.
- **Tư vấn giám sát và Nhà thầu thi công:** Đây là mối quan hệ phối hợp thường xuyên nhất tại công trường. Nhà thầu cần gửi phiếu yêu cầu nghiệm thu đúng quy trình và thực hiện theo chỉ dẫn kỹ thuật; tư vấn giám sát có trách nhiệm kiểm tra, nghiệm thu chuyển bước kịp thời để nhà thầu triển khai các hạng mục tiếp theo liên tục.
- **Nhà thầu thi công và Đơn vị cung ứng vật tư:** Nhà thầu cần chia sẻ kế hoạch thi công chi tiết theo tuần/tháng để nhà cung ứng chủ động nguồn hàng; phía cung ứng chịu trách nhiệm bảo đảm vật liệu đạt chuẩn kỹ thuật, có đầy đủ chứng chỉ thí nghiệm và vận chuyển đến công trường đúng thời điểm hẹn trước.
- **Ban QLDA và Chính quyền địa phương:** Phối hợp chặt chẽ trong công tác kiểm đếm, đo đạc, lập phương án bồi thường và hỗ trợ tái định cư để bàn giao mặt bằng theo từng đoạn liền mạch, hạn chế tình trạng bàn giao ngắt quãng kiểu "xôi đỗ" gây khó khăn cho việc đưa thiết bị vào thi công.

#### 2.3. Hậu quả khi thiếu sự phối hợp chặt chẽ
Khi các bên làm việc rời rạc, dự án thường đối mặt với nhiều hệ lụy thực tế:
- *Gây chậm tiến độ công trường:* Máy móc và công nhân của nhà thầu phải tạm dừng chờ đợi do tư vấn thiết kế chậm trả lời vướng mắc bản vẽ, tư vấn giám sát chậm nghiệm thu cấu kiện, hoặc nhà cung ứng giao hàng trễ.
- *Phát sinh sai sót kỹ thuật và tốn kém chi phí:* Trong nhiều trường hợp, do chờ đợi lâu mà không nhận được giải đáp, nhà thầu tự ý xử lý các chi tiết chưa rõ trên bản vẽ, dẫn đến sai khác thiết kế và buộc phải đập bỏ để thi công lại.
- *Nảy sinh tranh chấp hợp đồng:* Khi tiến độ bị trễ, các bên có xu hướng đổ lỗi cho nhau để tránh bị phạt hợp đồng, dẫn đến các khiếu nại kéo dài về chi phí máy móc nằm chờ và đề nghị gia hạn thời gian thực hiện, làm suy giảm tinh thần hợp tác trên công trường.

### 3. Các cơ chế phối hợp trong thực tiễn quản lý
Để công tác phối hợp đi vào thực chất, dự án cần áp dụng các biện pháp quản lý rõ ràng:
- **Duy trì các cuộc họp giao ban hiện trường:** Tổ chức giao ban định kỳ hàng tuần giữa Ban QLDA, tư vấn giám sát và các nhà thầu để rà soát tiến độ, nêu rõ các vướng mắc về mặt bằng hay thủ tục kỹ thuật, đồng thời ghi nhận biên bản cam kết thời hạn giải quyết cụ thể cho từng bên.
- **Quy định rõ thời hạn xử lý văn bản và phản hồi kỹ thuật:** Ban hành quy chế phối hợp nội bộ quy định thời gian tối đa để tư vấn thiết kế giải đáp yêu cầu làm rõ bản vẽ của nhà thầu, hoặc thời hạn tư vấn giám sát phải có mặt kiểm tra sau khi nhận được thông báo nghiệm thu hợp lệ.
- **Quản lý hồ sơ và bản vẽ thống nhất:** Xây dựng quy trình bàn giao và lưu trữ bản vẽ rõ ràng, bảo đảm các nhà thầu trên hiện trường luôn sử dụng phiên bản bản vẽ mới nhất đã được phê duyệt, tránh nhầm lẫn với các bản vẽ cũ đã chỉnh sửa.
- **Xác lập ranh giới trách nhiệm:** Bảng phân định công việc cụ thể giúp các bên hiểu rõ phạm vi nhiệm vụ của mình, hạn chế tình trạng đùn đẩy trách nhiệm khi nảy sinh sự cố.

### 4. Bảng phân định trách nhiệm chủ yếu giữa các bên tham gia

| Nội dung công việc | Chủ đầu tư / Ban QLDA | Tư vấn thiết kế | Tư vấn giám sát | Nhà thầu thi công | Nhà cung ứng vật tư | Chính quyền địa phương |
|---|---|---|---|---|---|---|
| Bồi thường, giải phóng mặt bằng | Phối hợp, bố trí vốn | Hỗ trợ mốc ranh giới | Theo dõi hiện trạng | Tiếp nhận mặt bằng | Không tham gia | Trực tiếp thực hiện |
| Khảo sát và lập hồ sơ thiết kế | Quản lý, phê duyệt | Trực tiếp thực hiện | Phối hợp rà soát | Tham khảo thi công | Không tham gia | Quản lý quy hoạch |
| Xử lý phát sinh, sai khác thiết kế | Chủ trì xem xét duyệt | Trực tiếp xử lý kỹ thuật | Đánh giá, xác nhận | Báo cáo, đề xuất | Phối hợp vật tư | Không tham gia |
| Thí nghiệm, kiểm định vật liệu | Kiểm tra đột xuất | Xem xét chỉ dẫn | Trực tiếp chứng kiến | Lấy mẫu, gửi thí nghiệm | Cung cấp chứng chỉ | Không tham gia |
| Nghiệm thu công việc xây dựng | Kiểm tra định kỳ | Giám sát tác giả | Trực tiếp nghiệm thu | Mời nghiệm thu | Không tham gia | Không tham gia |
| Nghiệm thu hoàn thành, bàn giao | Chủ trì nghiệm thu | Tham gia nghiệm thu | Tham gia nghiệm thu | Lập hồ sơ hoàn công | Bảo hành thiết bị | Kiểm tra theo thẩm quyền |

### 5. Nhận xét và kết luận
Phối hợp giữa các bên tham gia không chỉ là thủ tục trao đổi giấy tờ mà là yếu tố ảnh hưởng trực tiếp đến khả năng kiểm soát tiến độ, chi phí và chất lượng công trình. Khi các bên duy trì kênh thông tin rõ ràng và làm việc trên tinh thần hợp tác, thời gian chờ đợi sẽ giảm bớt và các vướng mắc kỹ thuật ngoài hiện trường được xử lý nhanh chóng hơn. Ban QLDA cần đóng vai trò điều phối tích cực, lắng nghe khó khăn của các đơn vị và duy trì kỷ cương làm việc để hướng tới mục tiêu hoàn thành công trình đúng kế hoạch."""

CAU_4 = """## CÂU 4. Thiết kế, thi công và cung ứng vật liệu liên tục không đồng bộ. Xác định vấn đề quản lý và giải pháp.

### 1. Xác định vấn đề
Tình trạng thiếu đồng bộ giữa tiến độ thiết kế, kế hoạch thi công xây lắp và kế hoạch cung ứng vật liệu là hiện tượng khá phổ biến tại nhiều công trình xây dựng. Vấn đề quản lý trung tâm ở đây là: **Kế hoạch của ba khâu thiết kế, cung ứng và thi công được lập và điều hành một cách rời rạc, thiếu sự gắn kết logic về mặt thời gian và không gian công trường.**

Biểu hiện thực tế trên hiện trường thường gồm các tình huống sau:
- Nhà thầu đã huy động đầy đủ máy móc, thiết bị và công nhân nhưng chưa nhận được bản vẽ thiết kế bản vẽ thi công được phê duyệt, buộc công trường phải tạm dừng chờ việc.
- Bản vẽ thiết kế liên tục bị điều chỉnh sau khi vật liệu đã được đặt hàng hoặc đã vận chuyển về công trường, dẫn đến việc vật tư bị ứ đọng không sử dụng được hoặc phải sửa đổi kết cấu đã thi công.
- Vật liệu được chuyển về quá sớm khi mặt bằng chưa giải phóng xong hoặc hạng mục đi trước chưa hoàn thành, gây quá tải kho bãi và khiến vật tư bị suy giảm chất lượng do phơi nắng mưa.
- Ngược lại, khi công trường đang đẩy nhanh tiến độ thi công thì vật liệu về nhỏ giọt hoặc đứt nguồn cung, làm gián đoạn dây chuyền sản xuất.

### 2. Nguyên nhân quản lý
Tình trạng mất đồng bộ nêu trên bắt nguồn từ một số nguyên nhân chính trong công tác quản lý:
- *Các bộ phận lập kế hoạch độc lập:* Bộ phận thiết kế, bộ phận thi công hiện trường và bộ phận mua sắm vật tư thường làm việc riêng rẽ, không có sự ràng buộc chặt chẽ về các mốc thời gian hoàn thành của nhau.
- *Đánh giá chưa đầy đủ thời gian cung ứng vật tư:* Kế hoạch mua sắm thường chỉ tính thời gian vận chuyển mà chưa tính đủ thời gian tìm nguồn, ký hợp đồng, sản xuất tại nhà máy và thời gian làm thí nghiệm kiểm định chất lượng trước khi đưa vào công trình (đặc biệt đối với các loại vật tư đặc thù như cáp dự ứng lực, thép hình cỡ lớn hoặc thiết bị cơ điện).
- *Thông tin thay đổi thiết kế truyền đạt chậm:* Khi hiện trường phát hiện sai khác địa chất hoặc điều chỉnh phương án kỹ thuật, thông tin không được chuyển kịp thời cho bộ phận cung ứng, khiến việc đặt hàng vẫn tiến hành theo phương án cũ.
- *Thiếu sự điều phối tập trung:* Ban QLDA chưa phát huy tốt vai trò kết nối giữa các bên, để các đơn vị tự liên hệ trao đổi dẫn đến thông tin không nhất quán.
- *Hợp đồng cung ứng thiếu linh hoạt trước biến động giá:* Khi giá cả thị trường biến động mạnh (như giá sắt thép, cát san lấp tăng cao), các điều khoản hợp đồng trọn gói cứng nhắc dễ khiến nhà cung ứng giao hàng cầm chừng để giảm lỗ, làm đứt đoạn nguồn vật tư của công trường.

### 3. Hậu quả của sự mất đồng bộ
- *Làm gián đoạn tiến độ và kéo dài thời gian hoàn thành:* Khi bản vẽ bị chậm hoặc vật liệu thiếu hụt tại các công việc trên đường găng, thời điểm kết thúc dự án chắc chắn sẽ bị lùi lại.
- *Gây lãng phí nguồn lực và tăng chi phí:* Máy móc và nhân công phải nằm chờ việc làm giảm hiệu suất lao động; đồng thời phát sinh chi phí bến bãi, chi phí bảo quản vật tư ứ đọng và nguy cơ hao hụt, hư hỏng vật liệu.
- *Tiềm ẩn rủi ro về chất lượng công trình:* Khi vật tư bị giao trễ làm tiến độ dồn ứ, các đơn vị thi công dễ nảy sinh tâm lý làm vội vàng, rút ngắn thời gian công nghệ (như rút ngắn thời gian dưỡng hộ bê tông hoặc gia tải nền đất yếu) để kịp bù đắp tiến độ, gây ảnh hưởng tiêu cực đến chất lượng lâu dài của công trình.

### 4. Giải pháp quản lý khắc phục
Để giải quyết tình trạng mất đồng bộ, công tác quản lý dự án cần tập trung vào các giải pháp cụ thể sau:

#### 4.1. Lập tiến độ tổng thể liên kết chặt chẽ ba khâu Thiết kế – Cung ứng – Thi công (Giải pháp trọng tâm)
Ban QLDA cần chủ trì xây dựng một bản tiến độ tích hợp thống nhất giữa các bên, trong đó xác định rõ trình tự phụ thuộc: Bản vẽ thiết kế được duyệt → Đặt hàng, sản xuất, vận chuyển và làm thí nghiệm kiểm định vật liệu → Tập kết về công trường → Tổ chức thi công lắp dựng. Kế hoạch cung ứng vật tư phải được tính toán lùi từ ngày bắt đầu thi công của từng hạng mục cụ thể, cộng thêm toàn bộ thời gian cần thiết cho khâu vận chuyển và kiểm định chất lượng đầu vào, bảo đảm vật tư về đến nơi vừa đúng thời điểm công trường cần.

#### 4.2. Quản lý cung ứng bám sát tiến độ thực tế và phân loại vật liệu
Hàng tuần, bộ phận điều hành hiện trường và bộ phận cung ứng cần họp đối chiếu tiến độ thi công thực tế để điều chỉnh lịch giao hàng phù hợp với hiện trạng mặt bằng. 

Bên cạnh đó, cần phân loại chiến lược mua sắm theo tính chất vật liệu:
- Đối với vật liệu thông thường khối lượng lớn (cát, đá, đất đắp, xi măng, thép xây dựng): Khảo sát kỹ năng lực các mỏ vật liệu hợp pháp và duy trì mức dự trữ an toàn hợp lý tại các bãi phụ cận để tránh gián đoạn khi thời tiết xấu.
- Đối với cấu kiện đúc sẵn hoặc thiết bị chuyên dùng (dầm cầu, thiết bị trạm biến áp): Điều phối lịch vận chuyển khớp với thời điểm cẩu lắp ngoài hiện trường để giảm diện tích lưu kho và hạn chế chi phí bốc dỡ nhiều lần.

#### 4.3. Kiểm soát quy trình thay đổi thiết kế và rút ngắn thủ tục phê duyệt
Quy định rõ mọi điều chỉnh kỹ thuật từ tư vấn thiết kế phải được gửi đồng thời cho bộ phận hiện trường và bộ phận cung ứng trong thời hạn cụ thể để kịp dừng hoặc điều chỉnh các đơn hàng không còn phù hợp. Đồng thời, xác định rõ thời hạn tối đa để tư vấn giám sát và chủ đầu tư kiểm tra, chấp thuận hồ sơ vật liệu đệ trình của nhà thầu, tránh kéo dài thời gian chờ đợi thủ tục.

#### 4.4. Tăng cường giao ban điều phối định kỳ
Duy trì giao ban thường xuyên giữa các bộ phận kỹ thuật thiết kế, hiện trường thi công và cung ứng để rà soát kế hoạch làm việc tuần/tháng, kịp thời tháo gỡ các vướng mắc về mặt bằng tiếp nhận vật tư. Ban QLDA nên phân công một cán bộ làm đầu mối theo dõi luồng thông tin này để xử lý nhanh các bất cập phát sinh.

#### 4.5. Ứng dụng công cụ quản lý tiến độ và mô hình thông tin hỗ trợ
Sử dụng các phần mềm quản lý tiến độ chuyên ngành để theo dõi đường găng và cảnh báo sớm nguy cơ chậm vật tư. Tại những dự án có điều kiện, có thể áp dụng mô hình thông tin công trình (BIM) như một công cụ hỗ trợ trực quan giúp mô phỏng không gian công trường theo tiến độ, qua đó phát hiện trước các xung đột về bãi tập kết và bố trí cẩu lắp vật liệu hợp lý hơn.

### 5. Nhận xét và kết luận
Sự nhịp nhàng giữa thiết kế, thi công và cung ứng vật liệu là điều kiện quan trọng để duy trì hoạt động sản xuất liên tục trên công trường. Để khắc phục hiệu quả tình trạng mất đồng bộ, người quản lý cần thiết lập một kế hoạch tiến độ tích hợp ngay từ ban đầu, lấy tiến độ thi công thực tế làm căn cứ điều phối vật tư và kiểm soát chặt chẽ các thay đổi kỹ thuật. Cách làm đồng bộ và thông tin thông suốt này sẽ giúp giảm thời gian chờ và các chi phí không cần thiết, góp phần đưa dự án hoàn thành đúng mục tiêu đã đề ra."""

CAU_5 = """## CÂU 5. Một quyết định của Ban QLDA làm chậm ba nhà thầu khác nhau. Hãy đề xuất cơ chế phối hợp khắc phục.

### 1. Xác định vấn đề và bản chất tác động dây chuyền
Trong các dự án xây dựng, công việc giữa các gói thầu thường có mối liên hệ mật thiết về mặt không gian và trình tự công nghệ: nhà thầu làm móng xong mới có mặt bằng giao cho nhà thầu kết cấu thân; nhà thầu kết cấu làm xong sàn mới tạo điều kiện cho nhà thầu hoàn thiện và lắp đặt thiết bị.

Khi Ban Quản lý dự án ban hành một quyết định can thiệp kỹ thuật (chẳng hạn yêu cầu tạm dừng thi công một khu vực để khảo sát địa chất bổ sung hoặc điều chỉnh thiết kế móng), quyết định này không chỉ tác động đến đơn vị trực tiếp thi công hạng mục đó mà còn tạo ra tác động dây chuyền làm chậm các nhà thầu ở các công đoạn tiếp sau.

*Ví dụ minh họa:* Trong một dự án xây dựng cầu đường, khi phát hiện địa tầng tại vị trí trụ cầu sai khác so với hồ sơ khảo sát ban đầu, Ban QLDA ra quyết định tạm dừng thi công hố móng để khoan khảo sát bổ sung và điều chỉnh thiết kế. Quyết định này khiến Nhà thầu A (thi công móng cọc) phải cho máy móc dừng hoạt động; kéo theo Nhà thầu B (thi công dầm và thân trụ) không có mặt bằng tiếp nhận, các phiến dầm đúc sẵn tại bãi bị tồn đọng; đồng thời Nhà thầu C (thi công lan can, khe co giãn, chiếu sáng) cũng bị lùi thời gian triển khai. Nếu không có biện pháp xử lý đồng bộ, tình huống này rất dễ dẫn đến việc các nhà thầu đồng loạt gửi văn bản khiếu nại, yêu cầu gia hạn thời gian và đòi bồi thường chi phí máy móc, nhân lực nằm chờ.

### 2. Cơ chế phối hợp khắc phục
Để giải quyết tình trạng này, Ban QLDA cần chủ trì thực hiện cơ chế phối hợp gồm 5 bước cụ thể:

#### Bước 1: Xác nhận thông tin và khoanh vùng phạm vi ảnh hưởng
Ban QLDA cần gửi văn bản thông báo chính thức cho các nhà thầu, tư vấn giám sát và tư vấn thiết kế, nêu rõ lý do kỹ thuật của việc tạm dừng thi công nhằm bảo đảm an toàn công trình, xác định cụ thể phạm vi khu vực bị dừng và thời gian dự kiến xử lý xong. Thông báo chính thức giúp tránh các thông tin phỏng đoán thiếu chính xác trên công trường.

Đồng thời, tư vấn giám sát phối hợp cùng chỉ huy trưởng của ba nhà thầu tiến hành kiểm tra thực tế và ký biên bản xác nhận hiện trạng công trường tại thời điểm quyết định có hiệu lực. Biên bản cần ghi nhận rõ số lượng máy móc, thiết bị và nhân lực thực tế đang có mặt bị ảnh hưởng dừng việc để làm căn cứ giải quyết các vấn đề hợp đồng sau này.

#### Bước 2: Tổ chức cuộc họp điều phối giữa các bên
Lãnh đạo Ban QLDA chủ trì cuộc họp làm việc với tư vấn thiết kế, tư vấn giám sát và chỉ huy trưởng ba nhà thầu để công khai tình hình, nắm bắt khó khăn của từng đơn vị và cùng tìm giải pháp tháo gỡ.

Cuộc họp cần rà soát cụ thể phần việc nào bắt buộc phải dừng, phần việc nào vẫn có thể tiếp tục triển khai, từ đó thống nhất phương án điều chuyển tạm thời nguồn lực:
- Nhà thầu móng có thể điều chuyển máy khoan sang thi công các vị trí trụ khác trong cùng dự án chưa bị ảnh hưởng địa chất.
- Nhà thầu kết cấu tập trung gia công trước cốt thép, ván khuôn hoặc đúc sẵn cấu kiện tại bãi tập kết trong lúc chờ mặt bằng móng.
- Nhà thầu lắp đặt thiết bị rà soát lại tiến độ giao hàng từ nhà sản xuất; nếu thiết bị đã chuyển về công trường, Ban QLDA hỗ trợ bố trí khu vực kho bãi bảo quản tạm thời để hạn chế chi phí lưu kho bên ngoài.

#### Bước 3: Lập tiến độ điều chỉnh chung và tổ chức bàn giao mặt bằng cuốn chiếu
Thay vì để từng nhà thầu tự điều chỉnh riêng lẻ, Ban QLDA cần tổng hợp và ban hành một bản tiến độ điều chỉnh chung cho toàn bộ các gói thầu có liên quan nhằm giữ tính đồng bộ cho dự án.

Giải pháp bàn giao mặt bằng cuốn chiếu nên được áp dụng: khi nhà thầu móng thi công xong từng mố trụ độc lập, tư vấn giám sát tổ chức nghiệm thu và bàn giao ngay mặt bằng cho nhà thầu kết cấu vào làm việc, không cần chờ hoàn thành toàn bộ gói thầu móng mới bàn giao. Song song đó, Ban QLDA đôn đốc tư vấn thiết kế sớm ban hành hồ sơ điều chỉnh kỹ thuật để công trường thi công trở lại bình thường, sau đó có thể xem xét cho phép các nhà thầu tăng ca hợp lý để bù lại phần thời gian đã mất.

#### Bước 4: Xem xét giải quyết về tiến độ và chi phí theo hợp đồng
- *Về tiến độ:* Khi nguyên nhân dừng việc xuất phát từ quyết định của Ban QLDA nhằm xử lý vấn đề kỹ thuật khách quan, Ban QLDA căn cứ vào mức độ ảnh hưởng thực tế đến các công việc trên đường găng để xem xét việc gia hạn thời gian thực hiện hợp đồng tương ứng cho các nhà thầu, bảo đảm không áp dụng phạt chậm tiến độ đối với khoảng thời gian dừng chờ này.
- *Về chi phí phát sinh:* Căn cứ hợp đồng đã ký và quy định pháp luật áp dụng, Ban QLDA cùng tư vấn giám sát thẩm tra tính hợp lý, hợp lệ của các chi phí thực tế mà nhà thầu đề xuất (như chi phí khấu hao máy móc trong thời gian dừng việc theo quy định, chi phí bảo quản thiết bị). Các khoản chi phí chỉ được xem xét giải quyết nếu nhà thầu chứng minh được thiệt hại thực tế bằng biên bản kiểm tra hiện trường hợp lệ và đáp ứng đầy đủ điều kiện quy định trong hợp đồng, được chi trả từ nguồn dự phòng hợp pháp của dự án. Ban QLDA không tự động chấp thuận bồi thường nếu hồ sơ chưa được kiểm tra, thẩm định chặt chẽ.

#### Bước 5: Rà soát quy trình và thiết lập biện pháp phòng ngừa
Từ sự cố đã xảy ra, Ban QLDA cần rút kinh nghiệm bằng việc hoàn thiện quy trình làm việc nội bộ: trước khi ban hành bất kỳ quyết định can thiệp kỹ thuật hoặc tạm dừng thi công nào, bộ phận tham mưu phải đánh giá trước tác động chéo đến các gói thầu liên quan về mặt bằng và tiến độ. Cần tham vấn ý kiến của tư vấn giám sát và các nhà thầu để chủ động phương án điều chuyển công việc, đồng thời phân công một cán bộ làm đầu mối theo dõi và cập nhật lại tiến độ tổng thể ngay sau mỗi biến động lớn ngoài hiện trường.

### 3. Nhận xét và kết luận
Khi một quyết định của Ban QLDA ảnh hưởng đến nhiều nhà thầu, việc xử lý cần được thực hiện trên tiến độ chung của dự án thay vì tách riêng từng gói thầu. Ban QLDA cần kịp thời xác định phạm vi ảnh hưởng, tổ chức phối hợp giữa các đơn vị, điều chỉnh kế hoạch và xử lý các vấn đề hợp đồng trên cơ sở hồ sơ thực tế. Cách tiếp cận này giúp hạn chế tác động dây chuyền và đưa tiến độ dự án dần trở lại ổn định."""

REFERENCES = """## TÀI LIỆU THAM KHẢO

1. Bùi Ngọc Toàn (2018), *Các nguyên lý quản lý dự án*, Nhà xuất bản Giao thông Vận tải, Hà Nội.
2. Nguyễn Duy Hưng, Nguyễn Anh Tuấn (2024), *Giáo trình Quản lý dự án xây dựng*, Nhà xuất bản Giao thông Vận tải, Hà Nội.
3. Quốc hội nước CHXHCN Việt Nam, *Luật Xây dựng số 50/2014/QH13* và *Luật sửa đổi, bổ sung một số điều của Luật Xây dựng số 62/2020/QH14*.
4. Chính phủ nước CHXHCN Việt Nam, *Nghị định số 15/2021/NĐ-CP ngày 03/03/2021 quy định chi tiết một số nội dung về quản lý dự án đầu tư xây dựng* (được sửa đổi, bổ sung bởi Nghị định số 35/2023/NĐ-CP).
5. Chính phủ nước CHXHCN Việt Nam, *Nghị định số 06/2021/NĐ-CP ngày 26/01/2021 quy định chi tiết về quản lý chất lượng, thi công xây dựng và bảo trì công trình xây dựng*.
6. Chính phủ nước CHXHCN Việt Nam, *Nghị định số 10/2021/NĐ-CP ngày 09/02/2021 về quản lý chi phí đầu tư xây dựng*."""

def main():
    parts = [
        "# BÀI LÀM CÂU HỎI TỰ LUẬN – QUẢN LÝ DỰ ÁN ĐẦU TƯ XÂY DỰNG CÔNG TRÌNH",
        CAU_1,
        CAU_2,
        CAU_3,
        CAU_4,
        CAU_5,
        REFERENCES
    ]
    
    full_md = "\n\n---\n\n".join(parts)
    
    # Save markdown
    out_md = r"e:\word_ppt-auto\work\quan-ly-du-an-xaydung\TRA_LOI_CAU_HOI_QLDA_FINAL.md"
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(f"Đã lưu markdown sạch tại: {out_md}")
    
    # Build docx
    out_docx = r"e:\word_ppt-auto\work\quan-ly-du-an-xaydung\TRA_LOI_CAU_HOI_QLDA_FINAL.docx"
    lines = full_md.split("\n")
    build_docx_from_lines(lines, out_docx)
    print(f"Hoàn thành tạo tài liệu Word: {out_docx}")

if __name__ == "__main__":
    main()
