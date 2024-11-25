-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: db_sgswayne
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-29 23:41:26.750199'),(2,'auth','0001_initial','2024-10-29 23:41:27.850365'),(3,'admin','0001_initial','2024-10-29 23:41:28.134540'),(4,'admin','0002_logentry_remove_auto_add','2024-10-29 23:41:28.159801'),(5,'admin','0003_logentry_add_action_flag_choices','2024-10-29 23:41:28.181853'),(6,'contenttypes','0002_remove_content_type_name','2024-10-29 23:41:28.332847'),(7,'auth','0002_alter_permission_name_max_length','2024-10-29 23:41:28.454907'),(8,'auth','0003_alter_user_email_max_length','2024-10-29 23:41:28.491258'),(9,'auth','0004_alter_user_username_opts','2024-10-29 23:41:28.503821'),(10,'auth','0005_alter_user_last_login_null','2024-10-29 23:41:28.604505'),(11,'auth','0006_require_contenttypes_0002','2024-10-29 23:41:28.608799'),(12,'auth','0007_alter_validators_add_error_messages','2024-10-29 23:41:28.622782'),(13,'auth','0008_alter_user_username_max_length','2024-10-29 23:41:28.753487'),(14,'auth','0009_alter_user_last_name_max_length','2024-10-29 23:41:28.869226'),(15,'auth','0010_alter_group_name_max_length','2024-10-29 23:41:28.897734'),(16,'auth','0011_update_proxy_permissions','2024-10-29 23:41:28.909331'),(17,'auth','0012_alter_user_first_name_max_length','2024-10-29 23:41:29.032047'),(18,'sessions','0001_initial','2024-10-29 23:41:29.091975'),(19,'sistema_de_seguranca','0001_initial','2024-11-01 23:45:26.613316'),(20,'sistema_de_seguranca','0002_profile','2024-11-03 23:40:06.911756'),(21,'sistema_de_seguranca','0003_profile_cargo','2024-11-07 23:01:32.196279'),(22,'sistema_de_seguranca','0004_profile_profile_picture_alter_profile_cargo_and_more','2024-11-17 00:29:52.784027'),(23,'sistema_de_seguranca','0004_profile_profile_image_alter_profile_cargo_and_more','2024-11-17 23:03:52.403923'),(24,'sistema_de_seguranca','0005_alter_profile_profile_image','2024-11-19 00:03:04.308987'),(25,'sistema_de_seguranca','0006_alter_profile_profile_image','2024-11-19 00:09:32.001937'),(26,'sistema_de_seguranca','0007_rename_cargo_profile_cargo_choices','2024-11-20 19:05:13.557293'),(27,'sistema_de_seguranca','0008_rename_cargo_choices_profile_cargo','2024-11-20 19:05:46.014639'),(28,'sistema_de_seguranca','0009_remove_profile_codigo_recuperacao_and_more','2024-11-21 23:56:03.271611'),(29,'sistema_de_seguranca','0010_profile_codigo_recuperacao','2024-11-21 23:56:03.312090'),(30,'sistema_de_seguranca','0011_alter_profile_user','2024-11-22 00:00:45.529687'),(31,'sistema_de_seguranca','0012_alter_profile_user','2024-11-22 00:24:44.253994');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-25 20:14:41
