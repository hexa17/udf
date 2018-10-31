import re

def change_alias(s):
    s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', str(s))
    s = re.sub(u'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', str(s))
    s = re.sub(u'[èéẹẻẽêềếệểễ]', 'e', str(s))
    s = re.sub(u'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', str(s))
    s = re.sub(u'[òóọỏõôồốộổỗơờớợởỡ]', 'o', str(s))
    s = re.sub(u'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', str(s))
    s = re.sub(u'[ìíịỉĩ]', 'i', str(s))
    s = re.sub(u'[ÌÍỊỈĨ]', 'I', str(s))
    s = re.sub(u'[ùúụủũưừứựửữ]', 'u', str(s))
    s = re.sub(u'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', str(s))
    s = re.sub(u'[ỳýỵỷỹ]', 'y', str(s))
    s = re.sub(u'[ỲÝỴỶỸ]', 'Y', str(s))
    s = re.sub(u'[Đ]', 'D', str(s))
    s = re.sub(u'[đ]', 'd', str(s))
    s = re.sub("[~!@#$^%&*\\(\\)_+={}\\[\\]|;:\"'<,>.?` /\\\\-]", ' ', str(s))
    return s

def find_one_province(address):
    dc = change_alias(address)
    provinces = ["Đà Nẵng", "Đắk Lắk", "Đắk Nông", "Đồng Nai", "Đồng Tháp", "Điện Biên", 
         "An Giang", "Bà Rịa - Vũng Tàu", "Bạc Liêu", "Bắc Giang", "Bắc Kạn", "Bắc Ninh", "Bình Định", 
         "Bình Dương", "Bình Phước", "Bình Thuận", "Bến Tre", "Cà Mau", "Cao Bằng", "Cần Thơ", "Gia Lai", 
         "Hưng Yên", "Hà Giang", "Hà Nam", "Hà Nội", "Hà Tĩnh", "Hải Dương", "Hải Phòng", "Hồ Chí Minh", 
         "Hậu Giang", "Hòa Bình", "Khánh Hòa", "Kiên Giang", "Kon Tum", "Lâm Đồng", "Lào Cai", "Lạng Sơn", 
         "Lai Châu", "Long An", "Nam Định", "Nghệ An", "Ninh Bình", "Ninh Thuận", "Phú Thọ", "Phú Yên", 
         "Quảng Bình", "Quảng Nam", "Quảng Ngãi", "Quảng Ninh", "Quảng Trị", "Sơn La", "Sóc Trăng", "Tây Ninh", 
         "Thái Bình", "Thái Nguyên", "Thanh Hóa", "Thừa Thiên Huế", "Tiền Giang", "Trà Vinh", "Tuyên Quang", "Vĩnh Long", "Vĩnh Phúc", "Yên Bái"]
    pro = ""
    for province in provinces:
        tinh = change_alias(province)
        if tinh in dc:
            pro = province
            
    if pro != "" and pro != "Hà Nội":
        return pro
    
    patterns = {
        "quan 1" : "Hồ Chí Minh",
        "quan 2" : "Hồ Chí Minh",
        "quan 3" : "Hồ Chí Minh",
        "quan 4" : "Hồ Chí Minh",
        "quan 5" : "Hồ Chí Minh",
        "quan 6" : "Hồ Chí Minh",
        "quan 7" : "Hồ Chí Minh",
        "quan 8" : "Hồ Chí Minh",
        "quan 9" : "Hồ Chí Minh",
        "quan 10" : "Hồ Chí Minh",
        "quan 11" : "Hồ Chí Minh",
        "quan 12" : "Hồ Chí Minh",
        "Hà Đông" : "Hà Tây",
        "Sơn Tây" : "Hà Tây",
        "Ba Vì" : "Hà Tây",
        "Phúc Thọ" : "Hà Tây",
        "Thạch Thất" : "Hà Tây",
        "Quốc Oai" : "Hà Tây",
        "Chương Mỹ" : "Hà Tây",
        "Đan Phượng" : "Hà Tây",
        "Hoài Đức" : "Hà Tây",
        "Thanh Oai" : "Hà Tây",
        "Mỹ Đức" : "Hà Tây",
        "Ứng Hoà" : "Hà Tây",
        "Thường Tín" : "Hà Tây",
        "Phú Xuyên" : "Hà Tây",
        "Mê Linh" : "Hà Tây",
        "HN" : "Hà Nội",
        "HCM" : "Hồ Chí Minh",
        "Bình Tân" : "Hồ Chí Minh",
        "Gò Vấp" : "Hồ Chí Minh",
        "Bình Thạnh" : "Hồ Chí Minh",
        "Bình Chánh" : "Hồ Chí Minh",
        "Hóc Môn" : "Hồ Chí Minh",
        "Tân Bình" : "Hồ Chí Minh",
        "Hoc Môn" : "Hồ Chí Minh",
        "Thủ Đức" : "Hồ Chí Minh",
        "Đắc Lắc" : "Đắk Lắk",
        "Dack Lak" : "Đắk Lắk",
        "Vũng Tàu" : "Bà Rịa - Vũng Tàu",
        "BR _ VT" : "Bà Rịa - Vũng Tàu",
        "Vũng tàu" : "Bà Rịa - Vũng Tàu",
        "KonTum" : "Kon Tum",
        "Nha Trang" : "Khánh Hòa"
    }
    if pro == "Hà Nội":
        patterns = {
            "Sơn Tây" : "Hà Tây",
            "Ba Vì" : "Hà Tây",
            "Phúc Thọ" : "Hà Tây",
            "Thạch Thất" : "Hà Tây",
            "Quốc Oai" : "Hà Tây",
            "Chương Mỹ" : "Hà Tây",
            "Đan Phượng" : "Hà Tây",
            "Hoài Đức" : "Hà Tây",
            "Thanh Oai" : "Hà Tây",
            "Mỹ Đức" : "Hà Tây",
            "Ứng Hoà" : "Hà Tây",
            "Thường Tín" : "Hà Tây",
            "Phú Xuyên" : "Hà Tây"
        }
        
    for key, value in patterns.items():
        p = change_alias(key)
        if p in dc:
            pro = province
            
    return pro

def tcvn3_to_Unicode(tcvn3str):
    TCVN3TAB = "µ¸¶·¹¨»¾¼½Æ©ÇÊÈÉË®ÌÐÎÏÑªÒÕÓÔÖ×ÝØÜÞßãáâä«åèæçé¬êíëìîïóñòô­õøö÷ùúýûüþ¡¢§£¤¥¦"
    UNICODETAB = "àáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵĂÂĐÊÔƠƯ"
    r = re.compile("|".join(TCVN3TAB))
    replaces_dict = dict(zip(TCVN3TAB, UNICODETAB))
    return r.sub(lambda m: replaces_dict[m.group(0)], tcvn3str)