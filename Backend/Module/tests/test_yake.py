#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for yake package."""

import pytest
from click.testing import CliRunner

import sys, os
sys.path.append('/home/luuthanh/Desktop/Keyword_extraction/Backend/Module/yake/yake.py')
print(sys.path)
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')
import yake

def test_simple_interface():
    text_content = """
    Ông Vũ Huy Chương sinh năm 1950 tại một làng quê nghèo tại xóm 2, xã Kim Hải, huyện Kim Sơn, Ninh Bình. Cũng giống như bao thanh niên trai tráng thời đó, nghe theo tiếng gọi thiêng liêng của Tổ quốc ông đã lên đường nhập ngũ cầm súng bảo vệ quê hương. Trải qua bom đạn chiến trường, đã bao lần vào sinh ra tử, ông may mắn được trở về đoàn tụ cùng gia đình vào năm 1976 nhưng lại bị nhiễm chất độc hóa học và phải chấp nhận sống chung với chúng đến cuối đời. Bà Vũ Thị Hoa, vì cảm mến con người ông Chương nên đã bất chấp tất cả dọn về chung một nhà với ông. Họ có với nhau bốn người con, trai gái đủ cả nhưng vì tàn dư chiến tranh từ người bố khiến thân thể họ yếu ớt, bệnh tật triền miên.
    """

    pyake = yake.KeywordExtractor(lan="vi",n=3)

    result = pyake.extract_keywords(text_content)

    print(result)

    keywords = [kw[0] for kw in result]

    print(keywords)
    assert "google" in keywords
    assert "kaggle" in keywords
    assert "san francisco" in keywords
    assert "machine learning" in keywords


def test_simple_interface():
    text_content = """
    Nguyễn Thanh Tùng hay còn được biết đến với nghệ danh Sơn Tùng M-TP là một nam ca sĩ, nhạc sĩ và diễn viên người Việt Nam. Các đĩa đơn năm 2012 và 2013 của anh, "Cơn mưa ngang qua" và "Em của ngày hôm qua" đã đánh dấu mốc khởi đầu cho sự nghiệp của anh.
    """
#features=['WFreq', 'WRel', 'tf', 'WCase', 'WPos', 'WSpread'],
    text_test = '''
    Mỹ: Nhiều nơi áp lệnh giới nghiêm, huy động quân đội đối phó biểu tình
    Sức nóng biểu tình ở nhiều thành phố lớn

Theo AP, phong trào biểu tình tại Mỹ được tổ chức nhằm đòi quyền lợi cho người da màu sau vụ George Floyd qua đời hôm 25/5 sau khi bị một cảnh sát da trắng ghì đầu gối lên cổ ở Minneapolis, bang Minnesota. Cái chết của Floyd được xem đã châm ngòi cho sự giận dữ bùng phát, dẫn tới biểu tình, đập phá, cướp bóc diễn ra ở nhiều thành phố của Mỹ.

Nhiều thành phố tại nước Mỹ tiếp tục trải qua đêm 30/5 với các vụ bạo động, xung đột giữa người biểu tình và cảnh sát. Nhiều thành phố như Los Angeles, Atlanta, Seattle, Portland, Denver, Cleveland, Columbus, Pittsburgh và Philadelphia đã ban hành lệnh giới nghiêm vào ban đêm. 
Tại Los Angeles, cảnh sát đã bắn đạn cao su trấn áp đám đông giận dữ châm lửa đốt xe của lực lượng hành pháp. Tại Chicago và New York, cảnh sát và người biểu tình cũng xảy ra xô xát và một số người đã bị bắt. 

Minneapolis đã trải qua đêm biểu tình thứ 5 trong phong trào phản đối cái mà những người tham gia gọi là sự đối xử sai trái có hệ thống bởi lực lượng hành pháp. 

Thống đốc bang Minnesota Tim Walz đã điều động thêm vệ binh quốc gia hôm 30/5 và cảnh báo họ sẽ trấn áp những người tham gia bạo động. Ông Walz cảnh báo ông đang huy động toàn bộ lực lượng vệ binh 13.000 người để xử lý những người cướp bóc các cửa hàng, đốt phá cơ sở hạ tầng. 
Toàn bộ các đường cao tốc dẫn tới Minneapolis bị chặn vào đêm qua, với trực thăng quân sự bay trên không kiểm soát các hành động phá hoại.

Thống đốc các bang Georgia, Kentucky, Ohio và Texas cũng đã điều động Vệ binh quốc gia sau khi các cuộc biểu tình trở thành bạo động vào ban đêm cũng như người biểu tình bất tuân lệnh giới nghiêm.

Nguy cơ lây lan Covid-19
Các cuộc biểu tình quy mô lớn diễn ra trên các thành phố Mỹ những ngày qua đang khiến giới chức địa phương quan ngại sâu sắc và châm ngòi cho nỗi sợ hãi rằng đám đông khổng lồ sẽ lan truyền mầm bệnh Covid-19, làm bùng lên một làn sóng lây nhiễm tiếp theo ở vùng dịch lớn nhất thế giới.

Các quan chức đã kêu gọi người biểu tình bình tĩnh, bày tỏ quan điểm trong ôn hòa, mang khẩu trang khi tụ tập đông người và cảnh báo rằng họ đang gặp nguy hiểm vì đi biểu tình giữa lúc dịch bệnh vẫn đang diễn biến phức tạp.

Giới chức Minnesota hôm 30/5 cảnh báo rằng quá nhiều người biểu tình không thực hiện giãn cách xã hội hoặc mang khẩu trang khi tới đám đông. Tuy nhiên, nhiều người vẫn phớt lờ các cảnh báo.
“Thật không ổn khi giữa đại dịch, chúng tôi phải ra ngoài và rủi ro mạng sống. Nhưng tôi phải biểu tình cho cuộc đời tôi và chiến đấu cho bản thân”, người biểu tình Spence Ingram nói hôm 29/5 trong cuộc biểu tình ở Atlanta.

Ingram, 25 tuổi, mang khẩu trang, nói rằng cô bị hen suyễn và lo sẽ mắc bệnh. Nhưng cô cho biết với tư cách là một phụ nữ da màu, cô luôn cảm thấy mối đe dọa từ lực lượng cảnh sát và cô phải biểu tình phản đối điều này.
    '''
    pyake = yake.KeywordExtractor(lan="vi", n=4 , dedupLim=0.5, dedupFunc='jaro', windowsSize=1, top=10)

    result = pyake.extract_keywords(text_test)

    # highlight = yake.highlight.TextHighlighter();

    for i in result:
        print(i)

    # print(highlight.highlight(text_content, result))

    assert len(result) > 0
test_simple_interface()