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
-- Table structure for table `platform`
--

DROP TABLE IF EXISTS `platform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platform` (
  `LineNum` text COLLATE utf8mb3_unicode_ci,
  `StationName` text COLLATE utf8mb3_unicode_ci,
  `StationName(plus)` text COLLATE utf8mb3_unicode_ci,
  `AboveUnder` text COLLATE utf8mb3_unicode_ci,
  `Floor` int DEFAULT NULL,
  `Connection` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platform`
--

LOCK TABLES `platform` WRITE;
/*!40000 ALTER TABLE `platform` DISABLE KEYS */;
INSERT INTO `platform` VALUES ('1호선','괴정','괴정','지하',2,1),('1호선','교대','교대','지하',2,1),('1호선','구서','구서','지상',2,0),('1호선','남산','남산(부산외국대학교)','지하',2,0),('1호선','남포','남포','지하',2,0),('1호선','낫개','낫개','지하',3,0),('1호선','노포','노포(종합버스터미널)','지상',2,0),('1호선','다대포항','다대포항','지하',2,0),('1호선','다대포해수욕장','다대포해수욕장','지하',2,1),('1호선','당리','당리(사하구청)','지하',2,0),('1호선','대티','대티(동주대학)','지하',5,1),('1호선','동대신','동대신','지하',2,0),('1호선','동래(1)','동래','지상',2,1),('1호선','동매','동매','지하',2,0),('1호선','두실','두실','지하',2,0),('1호선','명륜','명륜','지상',2,0),('1호선','범내골','범내골','지하',2,1),('1호선','범어사','범어사','지하',3,0),('1호선','범일','범일','지하',2,0),('1호선','부산대','부산대','지상',2,0),('1호선','부산역','부산','지하',2,0),('1호선','부산진','부산진','지하',2,1),('1호선','부전','부전(부산시민공원·송상현광장)','지하',2,0),('1호선','사하','사하','지하',2,0),('1호선','서대신','서대신','지하',4,1),('1호선','서면(1)','서면','지하',2,1),('1호선','시청','시청(연제)','지하',2,1),('1호선','신장림','신장림','지하',2,0),('1호선','신평','신평','지하',1,0),('1호선','양정','양정','지하',2,1),('1호선','연산(1)','연산','지하',2,1),('1호선','온천장','온천장','지상',2,0),('1호선','자갈치','자갈치','지하',2,0),('1호선','장림','장림','지하',2,0),('1호선','장전','장전(부산가톨릭대학교)','지상',2,0),('1호선','좌천','좌천','지하',2,0),('1호선','중앙','중앙','지하',2,1),('1호선','초량','초량','지하',2,0),('1호선','토성','토성','지하',2,0),('1호선','하단','하단(부산본병원)','지하',2,0),('2호선','가야','가야','지하',3,1),('2호선','감전','감전(사상구청)','지하',2,0),('2호선','개금','개금','지하',3,1),('2호선','경성대·부경대','경성대·부경대(동명대학교)','지하',3,1),('2호선','광안','광안','지하',3,1),('2호선','구남','구남','지하',3,0),('2호선','구명','구명','지하',3,0),('2호선','국제금융센터·부산은행','국제금융센터·부산은행','지하',2,1),('2호선','금곡','금곡','지상',2,0),('2호선','금련산','금련산','지하',4,1),('2호선','남양산','남양산(범어)','지상',3,1),('2호선','남천','남천(KBS·수영구청)','지하',3,1),('2호선','냉정','냉정','지하',2,0),('2호선','대연','대연(고려병원)','지하',3,1),('2호선','덕천(2)','덕천(부산과기대)','지하',2,1),('2호선','덕포','덕포','지하',2,0),('2호선','동백','동백','지하',2,0),('2호선','동원','동원','지상',1,1),('2호선','동의대','동의대','지하',4,1),('2호선','모덕','모덕','지하',2,0),('2호선','모라','모라','지하',2,0),('2호선','못골','못골(남구청)','지하',3,1),('2호선','문현','문현','지하',3,1),('2호선','민락','민락','지하',3,0),('2호선','벡스코','벡스코(시립미술관)','지하',2,0),('2호선','부산대양산캠퍼스','부산대양산캠퍼스','지상',1,1),('2호선','부암','부암(온종합병원)','지하',3,1),('2호선','사상','사상(서부터미널)','지하',2,0),('2호선','서면(2)','서면','지하',3,1),('2호선','센텀시티','센텀시티(BEXCO·신세계)','지하',2,0),('2호선','수영(2)','수영','지하',3,1),('2호선','수정','수정(방송통신대)','지하',2,0),('2호선','양산','양산(시청·동원과학기술대학교)','지상',3,1),('2호선','율리','율리','지하',2,0),('2호선','장산','장산(해운대백병원)','지하',2,1),('2호선','전포','전포','지하',3,1),('2호선','주례','주례','지하',2,0),('2호선','중동','중동','지하',2,0),('2호선','증산','증산','지상',2,0),('2호선','지게골','지게골','지하',4,1),('2호선','해운대','해운대','지하',2,1),('2호선','호포','호포','지상',5,1),('2호선','화명','화명','지하',2,0),('3호선','강서구청','강서구청','지상',5,0),('3호선','거제','거제(법원·검찰청)','지하',2,0),('3호선','구포','구포','지상',2,0),('3호선','남산정','남산정(부산폴리텍대학)','지하',2,0),('3호선','대저','대저','지상',3,1),('3호선','덕천(3)','덕천(부산과기대)','지하',3,1),('3호선','만덕','만덕','지하',9,1),('3호선','망미','망미(병무청)','지하',6,1),('3호선','물만골','물만골','지하',5,1),('3호선','미남(3)','미남','지하',3,1),('3호선','배산','배산','지하',8,1),('3호선','사직','사직','지하',2,0),('3호선','수영(3)','수영','지하',4,1),('3호선','숙등','숙등(부민병원)','지하',3,0),('3호선','연산(3)','연산','지하',4,1),('3호선','종합운동장','종합운동장','지하',3,1),('3호선','체육공원','체육공원','지상',4,1),('4호선','고촌','고촌','지상',2,1),('4호선','금사','금사','지하',3,1),('4호선','낙민','낙민','지하',3,1),('4호선','동래(4)','동래','지하',4,1),('4호선','명장','명장','지하',3,1),('4호선','미남(4)','미남','지하',3,1),('4호선','반여농산물시장','반여농산물시장','지상',1,1),('4호선','서동','서동','지하',3,1),('4호선','석대','석대','지상',2,1),('4호선','수안','수안','지하',3,1),('4호선','안평','안평(고촌주택단지)','지상',2,1),('4호선','영산대','영산대(아랫반송)','지상',2,1),('4호선','윗반송','윗반송','지상',2,1),('4호선','충렬사','충렬사(안락)','지하',3,1);
/*!40000 ALTER TABLE `platform` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-27  0:16:55
