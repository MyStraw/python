-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: metro
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stations`
--

DROP TABLE IF EXISTS `stations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stations` (
  `StationCode` int NOT NULL,
  `StationName` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `StationNameplus` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `EnglishName` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Tel` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Address` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `History` varchar(800) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`StationCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stations`
--

LOCK TABLES `stations` WRITE;
/*!40000 ALTER TABLE `stations` DISABLE KEYS */;
INSERT INTO `stations` VALUES (95,'다대포해수욕장','다대포해수욕장','Dadaepo Beach','051-678-6195','부산광역시 사하구 다대로 지하 692','큰 포구가 많은 바다라는 데서 비롯되며 일본서기에는 다다라(多多羅)로 기록되어 있다. 이곳은 일찍부터 왜구의 출몰이 잦았으며 따라서 국방상 중요한 요새지였다. 조선 세종 때는 이곳에 수군만호영을 설치 수군 123인과 병선 9척을 배치하였고 성종 때는 높이 4ｍ 둘레 560ｍ의 다대포진을 축성한 바 있으며 임진왜란 때 다대포첨사였던 윤흥신(尹興信)과 그 동생 흥제(興悌)가 왜군과 접전을 벌여 전사한 유서 깊은 곳이다.'),(96,'다대포항','다대포항','Dadaepo Harbor','051-678-6196','부산광역시 사하구 다대로 지하 548','1971년 제1종 어항(지금의 국가어항)으로 지정되면서 개발되기 시작하여 1995년 공사를 완료하였다. 부산 지역엔 총 51개의 어항이 있는데 그중 국가어항은 다대포항과 대변항 두 곳이다. 다대포항은 부산항을 이루고 있는 네 곳의 항구(북항 감천항 다대포항 남항) 중 하나로 원래 목재 화물 부두로 개발되었다. 낙동강 하구에 위치하고 있으며 수심은 2~20m으로 얕고 항역이 좁은 편이다. 바다 밑바닥은 진흙으로 이루어져 있으며 3면이 육지에 둘러싸여 있다. 소형 선박을 정박시키고 피항시키기에 좋은 항구로 주로 고등어 삼치 방어 등의 연안 어획물을 취급한다. '),(97,'낫개','낫개','Natgae','051-678-6197','부산광역시 사하구 다대로 지하 422','멸치잡이로 유명했던 옛날의 낫개 포구를 그대로 사용'),(98,'신장림','신장림','Sinjangnim','051-678-6198','부산광역시 사하구 다대로 지하 310','지명은 숲이 우거지고 지형적으로 길게 늘어선 동네라는 뜻에서 유래되었다. 안장림  바깥 장림  보덕보(부득포 또는 비득포)의 3개 마을로 구분된다. 장림 지역이 주거지역 공단 병원 등 새로운 중심을 이루고 있어 옛날의 안장림과 바깥장림 식으로 갈라 놓을 수 있다'),(99,'장림','장림','Jangnim','051-618-6199','부산광역시 사하구 다대로 지하 230','지명은 숲이 우거지고 지형적으로 길게 늘어선 동네라는 뜻에서 유래되었다. 안장림 · 바깥 장림 · 보덕보(부득포 또는 비득포)의 3개 마을로 구분된다. 바깥 장림은 농업을 안장림은 어업을 주업으로 하여 생활하고 있었으며 지금은 주택지구로 바뀌었다. 보덕포는 안장림 서남쪽 바닷가에 있던 마을로서 보득포 · 부득포 · 버득포라고도 하였다. 1983년에 서구에서 사하구 관할로 바뀌었고 같은 해 장림 1 · 2동으로 분동되어 오늘에 이른다.'),(100,'동매','동매','Dongmae','051-618-6100','부산광역시 사하구 신산로 지하 168','해발 210ｍ인 산 서쪽에 있는 동매 마을에서 유래'),(101,'신평','신평','Sinpyeong','051-678-6101','부산광역시 사하구 하신번영로 140','신평은 새로운 평지라는 뜻으로 신촌 새벌 등과 통하는 지명으로 파악된다. 동래군가호안(1904)에 신평동이란 행정지명이 처음으로 기록이 보인다. '),(102,'하단','하단(부산본병원)','Hadan','051-678-6102','부산광역시 사하구 낙동남로 지하 1415','하단동(下端洞)의 옛 마을 이름은 평림리(平林里)라고 불린 일이 있으며 하단리라고 불리기도 했다.'),(103,'당리','당리(사하구청)','Dangni','051-678-6103','부산광역시 사하구 낙동대로 지하 405','당리동(堂里洞)에는 제석골(帝釋谷)이라고 불리는 계곡이 있다 그 제석곡에 사당이 있어 지난날에는 여신을 모셨다고 한다. 그래서 신주를 모신 당집의 곳이라 하여 당리가 되었다는 것이다.'),(104,'사하','사하','Saha','051-678-6104','부산광역시 사하구 낙동대로 지하 309','동래부지(1740)에 의하면 동래군 사천면을 다시 상단과 하단으로 나누는데 上端을 사상지역이고 下端은 사하지역이다.  사천면의 사와 하단의 하를 따서 사하라고 하였다.'),(105,'괴정','괴정','Goejeong','051-678-6105','부산광역시 사하구 낙동대로 지하 221','지금의 괴정동을 옛날에는 목장리라 했다. 조선시대에는 국마(國馬)를 기르는 목장이었는데 이 괴정동의 목장이 가장 규모가 컸다. 그때 다대포첨사가 목장을 감독하는 감목관이었는데 어느 감독관 때 감목행위가 너무 지나치게 가혹해서 마을사람들이 팔정자나무 아래서 그 감목관을 성토하다가 비참한 죽음을 입었다고 한다. 그 팔정자나무의 하나가 지금 부산시 보호수로 지정된 회화나무인데 이 나무가 있는 정자를 괴정이라 했고 이 괴정으로 괴정동이란 마을 이름이 바뀌었다고 한다.'),(106,'대티','대티(동주대학)','Daeti','051-678-6106','부산광역시 사하구 낙동대로 지하 141','大峙(대치)의 .峙(치)원음이  디 라 해도 「지」「치」로 구개음화 된지 오래다. 그런데 구개음화 버릇되기가 심한 영남지방에서 구개음화 이전의 「대티」의 「대티고개」로 지금도 남아있다. 이에 대해서는 국어학자 박자흥교수가 실제 답사를 한 바에 의하면「대티」 이전은 「한티」었다는 것을 조사 당시의 古老들의 말에서 확인되었다고 한다. 큰 고개로서의 「한」과 峙의 원음 「디」가 「티」로 소리나서 「한티」였는데 그 「한」이 「大」로 쓰게 되면서도 「티」는 본디 나던 소리인 구개음화 이전의 상태를 지속하고 있다는 것이다. 이로 미루어 보아 「대치고개」는 「한티」고개에서 나온 것이 사실인 것 같다고 「한티고개」가 「대티고개」가 되어서도 종전에 일컬어지던 「티」소리를 지키고 있는 것으로 보아진다'),(107,'서대신','서대신','Seodaesin','051-678-6107','부산광역시 서구 대영로 지하 1','대신동이란 마을 이름이 처음 생긴 것은 1914년으로 추정되며 보수천의 호안공사 이후 일본인이 대거 밀려와서 생긴 새로운 시가지를 한새벌이라 부른 데서 비롯되었다. 한새벌의 한은 큰길을 한길이라 하듯이 큰대(大) 또는 태(太) 새는 새로운이라는 뜻의 신(新) 벌은 넓은 땅이라는 뜻을 가진 동(洞)이므로 대신동은 한새벌의 한자식 표현이라 할 수 있다.'),(108,'동대신','동대신','Dongdaesin','051-678-6108','부산광역시 서구 구덕로 지하 290','동대신동은1926 년 동대신정과 서대신정으로 구분하게 되었고 광복 이후 1947년 일제식 명칭만 바꾼 동대신동 123 가로 불리우게 되었고 1959년 1월 동명개정 때 동대신123동으로 바꾸어 오늘에 이르고 있다.'),(109,'토성','토성','Toseong','051-678-6109','부산광역시 서구 구덕로 지하 170','토성동(土城洞)이란 동명은 이곳에 토성이 있었다는 데서 붙여진 것이다. 이 토성은 아미동 구 화장장 부근을 중심으로 아미골 아래쪽에 반월형으로 축조된 성으로서 현 토성중학교 부근을 통과하며 성내 면적이 3∼4천평 되는 반월성이다. 성의 높이는 4∼5척이 되었다는 기록이 있다.'),(110,'자갈치','자갈치','Jagalchi','051-678-6110','부산광역시 중구 구덕로 지하 80','용두산에서 내려다보이는 남포(南浦) 일대의 바닷가를 자갈치라 한다. 자갈치는 본래 자갈+치로 구성된 지명이다. 이 지명은 이 해안이 매립되기 전에 이미 명명된 것으로 본래 주먹만한 크기의 옥돌자갈들로 이루어진 수려한 자갈해안이었기 때문에 명명된 것이다. 치는 언저리 언덕빼기라는 뜻이니 이에 자갈치는 자갈언저리라는 지형적 특성으로 말미암아 명명된 지명이다.'),(111,'남포','남포','Nampo','051-678-6111','부산광역시 중구 구덕로 지하 12','남포동은 남포에서 유래한 것이다. 남포는 영도대교 (일명 영도다리)로부터 보수천 하구를 지나 부산공동어시장에 이르는 남항의 해안에 해당하는데 본래 이곳은 자갈치였다. 그런데 이곳이 매립되면서 일본식 지명인 남빈으로 불리다가 광복 이후인 1947년 우리식의 한자 지명인 남포로 바뀌어 지금의 동명으로 되었다.'),(112,'중앙','중앙','Jungang','051-678-6112','부산광역시 중구 중앙대로 지하 83','광복이후 부산역(지금의 본부세관 맞은편 소화물 취급소)을 가진 중앙부에 위치하여 있다는 뜻에서 1947년 동명개정 때 중앙동으로 개칭하였다. 1982년 5월 시조례에 의해 법정동인 대교가를 중앙동으로 명칭이 바뀌어 오늘에 이르고 있다.'),(113,'부산역','부산','Busan Station','051-678-6113','부산광역시 동구 중앙대로 지하 200','『세종실록지리지』에는 동래부산포(東萊富山浦)라 하였고 신숙주의『해동제국기』에도 동래지부산포(東萊之富山浦)라 하였으며 또 같은 책『삼포왜관도(三浦倭館圖)』에도 동래현부산포(東萊縣富山浦)라고 기록해 놓고 있다. 1481년(성종 12)에 편찬되고 그후 여러번 증보된『동국여지승람(1481)』산천조에 보면 부산은 동평현(오늘날 당감동 근처)에 있으며 산이 가마꼴과 같으므로 이같이 이름하였는데 그 밑이 곧 부산포이다. 항거왜호가 있는데 북쪽 현에서 거리가 21리이다.라고 하여 산 모양이 가마꼴과 같아 부산(釜山)이라고 하였다는 부산이라는 이름이 나오고 그후 이를 그대로 인용하여 부산이라고 기록하고 있다'),(114,'초량','초량','Choryang','051-678-6114','부산광역시 동구 중앙대로 지하 264','초량동(草梁洞)의 유래는 1678년 초량소산(草梁小山)인 지금의 용두산 주위에 왜관이 설치되기 이전 지금의 부평동에 어민들이 얼마간 살았을 뿐 초량 이남은 사람이 살지 않은 억새풀과 띠풀의 초원지대로 샛디라하여 초량이었다.'),(115,'부산진','부산진','Busanjin','051-678-6115','부산광역시 동구 중앙대로 지하 350','부산진의 명칭은 임진왜란 당시 부산포구의 관문이라고 할 수 있는 부산진성에서 유래.'),(116,'좌천','좌천','Jwacheon','051-678-6116','부산광역시 동구 중앙대로 지하 446','좌천동(佐川洞) 이라는 이름은『동래부지(1740)』에 나오는 좌자천(佐自川) 이라는 이름의 약칭이다. 좌자천은 가야산 및 감고개에서 시작되어 지금의 수정동의 중앙을 거쳐 부산진 동쪽을 돌아서 바다로 들어가는 작은 개천을 말한다'),(117,'범일','범일','Beomil','051-678-6117','부산광역시 동구 범일로 지하 108','범일동(凡一洞)은 동구 범6동에서 범4동으로 이어진 계곡 주위로 숲이 우거져 있는 그 계곡의 내를 범내라 했다. 그 범내 주위로 마을이 형성되자 범천1리 범천2리라 했는데 일제강점 이후 범천1리와 범천2리가 병합될 때 범천1리의 약칭인 범일동(凡一洞)을 동명으로 삼았다.'),(118,'범내골','범내골','Beomnaegol','051-678-6118','부산광역시 부산진구 중앙대로 지하 612','호랑이가 이 계곡에서 자주 출몰하였다고 하여 붙여진 명칭  즉 호랑이를 뜻하는 범(虎) 시내를 뜻하는 내(川) 골짜기를 뜻하는 골(谷)으로 이루어졌다. 오늘날은 범천이라 부르고 있는데 이는 호랑이를 뜻하는 범이라는 음을 한자에서 빌려 표기하였기 때문이다. '),(119,'서면(1)','서면','Seomyeon','051-678-6119','부산광역시 부산진구 중앙대로 지하 730','서면이라는 명칭은 본래 조선시대 동래군에 속하는 면이었다. 1904년 간행된『경상도동래군가호안』에는 서면이 서상면과 서하면으로 나누어져 있다현재 서면이라 불리는 지역은 서하면의 부전리 일대로서 서상면서하면의 중심지였던 것으로 보인다. '),(120,'부전','부전(부산시민공원·송상현광장)','Bujeon','051-678-6120','부산광역시 부산진구 중앙대로 지하 786','부전동(釜田洞)은 조선시대의 동래부 동평면 부현리(釜峴里)에 속하였다. 공식적인 명칭으로 사용된 것은 1936년 시·구명 정비 때 부전동이란 이름이 쓰여지게 되다.'),(121,'양정','양정','Yangjeong','051-678-6121','부산광역시 부산진구 중앙대로 지하 930','양정동은『동래부지(1740)』에는 양정리(羊亭里) 라 하였다. 양정(羊亭)이란 정자는 고적조나루정(樓亭)조에 이름이 보이지 않는 것으로 보아 정자(亭子)가 존재하지 않은 것으로 파악된다. 이 지역의 고로들에 의하면 양정본동 일대에는 수양버들의 실같은 가지가 바람에 하늘거리는 모습이 눈에  많이 띄었다고 하는데 그래서 이곳을 버들 양(楊)으로 개칭한 것이 아닌가 한다.'),(122,'시청','시청(연제)','City Hall','051-678-6122','부산광역시 연제구 중앙대로 지하 1017','연제구는 구석기 청동기 철기(삼한)시대를 거쳐 거칠산국이나 장산국에 소속되었다가 통일신라 경덕왕(742∼765) 때 부산지역이 \"동래(東萊)\"\"군으로 개명됨에 동래군에 소속된다. 고려시대는 동래현이었고 조선시대는 동래부였다. 동래부 아래의 서면에 대조리 거벌리가 연제구의 전신이 되었다. 이후 조선초 15세기에 일본에게 3포를 개항할 때 항구명은 부산포(富山浦 후에 釜山浦)였다. 이 부산이란 지명이 부각되다가 1910년 일본이 우리나라 국권을 탈취하면서 부산부란 행정구역이 동래 대신 부산을 대표하게 되었다. 1942년 10월 1일 부산부 아래 동래출장소가 있었고 대한민국 제1공화국시대인 1957년 1월 1일 동래구로 승격하여 거제동과 연산동이 동래구에 속하게 된다. 이때 연산리 거제리의 지명이 독립되고 1946년∼1985년까지 거제동의 4개동 연산동의 9개동이 탄생된다. 1995년 3월 1일로 동래구에서 연제구가 분구되어 오늘에 이르고 있다. 연산동의『연(蓮)』과 거제동의『제(堤)』를 따서 연제구(蓮堤區)라는 구의 명칭이 제정되었다.\"'),(123,'연산(1)','연산','Yeonsan','051-678-6123','부산광역시 연제구 중앙대로 지하 1101','연산동(蓮山洞)이란 지명은 낮은 늪지대로 수련이 많고 배산과 황령산쪽은 산지로 되어 연산이란 이름이 붙여졌다는 설과 이 동네의 시발은 금련산(金蓮山)이어서 연산(蓮山)이라 했다는 설이 있다.'),(124,'교대','교대','Busan Natl Univ. Edu.','051-678-6124','부산광역시 연제구 중앙대로 지하 1217','부산교육대학교는 연제구 거제1동에 있으며 역사위치가 본대학 동편에 설치함에 따라 역명을 교대라고 명명하였음'),(125,'동래(1)','동래','Dongnae','051-678-6125','부산광역시 동래구 중앙대로 1324','《삼국지(三國志)》위지(魏志) 동이전(東夷傳) 변진(弁辰) 조에는 삼한시대 24개의 국명 중에 독로국(瀆盧國)이 기록되어 있는데 이를 동래라는 설도 있다. 따라서 동래는 독로 음에서 독로 → 동네 → 동래로 음전되어 불리어지게 되었다고 볼 수 있는데 이는 통일신라 경덕왕 16년(757)에 지방행정제도를 개편할 때 지방명을 모두 중국식 한자음으로 고침에 따라 동래라는 이름을 가지게 되었다'),(126,'명륜','명륜','Myeongnyun','051-678-6126','부산광역시 동래구 중앙대로 1414','명륜동(明倫洞)은『동래부지(1740)』의 방리조에 보면 신향교동(新鄕校洞)이라 하였다. 조선시대는 고을마다 향교가 있어 그 향교가 있는 마을을 교동(校洞) 또는 교리(校里)라 하는 경우가 많았다.'),(127,'온천장','온천장','Oncheonjang','051-678-6127','부산광역시 동래구 중앙대로 1520','온천동(溫泉洞)의 유래가 된 동래온천장에서 온천이 자연용출 한 시기는 신라시대부터로 본다. 그러나 산저리(속칭 차밭골)와 장전리 일부를 합하여 행정구역상의 온천동(溫泉洞)으로 독립시킨 것은 1910년일제강점 이후가 된다'),(128,'부산대','부산대','Pusan Natl Univ','051-678-6128','부산광역시 금정구 장전온천천로 48','부산대학교의 소재지는 금정구 장전동에 있으며 이 대학 동편에 정거장을 설치함에 따라 정거장이름을 부산대역이라고 제정'),(129,'장전','장전(부산가톨릭대학교)','Jangjeon','051-678-6129','부산광역시 금정구 장전온천천로 144','장전동(長箭洞)은『동래부지(1740)』는 물론 이후 모든 읍지에도 북면 장전리(長箭里)로 기록되어 있는 것으로 보아 동(洞)의 형성은 일찍부터 이루어졌음을 알 수 있다. 1952년 上里인 장전마을과 下里인 소정마을을 합하여 장전동이라 하였다. 장전(長箭) 유래는 긴 화살이라는 뜻으로 금정산의 선안 죽전마을과 같이 화살대를 만드는 대나무가 많이 생산되어 붙여진 이름이라 한다.'),(130,'구서','구서','Guseo','051-678-6130','부산광역시 금정구 금정로 233번길 46','구서동(久瑞洞)은『동래부지(1740)』의 방리조에 보면 구세리(仇世里)라 기록되어 있다. 대한제국시기 구세리와 두실리의 두 개 자연마을로 편성되었다. 1914년 행정구역 개편 때 구서(九瑞)·두실(斗實)·금단(琴端)의 3개 자연마을을 합하여 구서리라 칭하였고 동래군 북면에 속하게 되었다.『동래군지(1937) 』에는 구서리(九瑞里)란 명칭으로 기록되어 있다.'),(131,'두실','두실','Dusil','051-678-6131','부산광역시 금정구 중앙대로 지하 1927-1','구서동(久瑞洞)은『동래부지(1740)』의 방리조에 보면 구세리(仇世里)라 기록되어 있다. 대한제국시기 구세리와 두실리의 두 개 자연마을로 편성되었다. 1914년 행정구역 개편 때 구서(九瑞)·두실(斗實)·금단(琴端)의 3개 자연마을을 합하여 구서리라 칭함'),(132,'남산','남산(부산외국대학교)','Namsan','051-678-6132','부산광역시 금정구 중앙대로 지하 2019-1','남산동(南山洞)의 명칭은 조선시대부터 오늘날까지 줄곧 쓰여진 이름이다. 『동래부지(1740)』방리조에도 동래부 북면에 남산리라 하여 부 관문에서 북으로 18리에 있다고 하였고『동래부읍지(1832)』 『동래군지(1937)』에도 북면의 남산리로 기록하고 있었다. 남산동은 남산·남중(南中)·신암(新岩)의 3개 자연마을이 있으며 남산마을 조금 떨어져 작은 마을로 반남산(半南山) 마을이 있다. 이중 가장 취락이 먼저 발달한 곳이 남산마을로 지세는 북이 높고 남쪽이 낮아 집을 지으면 모두 남쪽으로 향하여 남산이라 하였다 한다. 한편 남산동은 범어사의 사전(寺田)이 많아 범어사에서 볼 때 남쪽 산등성이라 하여 남산동이라고 불렀다고 한다.'),(133,'범어사','범어사','Beomeosa','051-678-6133','부산광역시 금정구 중앙대로 지하 2107','<범어사 창건사적>에 따르면 이 절은 왜구를 막기 위해 창건되었다고 한다. 835년(신라 흥덕왕 10년) 동쪽 해안에 왜인이 10만 병선을 거느리고 나타나 신라를 침략하려고 하여 왕이 근심하고 있을 때 꿈속에 신인(神人)이 나타나서, \"태백산맥에 의상(義湘)이라는 스님이 계시는데 항상 성중 1천'),(134,'노포','노포(종합버스터미널)','Nopo','051-678-6134','부산광역시 금정구 중앙대로 2238','노포동(老圃洞)은『동래부지(1740)』의 기록에 의하면 북면 작장리(鵲掌里)와 소산리(蘇山里)에 해당하는 지역이다. 노포라는 지명은 농사를 잘 짓는 농부 또는 농사에 경험이 많은 사람으로 늙은 농부를 뜻하는데 노포동이란 농사가 잘되는 마을 다른 곳에 비하여 농토가 풍부한 마을이라는데서 붙여진 이름으로 보인다.'),(201,'장산','장산(해운대백병원)','Jangsan','051-678-6201','부산광역시 해운대구 해운대로 지하 820','가장 높은 산이란 뜻이며 현 역세권의 좌동은 장산의 남쪽사면의 평야를 낀 지대로서 장산의 주인 동네임.'),(202,'중동','중동','Jung-dong','051-678-6202','부산광역시 해운대구 해운대로 지하 730','해운대 지구의 중심부이며 좌우에 좌동 및 우동이 있음.  행정동명에 따라 중동이라 명명함'),(203,'해운대','해운대','Haeundae','051-678-6203','부산광역시 해운대구 해운대로 지하 626','유학자인 최치원이 동백섬 일대의 절경에 심취하여 동백섬 남쪽의 암벽에 자신의 호인 해운을 따서 해운대라는 글자를 새긴 것에서 유래.'),(204,'동백','동백','Dongbaek','051-678-6204','부산광역시 해운대구 해운대로 지하 522','동백 두송 송삼등이 울창하고 시민의 휴식처인 동백섬에서 유래.'),(205,'벡스코','벡스코(시립미술관)','Busan Museum of Art','051-678-6205','부산광역시 해운대구 해운대로 지하 396','현 역세권에 가장 뚜렷한 지형지물이고 부산시민의 미술저변확대와 미술관을 찾는 내ㆍ외 관람객들의 교통 편의도모와 미술관의 대외 홍보하기 위해 시립미술관이라고 표기함.'),(206,'센텀시티','센텀시티(BEXCO·신세계)','Centum City','051-678-6206','부산광역시 해운대구 센텀남대로 지하 76','21세기 정보화 사회의 중추적 역할을 담당할 첨단 정보산업단지가 들어설 예정이고 역사가 컨벤션센터에 위치하여 역명을 센텀시티라 하게되면 대내외적으로 지대한 홍보효과를 가져올 수 있음.'),(207,'민락','민락','Millak','051-678-6207','부산광역시 수영구 수영로 지하 769','수영의 진산 앞의 마을로 수영강의 어귀를 접한 놀이터인 까닭에 여러 사람이 함께 즐길 수 있는 경치라는 데서 붙임. (여민동락)'),(208,'수영(2)','수영','Suyeong','051-678-6208','부산광역시 수영구 수영로 지하 677','조선시대 경상 좌도수군 절도사영이 있어서 관아명을 줄여 좌수영이라 하며 조선시대 수군제가 확립된 후 주둔하였던 군대명칭으로서 경상 좌도수군 절도사영에서 수자와 영자를 따와서 이미 지명으로 굳어졌음'),(209,'광안','광안','Gwangan','051-678-6209','부산광역시 수영구 수영로 지하 576','해안과 모래벌을 가진 곳으로 넓은 해안이란 뜻의 廣岸이라 이름 짓는 것이 옳으나 풍수상 광안이라 하였음.'),(210,'금련산','금련산','Geumnyeonsan','051-678-6210','부산광역시 수영구 수영로 지하 482','당초 황령산 야영장의 명칭이 부산시 조례개정으로 청소년 수련소로 개칭되었고 황령산과는 거리가 멀어 의미가 없으며 정거장이 건설되는 지점이 금련산 자락이며 금련산은 수영구의 진산임.'),(211,'남천','남천(KBS·수영구청)','Namcheon','051-678-6211','부산광역시 수영구 수영로 지하 410','대연동의 석포에서 융기된 산지의 북안쪽을 남천 (동래부지도) 금련산에서 발원하여 수영만으로 흐르는 시내를 남천이라 부름.'),(212,'경성대·부경대','경성대·부경대(동명대학교)','Kyungsung Univ.ㆍPukyong Natl Univ','051-678-6212','부산광역시 남구 수영로 지하 324','현 역세권에 가장 뚜렷한 지형지물임.'),(213,'대연','대연(고려병원)','Daeyeon','051-678-6213','부산광역시 남구 수영로 지하 242','황령산의 북서는 준험하고 동남은 밋밋한 연봉이 10여개 남으로 뻗어내려 수많은 浦와 池를 이름 특히 이 일대에 큰 연못이 있어서 한자표기로 大淵이라 함.'),(214,'못골','못골(남구청)','Motgol','051-678-6214','부산광역시 남구 수영로 지하 170','황령산의 주봉인 관창봉 아래 큰 못 작은 못이 있었는데 이런 연유로  못골이라 불렀음.'),(215,'지게골','지게골','Jigegol','051-678-6215','부산광역시 남구 수영로 지하 70','지게는 마루나 바깥에서 방으로 드나드는 곳에 문종이로 안 밖을 두껍게 싸서 바른 외짝문이란 뜻으로 이 일대의 지형은 양편이 산으로 에워싸여 있어 마치 집안의 방으로 들어가는 문과 같기 때문에 옛날로부터 찌게골로 불리워 왔다. (찌게골 → 지게골)'),(216,'문현','문현','Munhyeon','051-678-6216','부산광역시 남구 전포대로 지하 17','지게골의 한문표기로서 지게에서 門을 고개에서 峴을 따옴.'),(217,'국제금융센터·부산은행','국제금융센터·부산은행','Busan Intl Finance Center·Busan Bank','051-678-6217','부산광역시 남구 전포대로 지하 97','인근의 국제금융센터와 부산은행 명칭을 따서 만듦'),(218,'전포','전포','Jeonpo','051-678-6218','부산광역시 부산진구 전포대로 지하 181','옛날에는 황령산 아래 산자락 마을이 있었는데 논밭과 갯가로 되어 있어 밭개로 불리었고 이의 한자 표현이 田浦임.'),(219,'서면(2)','서면','Seomyeon','051-678-6219','부산광역시 부산진구 중앙대로 지하 730','옛 동래군의 서쪽에 위치하는 면.'),(220,'부암','부암(온종합병원)','Buam','051-678-6220','부산광역시 부산진구 가야대로 지하 719','지금의 부암동과 부전동 사이에 가마솥(釜)을 거꾸로 엎어 놓은 것 같은 형상의 바위가 있었다는데서 유래.'),(221,'가야','가야','Gaya','051-678-6221','부산광역시 부산진구 가야대로 지하 650','가야는 갑우내를 한자로 표기한 것이며 갑우는 정중(正中)의 뜻으로 지금의 가운의 원말. 지금의 구관으로부터 감고개(&#26617;嶺) 가모고개 가마고개를 넘어 가야동으로 왕래하여 이곳(가야)은 교통의 요충지이며 가야리란 명칭은 감고개 아래의 마을이란 뜻이 있음.'),(222,'동의대','동의대','Dongeui Univ','051-678-6222','부산광역시 부산진구 가야대로 지하 554','현 역세권에 가장 뚜렷한 지형지물임.'),(223,'개금','개금','Gaegeum','051-678-6223','부산광역시 부산진구 가야대로 지하 442','이 마을의 모양이 꼭 거문고와 같이 길게 늘어져 있는 현상이라 개금이라 하였음.'),(224,'냉정','냉정','Naengjeong','051-678-6224','부산광역시 사상구 가야대로 지하 362-1','가야에서 주례동으로 넘어오는 고개밑에 천하에 청량미를 자랑하는 맑은 물이 솟는 샘에서 유래하며 이고개 이름을 냉정치라고 부르고 부락이름도 냉정동 이라함.'),(225,'주례','주례','Jurye','051-678-6225','부산광역시 사상구 가야대로 지하 292','주례로 기사(記寫)된 말의 어원은 바로 두리에서 왔을 것임.  (두리 → 두례 → 주례)'),(226,'감전','감전(사상구청)','Gamjeon','051-678-6226','부산광역시 사상구 사상로 지하 93-1','甘東부락 = 신(神)의 마을에서 유래. 농토가 비옥하다는 뜻의 甘田.'),(227,'사상','사상(서부터미널)','Sasang','051-678-6227','부산광역시 사상구 사상로 지하 203','옛 사천면 상당(沙川面 上端)의 줄임말.'),(228,'덕포','덕포','Deokpo','051-678-6228','부산광역시 사상구 사상로 지하 320-1','덕포의 옛이름이 덕개였으며 덕개의 위치는 낙동강을 향하여 길게 뻗어 나온 긴 동산이 있는데 여기에는 상강선대 하강선대가 있고 이 강선대의 중간 도로변에 있는 바위언덕이 그것이다. 이 언덕이 동리의 포구였고 여기에서 동리명인 덕포동이 된 것임.'),(229,'모덕','모덕','Modeok','051-678-6229','부산광역시 사상구 사상로 지하 409','덕포2동과 모라1동의 경계지점이고 현재 모덕초등교 모덕시장 등의 명칭이 통용되고 있음.'),(230,'모라','모라','Mora','051-678-6230','부산광역시 사상구 사상로 지하 498','마을(집회소)이라는 우리말의 고대어임.'),(231,'구남','구남','Gunam','051-678-6231','부산광역시 북구 백양대로 지하 1026','구포 남쪽의 자연부락.'),(232,'구명','구명','Gumyeong','051-678-6232','부산광역시 북구 백양대로 지하 1094','주변지역 일대가 구명리라는 자연부락으로 주민등록법 시행이전의 기류초본에도 구명동으로 표기되어 있으며 인근의 구포초등학교 전신인 구포사립구명학교가 1906년 교육계의 선각자들에 의해 창설되어 이듬해인 1907년 10월 15일에 개교되었음.'),(233,'덕천(2)','덕천(부산과기대)','Deokcheon','051-678-6233','부산광역시 북구 금곡대로 지하 14','덕천동의 옛이름인 덕곡촌의 마을에 흐르는 시내로서 금정산에서 발원하여 낙동강으로 유입하는 천을 덕천이라 불리움.'),(234,'수정','수정(방송통신대)','Sujeong','051-678-6234','부산광역시 북구 금곡대로 지하 160','수정마을은 구포 왜성 바로 밑에 위치하므로 이곳에 수정(戍亭)이 설치되어 붙은 이름일 것임.'),(235,'화명','화명','Hwamyeong','051-678-6235','부산광역시 북구 금곡대로 지하 311','회붉이(日明)에서 온 것으로서 즉 “해”가 “화”가 되고 “붉”이“명”이 되었을 것으로 사료됨.'),(236,'율리','율리','Yulli','051-678-6236','부산광역시 북구 금곡대로 지하 440','밤 즉 밝은 곳이란 뜻이니 예를 들면 “밤개울” “붉개울”은 율포를 말하는 것이고 신하(神河)의 고어이다.  또한 이 마을에 신석기 유적과 당산 그리고 바위에 새겨진 성혈이 모두 신과 관련된 것으로 율리는 그 뜻을 내포함.'),(237,'동원','동원','Dongwon','051-678-6237','부산광역시 북구 금곡대로 575','선 세조때 김해군 생림면에 있던 도요진을 금곡동의 동원동으로 옮겨와 세곡수송의 수참 및 왜인들과 무역하는 나루로 사용하였으며 현재도 금곡동 장어마을 일대가 동원부락으로 불려지고 있음.'),(238,'금곡','금곡','Geumgok','051-678-6238','부산광역시 북구 금곡대로 685','금정산의 골에서 유래.'),(239,'호포','호포','Hopo','051-678-6239','경상남도 양산시 동면 양산대로 62','옛이름은 호포(狐浦)이며 낙동강변 포구의 자연부락명임.'),(240,'증산','증산','Jeungsan','051-678-6240','경상남도 양산시 물금읍 메기로 168','-'),(241,'부산대양산캠퍼스','부산대양산캠퍼스','Pusan Natl Univ. Yangsan Campus','051-678-6241','경상남도 양산시 물금읍 메기로 270','-'),(242,'남양산','남양산(범어)','Namyangsan','051-678-6242','경상남도 양산시 동면 메기로 380','-'),(243,'양산','양산(시청·동원과학기술대학교)','Yangsan','051-678-6243','경상남도 양산시 강변로 441','양주(良州)는 고려 태조 23년 경자에 양주(梁州)로 개칭되고 현종 무오년에 방어사를 두었는데 조선태종 13년 계사에 류수부 대도호부 목관을 제외한 “주”자를 가진 단부 및 군연은 모두 “산과 천”으로 고쳐짐에 따라 양산으로 개칭되어 오늘에 이르고 있다'),(301,'수영(3)','수영','Suyeong','051-678-6301','부산광역시 수영구 수영로 지하 677','조선시대 경상 좌도수군 절도사영이 있어서 관아명을 줄여 좌수영이라 하며 조선시대 수군제가 확립된 후 주둔하였던 군대명칭으로서 경상 좌도수군 절도사영에서 수자와 영자를 따와서 이미 지명으로 굳어졌음'),(302,'망미','망미(병무청)','Mangmi','051-678-6302','부산광역시 수영구 연수로 지하 337','고려시대 충신 정서가 이곳에서 귀양살이 하면서 초하루와 보름날에 북쪽을바라보며(望) 임금(美)을 향하여 절을 했다는 뜻에서 망미동이라는 명칭이유래.'),(303,'배산','배산','Baesan','051-678-6303','부산광역시 연제구 연수로 지하 229','망미1동의 뒷산인 배산에 거칠산국(신라의 변방에 위치한 속국)의 유적으로 추정되는 배산성지가 있으며 이 지역이 거칠산국의 중심지로 추정됨.'),(304,'물만골','물만골','Mulmangol','051-678-6304','부산광역시 연제구 월드컵대로 지하 23','황령산 북쪽자락으로 물이 많은 골짜기라는 뜻으로 옛날 전리(田里)에 속한작은 마을 지명으로 가뭄에도 물이 마르지 않는다는 뜻이 있고 지금도 널리 쓰이고 있음. 전리는 밭이 많은 동네란 뜻으로 금련산 골짜기에서 흘러 내리는 중앙천 쌍미천 마곡천의 수자원이 풍부'),(305,'연산(3)','연산','Yeonsan','051-678-6305','부산광역시 연제구 중앙대로 지하 1101','연산동(蓮山洞)이란 지명은 낮은 늪지대로 수련이 많고 배산과 황령산쪽은 산지로 되어 연산이란 이름이 붙여졌다는 설과 이 동네의 시발은 금련산(金蓮山)이어서 연산(蓮山)이라 했다는 설이 있다.'),(306,'거제','거제(법원·검찰청)','Geoje','051-678-6306','부산광역시 연제구 월드컵대로 지하 209','조선시대 서면에 속하며 거벌(巨伐)로 표기되어 연산동 및 거제동 일대의 넓은 들을 의미하였으나 일제시대 동래천에 제방을 쌓으면서 큰제방이 있는 마을이라는 뜻에서 거제(巨堤)로 불림.'),(307,'종합운동장','종합운동장','Sports Complex','051-678-6307','부산광역시 연제구 아시아드대로 지하 73','조선중기 동래부 서면 거벌리로 불리다가 거평동으로 불려졌으며 2002년 아시안게임 주경기장(종합운동장)이 위치하여 종합운동장으로 명명함.'),(308,'사직','사직','Sajik','051-678-6308','부산광역시 동래구 아시아드대로 지하 153','예부터 사직단이 있던 곳으로 社는 토지신이고 稷은 곡물신으로써 임금을 비롯한 지방수령이 토지신과 곡물신에게 제사를 드려 나라와 지방의 풍요와 안녕을 비는 곳이 사직단이며 1914년 석사동 거인동을 병합해 여고동이라하여 동래군 동래면에 편입되었는데 1916년 사직'),(309,'미남(3)','미남','Minam','051-678-6309','부산광역시 동래구 아시아드대로 지하 232','예로부터 내려오는 자연마을로 자식이 성년이 되는 날 막걸리 1말을 대접하는 풍습이 내려옴. 예부터 미남 마을이 존재하였고 미남교차로 등 여건을 고려하여 미남이라 명명함.'),(310,'만덕','만덕','Mandeok','051-678-6310','부산광역시 북구 만덕대로 지하 291','임진왜란때 금정산 기슭인 이곳에 1만여의 피난민이 피난와서 모두 화를 면했었는데 이에 따라 1만여명이 덕을 입었다고 하여 마을이름이 만덕동이되었다고 한다. 그러나 <고려사절요> 권26을 보면 충혜왕의 서자 석기의 머리를 깍고 만덕사에 두었다라고 한다. '),(311,'남산정','남산정(부산폴리텍대학)','Namsanjeong','051-678-6311','부산광역시 북구 만덕대로 지하 179','덕천동의 본 마을에 해당하는 자연 발생적 마을로서 정확한 유래는 알 수 없으나 구포왜성(의성)과 관련된 명칭에서 유래한 것으로 추정되며 정자(당산) 나무가 있어 붙여진 자연마을 지명에 따라 남산정이라 명명함. '),(312,'숙등','숙등(부민병원)','Sukdeung','051-678-6312','부산광역시 북구 만덕대로 지하 79','숙등마을의 유래는 여러 가지 설이 있으나 그 중 대표적인 것은 구포장에서 만덕고개를 넘어 동래장으로 향하는 길목으로 임진왜란 후 수정(戍亭)이 있었던 곳으로 볼 때 수정이 변하여 숙등으로 되었다고 보는 설이 있음.'),(313,'덕천(3)','덕천(부산과기대)','Deokcheon','051-678-6313','부산광역시 북구 금곡대로 지하 14','덕천동의 옛이름인 덕곡촌의 마을에 흐르는 시내로서 금정산에서 발원하여낙동강으로 유입하는 천을 덕천이라 부름.'),(314,'구포','구포','Gupo','051-678-6314','부산광역시 북구 낙동대로 1697','포의 구(龜)에 대한 학설중에서 정인보의 설을 보면 구포라는 말은 ‘거뵈개’를 한자로 적은 말이고 ‘거뵈개’는 낙동강 물 이름인 ‘갑우내’에서 왔다는 것이며 ‘구’를 신(神)으로 해석하는 설이 있음'),(315,'강서구청','강서구청','Gangseo-gu Office','051-678-6315','부산광역시 강서구 낙동북로 485','현재 대저 12동이 위치하고 있는 대저섬(삼각주)은 동서로 6Km 남북으로 15Km에 이르는 큰 섬이며. 조선시대 문헌자료에 의하면 노전(蘆田)을 비롯한 전답에 관한 기록과 농토를 보호하기 위한 제방축조의 기록이 있다. 인근에 강서구청이 있으므로 강서구청이라 명명함.'),(316,'체육공원','체육공원','Sports Park','051-678-6316','부산광역시 강서구 낙동북로 371','홍수 때마다 강물이 범람하여 물길이 한곳으로 세차게 맴돌며 모래를  쓸어버려 큰못을 이루었는데 이 못가에 정자를 짓게 되어 연정이라 불리었으며 정자의 동쪽은 동연정이라 하고 서쪽은 서연정이라 함. 하키경기장 양궁경기장 등 종합시설을 이용하는 시민들에게 친숙한'),(317,'대저','대저','Daejeo','051-678-6317','부산광역시 강서구 낙동북로 295','대저섬(삼각주)은 동서로 6Km 남북으로 15Km에 이르는 큰 섬으로 서낙동강 어귀에 큰 모래톱이 형성되어 대저라는 지명이 유래.'),(401,'미남(4)','미남','Minam','051-678-6401','부산광역시 동래구 아시아드대로 지하 232','○1832년 동래부읍지 방리조에 서면소속 미남리라 함 ○1904년 경상남도동래군가호안에 서상면관내에 미남리 존재 ○온천3동 파출소 동쪽편이 미남본동이라 함'),(402,'동래(4)','동래','Dongnae','051-678-6402','부산광역시 동래구 충렬대로 지하 147','○온천동의 개발은 일제 이후임(이전에는 온정원(溫井院)이라는 관리들을 위한 관용 여관 존재)  ○1914년 산저리 미남동 화촌동 소정동 합해 온천동으로 함 ○1942년 부산부 동래출장소 설치로 온천동 속함 1947년 일제식 동명 개정 때 미남리 산저리 일부 합쳐 온천2'),(403,'수안','수안','Suan','051-678-6403','부산광역시 동래구 충렬대로 지하 223','○1914년 평남 안민 장남 안국 서호등을 합하여 수안동 됨 ○1957년 법정명인 수안동과 낙민동이 수민동으로 병합 ○수안의 뜻은 首安(동부래 수장인 동래부사가 집무하는 동헌이 있어 으뜸되는 관아 안) 또는 水安(물이 많은 지역)의 의미가 있음'),(404,'낙민','낙민','Nangmin','051-678-6404','부산광역시 동래구 충렬대로 지하 285','1914년 신락 회룡동 병합하여 낙민동 됨  낙민동 지역은 수령이 민정 살피는 지역으로 수령이 백성을 즐겁게 해준다는 뜻'),(405,'충렬사','충렬사(안락)','Chungnyeolsa','051-678-6405','부산광역시 동래구 반송로 지하 205','○충렬사리 안락리 호현 화현 합해 원리(서원 있는 마을)라 함 ○1942년 서원의 명칭인 안락을 따서 안락정 ○1957년 안락동 1982년 안락1 2동 분동'),(406,'명장','명장','Myeongjang','051-678-6406','부산광역시 동래구 반송로 지하 281','○1740년 동래부 동면 명장리 표기 1910년 동래읍 소속 1959년 동래구 명장동 1990년 명장12동 분동 ○명편(의장때 쓰는 기구로 흔들어 소리내어 정숙케 하는 물건)을 보관했던 곳이라 하여 명장이라 전함'),(407,'서동','서동','Seo-dong','051-678-6407','부산광역시 금정구 반송로 지하 387','○1832년 명장리 서리 금사리 반여리 회동리 등을 동상면 우리 중리 좌리 남수리 등은 동하면이라 함 ○1942년 동래군의 부산부 편입으로 동상면의 중심마을인 서리 금사리 회동리 합하여 서동이 됨 ○1959년 서동을 동상동으로 개칭 1975년 동상123동으로 분'),(408,'금사','금사','Geumsa','051-678-6408','부산광역시 금정구 반송로 지하 465','○조선시대 동상면 지역 ○1914년 금천마을과 사천마을 첫글자 합하여 금사리됨 ○1942년 부산부에 편입 1957년 동래구 소속 ○광복후에도 법정동으로 존재하였으나 행정동으로는 서동에 속하였고 1985년 서3동이 분동되면서 금사동으로 발족'),(409,'반여농산물시장','반여농산물시장','Banyeo Agricultural Market','051-678-6409','부산광역시 해운대구 반송로 550','○지형이 소반처럼 동그랗다는 뜻에서 유래 ○조선시대 동래군 동상면 지역 ○1896년 부산부 편입 1914년 동래군 동래면 반여리 1942년 부산부 재편입 1957년 동래구 1980년 해운대구 관할 (행정동 반여1~4동으로 구성)'),(410,'석대','석대','Seokdae','051-678-6410','부산광역시 해운대구 석대천로 121','조선시대부터 사용 연원은 불명(주변에 지명과 관련된 흔적 없음)이나 동천의 상류로서 주변에 오륜대 동대 죽연대 등의 높은대가 많은 것으로 보아 석대동 일원에도 풍류를 즐길만한 좋은 자리가 있는 데서 지명유래 추측'),(411,'영산대','영산대(아랫반송)','Youngsan Univ','051-678-6411','부산광역시 해운대구 반송로 803','○ 조선시대부터 사용 연원은 불명(주변에 지명과 관련된 흔적 없음)이나 동천의 상류로서 주변에 오륜대 동대 죽연대 등의 높은대가 많은 것으로 보아 석대동 일원에도 풍류를 즐길만한 좋은 자리가 있는 데서 지명유래 추측'),(412,'윗반송','윗반송','Witbansong','051-678-6412','부산광역시 해운대구 반송로 917','○조선시대부터 사용 연원은 불명(주변에 지명과 관련된 흔적 없음)이나 동천의 상류로서 주변에 오륜대 동대 죽연대 등의 높은대가 많은 것으로 보아 석대동 일원에도 풍류를 즐길만한 좋은 자리가 있는 데서 지명유래 추측'),(413,'고촌','고촌','Gochon','051-678-6413','부산광역시 기장군 철마면 반송로 991','○옛이름은 돋골로서 범곡이라 함 이는 돛골로 돛은 배의 돛대가 아닌 돋골 즉 돋은 골의 준말임 돋은 골은 언덕골로 구곡이라는 뜻 돋골을 돛골로 알고 한역하여 범곡(帆谷)이라함. 고촌은 오래된 마을 뜻외 돋골마을의 본마을 큰마을이라는 뜻'),(414,'안평','안평(고촌주택단지)','Anpyeong','051-678-6414','부산광역시 기장군 철마면 반송로 1101','○1914년 기장군 상서면 안평동 일부와 원동면 만화동 일부가 합쳐 동래군 철마면 안평리 되었고 ○1973년 양산군에 속했다가 1995년 부산광역시로 편입되어 기장군 철마면 안평리 됨');
/*!40000 ALTER TABLE `stations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-28  0:53:44
