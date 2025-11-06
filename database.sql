/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - smart_voting_system
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`smart_voting_system` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `smart_voting_system`;

/*Table structure for table `assemblynomiee` */

DROP TABLE IF EXISTS `assemblynomiee`;

CREATE TABLE `assemblynomiee` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `member_name` varchar(100) NOT NULL,
  `party_name` varchar(100) DEFAULT NULL,
  `symbol_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `assemblynomiee` */

/*Table structure for table `assmvote` */

DROP TABLE IF EXISTS `assmvote`;

CREATE TABLE `assmvote` (
  `vote` varchar(100) NOT NULL,
  `aadhar` varchar(100) NOT NULL,
  PRIMARY KEY (`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `assmvote` */

/*Table structure for table `assmvoters` */

DROP TABLE IF EXISTS `assmvoters`;

CREATE TABLE `assmvoters` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `aadhar_id` varchar(100) DEFAULT NULL,
  `voter_id` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `d_name` varchar(100) DEFAULT NULL,
  `verified` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `assmvoters` */

/*Table structure for table `mptcnomiee` */

DROP TABLE IF EXISTS `mptcnomiee`;

CREATE TABLE `mptcnomiee` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `member_name` varchar(100) NOT NULL,
  `party_name` varchar(100) DEFAULT NULL,
  `symbol_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `mptcnomiee` */

/*Table structure for table `mptcvote` */

DROP TABLE IF EXISTS `mptcvote`;

CREATE TABLE `mptcvote` (
  `vote` varchar(100) NOT NULL,
  `aadhar` varchar(100) NOT NULL,
  PRIMARY KEY (`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `mptcvote` */

/*Table structure for table `mptcvoters` */

DROP TABLE IF EXISTS `mptcvoters`;

CREATE TABLE `mptcvoters` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `aadhar_id` varchar(100) DEFAULT NULL,
  `voter_id` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `d_name` varchar(100) DEFAULT NULL,
  `verified` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `mptcvoters` */

/*Table structure for table `nominee` */

DROP TABLE IF EXISTS `nominee`;

CREATE TABLE `nominee` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `member_name` varchar(100) NOT NULL,
  `party_name` varchar(100) DEFAULT NULL,
  `symbol_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `nominee` */

/*Table structure for table `vote` */

DROP TABLE IF EXISTS `vote`;

CREATE TABLE `vote` (
  `vote` varchar(100) NOT NULL,
  `aadhar` varchar(100) NOT NULL,
  PRIMARY KEY (`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `vote` */

/*Table structure for table `voters` */

DROP TABLE IF EXISTS `voters`;

CREATE TABLE `voters` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `aadhar_id` varchar(100) DEFAULT NULL,
  `voter_id` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `d_name` varchar(100) DEFAULT NULL,
  `verified` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `voters` */

/*Table structure for table `zptcnomiee` */

DROP TABLE IF EXISTS `zptcnomiee`;

CREATE TABLE `zptcnomiee` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `member_name` varchar(100) NOT NULL,
  `party_name` varchar(100) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT NULL,
  `symbol_name` varchar(100) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `zptcnomiee` */

insert  into `zptcnomiee`(`sno`,`member_name`,`party_name`,`symbol_name`) values (1,'KAMALA','jana','1.png');

/*Table structure for table `zptcvote` */

DROP TABLE IF EXISTS `zptcvote`;

CREATE TABLE `zptcvote` (
  `vote` varchar(100) NOT NULL,
  `aadhar` varchar(100) NOT NULL,
  PRIMARY KEY (`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `zptcvote` */

/*Table structure for table `zptcvoters` */

DROP TABLE IF EXISTS `zptcvoters`;

CREATE TABLE `zptcvoters` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `aadhar_id` varchar(100) DEFAULT NULL,
  `voter_id` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `d_name` varchar(100) DEFAULT NULL,
  `verified` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `zptcvoters` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
