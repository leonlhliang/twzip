# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: localhost (MySQL 5.6.22)
# Database: postal
# Generation Time: 2015-01-21 16:21:53 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table city
# ------------------------------------------------------------

DROP TABLE IF EXISTS `city`;

CREATE TABLE `city` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `alias` varchar(50) DEFAULT '',
  `name_zhtw` varchar(50) NOT NULL DEFAULT '',
  `name_enus` varchar(50) DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_zhtw` (`name_zhtw`),
  UNIQUE KEY `alias` (`alias`),
  UNIQUE KEY `name_enus` (`name_enus`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table district
# ------------------------------------------------------------

DROP TABLE IF EXISTS `district`;

CREATE TABLE `district` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `alias` varchar(50) DEFAULT '',
  `name_zhtw` varchar(50) NOT NULL DEFAULT '',
  `name_enus` varchar(50) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table region
# ------------------------------------------------------------

DROP TABLE IF EXISTS `region`;

CREATE TABLE `region` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_city` int(11) unsigned NOT NULL,
  `id_district` int(11) unsigned NOT NULL,
  `id_street` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_city` (`id_city`,`id_district`,`id_street`),
  KEY `id_district` (`id_district`),
  KEY `id_street` (`id_street`),
  CONSTRAINT `region_ibfk_1` FOREIGN KEY (`id_city`) REFERENCES `city` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `region_ibfk_2` FOREIGN KEY (`id_district`) REFERENCES `district` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `region_ibfk_3` FOREIGN KEY (`id_street`) REFERENCES `street` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table street
# ------------------------------------------------------------

DROP TABLE IF EXISTS `street`;

CREATE TABLE `street` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `alias` varchar(50) DEFAULT '',
  `name_zhtw` varchar(50) NOT NULL DEFAULT '',
  `name_enus` varchar(50) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
