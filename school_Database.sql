-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `Book_Id` int NOT NULL,
  `Book_Name` varchar(100) NOT NULL,
  `Book_Author` varchar(100) NOT NULL,
  `Book_Stock` int DEFAULT '0',
  `Book_Issued_Qty` int DEFAULT '0',
  PRIMARY KEY (`Book_Id`),
  CONSTRAINT `books_chk_1` CHECK ((`Book_Issued_Qty` <= `Book_Stock`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (124146,'The White Tiger','Aravind Adiga',10,2),(210212,'1984','George Orwell',60,0),(212142,'The Catcher in the Rye','J.D. Salinger',55,1),(323123,'The Great Gatsby','F. Scott Fitgerald',40,1),(564651,'Pride and Prejudice','Jane Austen',30,1),(584530,'A Suitable Boy','Vikram Seth',35,1),(656568,'The Hunger Games','Suzanne Collins',35,1),(678901,'To Kill a Mockingbird','Harper Lee ',50,0),(890123,'The Hobbit','J.R.R. Tolkein',45,1),(901234,'Train To Pakistan','Kushwant Singh',12,2);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `Emp_Id` int NOT NULL,
  `Emp_Name` varchar(50) NOT NULL,
  `Sex` char(1) DEFAULT NULL,
  `DOB` date NOT NULL,
  `Father_Name` varchar(50) NOT NULL,
  `Mother_Name` varchar(50) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Contact_Number` char(10) NOT NULL,
  `Join_Date` date DEFAULT NULL,
  `Duty` varchar(45) DEFAULT NULL,
  `Duty_Code` varchar(20) DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `password` char(20) NOT NULL,
  PRIMARY KEY (`Emp_Id`),
  CONSTRAINT `employee_chk_1` CHECK ((length(`Contact_Number`) = 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (102030,'Jai Prakash','M','1985-09-19','Lallan Prakash','Shivani Prakash','Gorakhnath,Groakhpur','9807424233','2016-07-16','Principal','P',19000,'Namaste@2023'),(125451,'Rohit Gupta','M','1986-02-18','Vikram Gupta','Seema Gupta','Maharajganj, Uttar Pradesh','9985200052','2015-07-13','Coordinator','E',17000,'secret#2020'),(212562,'Priyanka Sharma','F','1997-03-02','Golu Sharma','Vanshika Sharma','Mohaddipur,Gorakhpur','7876045221','2022-01-20','Teacher','E',28000,'TechStack$123'),(405060,'Aman Agarwal','M','1987-01-08','Sonu Agarwal','Shambhavi Agarwal','Lajpat Nagar,Delhi','8412352655','2023-04-19','Director','D',22000,'SQLDemo#Password'),(487452,'Nisha Patel','F','1997-05-08','Mahesh Patel','Neelam Patel','Deoria Road, Gorakhpur','9956236545','2016-11-05','Receptionist','E',25000,'qqww1122'),(515412,'Shreya Gupta','F','2000-12-05','Pankaj Gupta','Rohini Gupta','Betihata,Gorakhpur','8423452706','2018-12-05','Librarian','E',30000,'pass@123'),(546400,'Rajesh Kumar','M','1988-08-12','Ramesh Kumar','Sunita Kumari','Medical College Road, Gorakhpur','8400254895','2019-12-15','Teacher','E',18000,'aaron431'),(646566,'Rakesh Mehta','M','1999-06-15','Aman Mehtani','Shikha Mehtani','Civil Lines, Gorakhpur','9936352075','2020-09-30','Coordinator','E',25000,'google@dummy'),(853143,'Kavita Singh','F','2001-08-17','Vinod Singh','Poonam Singh','Kushinagar, Uttar Pradesh','8985400455','2014-02-15','Teacher','E',20000,'spark@fav@100'),(855223,'Ajay Sharma','M','1989-02-06','Gangesh Sharma','Priya Sharma','Golghar,Gorakhpur','8400644036','2023-06-15','Teacher','E',20000,'1q2w3e4r5t');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fee_details`
--

DROP TABLE IF EXISTS `fee_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fee_details` (
  `S_Id` int NOT NULL,
  `Qtr_I` varchar(45) DEFAULT 'NOT PAID',
  `Qtr_II` varchar(45) DEFAULT 'NOT PAID',
  `Qtr_III` varchar(45) DEFAULT 'NOT PAID',
  `Penalties` decimal(10,2) DEFAULT '0.00',
  UNIQUE KEY `S_Id_UNIQUE` (`S_Id`),
  KEY `FK_idx` (`S_Id`),
  CONSTRAINT `FK3` FOREIGN KEY (`S_Id`) REFERENCES `student` (`S_Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fee_details`
--

LOCK TABLES `fee_details` WRITE;
/*!40000 ALTER TABLE `fee_details` DISABLE KEYS */;
INSERT INTO `fee_details` VALUES (184545,'PAID','PAID','NOT PAID',50.00),(321315,'PAID','PAID','PAID',0.00),(489651,'PAID','NOT PAID','NOT PAID',0.00),(515049,'PAID','PAID','NOT PAID',50.00),(564623,'PAID','NOT PAID','NOT PAID',100.00),(585845,'PAID','PAID','PAID',0.00),(845422,'NOT PAID','NOT PAID','NOT PAID',150.00),(897454,'NOT PAID','NOT PAID','NOT PAID',0.00),(987541,'PAID','NOT PAID','NOT PAID',100.00),(987654,'PAID','PAID','PAID',0.00);
/*!40000 ALTER TABLE `fee_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issuedbookdetails`
--

DROP TABLE IF EXISTS `issuedbookdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issuedbookdetails` (
  `Book_Id` int NOT NULL,
  `S_Id` int NOT NULL,
  `Issue_Date` date NOT NULL,
  KEY `FK1_idx` (`Book_Id`),
  KEY `FK2_idx` (`S_Id`),
  CONSTRAINT `FK1` FOREIGN KEY (`Book_Id`) REFERENCES `books` (`Book_Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK2` FOREIGN KEY (`S_Id`) REFERENCES `student` (`S_Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issuedbookdetails`
--

LOCK TABLES `issuedbookdetails` WRITE;
/*!40000 ALTER TABLE `issuedbookdetails` DISABLE KEYS */;
INSERT INTO `issuedbookdetails` VALUES (901234,585845,'2023-10-20'),(564651,585845,'2023-10-20'),(584530,585845,'2023-10-20'),(124146,987541,'2023-10-20'),(212142,489651,'2023-10-20'),(656568,489651,'2023-10-20'),(890123,897454,'2023-10-20'),(323123,515049,'2023-10-20'),(901234,987541,'2023-10-24'),(124146,987541,'2023-10-24');
/*!40000 ALTER TABLE `issuedbookdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `letters`
--

DROP TABLE IF EXISTS `letters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `letters` (
  `Letter_Id` char(20) DEFAULT NULL,
  `Letter_File` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `letters`
--

LOCK TABLES `letters` WRITE;
/*!40000 ALTER TABLE `letters` DISABLE KEYS */;
INSERT INTO `letters` VALUES ('#321315_102030','_772223.dat'),('#897454_102030','_712905.dat'),('#646566_405060','_148631.dat'),('#855223_405060','_238917.dat'),('#102030_515412','_228623.dat'),('#102030_405060','_286627.dat'),('#405060_853143','_393871.dat'),('#405060_102030','_767708.dat'),('#487452_102030','_651043.dat');
/*!40000 ALTER TABLE `letters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notices`
--

DROP TABLE IF EXISTS `notices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notices` (
  `Notice_Id` char(20) DEFAULT NULL,
  `Notice_File` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notices`
--

LOCK TABLES `notices` WRITE;
/*!40000 ALTER TABLE `notices` DISABLE KEYS */;
INSERT INTO `notices` VALUES ('#102030_S','_894583.dat'),('#102030_E','_276396.dat'),('#102030_S','_472122.dat'),('#405060_S','_626291.dat'),('#405060_E','_641895.dat');
/*!40000 ALTER TABLE `notices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `progress_report`
--

DROP TABLE IF EXISTS `progress_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `progress_report` (
  `S_Id` int NOT NULL,
  `UT1` decimal(5,2) DEFAULT '0.00',
  `Half_Yearly` decimal(5,2) DEFAULT '0.00',
  `UT2` decimal(5,2) DEFAULT '0.00',
  `Annual` decimal(5,2) DEFAULT '0.00',
  PRIMARY KEY (`S_Id`),
  UNIQUE KEY `S_Id_UNIQUE` (`S_Id`),
  CONSTRAINT `FK` FOREIGN KEY (`S_Id`) REFERENCES `student` (`S_Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progress_report`
--

LOCK TABLES `progress_report` WRITE;
/*!40000 ALTER TABLE `progress_report` DISABLE KEYS */;
INSERT INTO `progress_report` VALUES (184545,63.00,65.00,69.00,0.00),(321315,86.00,66.00,64.00,0.00),(489651,88.00,90.00,89.00,0.00),(515049,83.00,84.00,90.00,0.00),(564623,73.00,72.00,79.00,0.00),(585845,77.00,84.00,93.00,0.00),(845422,56.00,60.00,55.00,0.00),(897454,98.00,95.00,92.00,0.00),(987541,65.00,78.00,95.00,0.00),(987654,87.00,79.00,91.00,0.00);
/*!40000 ALTER TABLE `progress_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `random`
--

DROP TABLE IF EXISTS `random`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `random` (
  `Num` int DEFAULT NULL,
  UNIQUE KEY `Num_UNIQUE` (`Num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `random`
--

LOCK TABLES `random` WRITE;
/*!40000 ALTER TABLE `random` DISABLE KEYS */;
INSERT INTO `random` VALUES (122384),(148631),(228623),(238917),(276396),(286627),(393871),(472122),(626291),(641895),(651043),(712905),(767708),(772223),(894583);
/*!40000 ALTER TABLE `random` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `S_Id` int NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Class` varchar(10) NOT NULL,
  `Section` char(1) DEFAULT NULL,
  `Sex` char(1) DEFAULT NULL,
  `DOB` date NOT NULL,
  `Father_Name` varchar(65) NOT NULL,
  `Father_Occupation` varchar(45) DEFAULT NULL,
  `Mother_Name` varchar(65) NOT NULL,
  `Mother_Occupatioin` varchar(45) DEFAULT NULL,
  `Address` varchar(100) NOT NULL,
  `Contact_Number` char(10) DEFAULT NULL,
  `password` char(20) NOT NULL,
  `Duty_Code` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`S_Id`),
  CONSTRAINT `student_chk_1` CHECK ((length(`Contact_Number`) = 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (184545,'Sanjana Malhotra','IX','C','F','2008-09-10','Harish Malhotra','Chef','Riya Malhotra','Teacher','Ramgarh Taal Road,Gorakhpur','9335245412','passpass#schl','S'),(321315,'Siddhart Menon','X','A','M','2003-12-05','Deepak Menon','Doctor','Swati Menon','Teacher','Gita Press Road,Gorakhpur','8985411421','1012abcde21','S'),(489651,'Rekha Patel','V','A','F','2012-12-14','Ramesh Patel','Police Officer','Radha Patel','Doctor','Ramlila Maidan, Gorakhnath, Gorakhpur','9936527555','MaiHoonNa@School','S'),(515049,'Nandini Mehta','XI','B','F','2009-05-08','Rohit Mehta','Manager','Meenal Mehta','Artist','Husainabad,Lucknow','9992124165','Nahi_Bataunga','S'),(564623,'Karan Suri','VIII','A','M','2006-10-30','Ajay Suri','Software Developer','Neha Suri','Lawyer','Chauri Chaura,Gorakhpur','9464854121','abc1020def2030','S'),(585845,'Sanya Singh','VII','C','F','2008-05-08','Rohit Singh','Doctor','Anjali Singh','Housewife','Kunraghat, Gorakhpur','9800251520','Sanya123','S'),(845422,'Akshay Yadav','VI','B','M','2010-10-09','Mahesh Yadav','Teacher','Meera Yadav','Singer','Chatra Sangh, Gorakhpur','9941005545','qwerty','S'),(897454,'Pooja Sharma','X','D','F','2001-01-01','Vivek Sharma','Proffesor','Shreya Sharma','Journalist','Imambara Road,Lucknow','8851547843','hello_password1010','S'),(987541,'Akash Gupta','XI','A','M','2005-03-02','Manish Gupta','Teacher','Anita Gupta','Housewife','Taramandal,Gorakhpur','8400345041','abac1232','S'),(987654,'Rahul Verma','IX','A','M','2005-03-02','Gaurav Verma','Manager','Sunita Verma','Housewife','Gorakhnath, Gorakhpur','8754510541','password','S');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-25 11:34:06
