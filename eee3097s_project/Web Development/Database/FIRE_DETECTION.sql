-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 27, 2020 at 08:31 AM
-- Server version: 8.0.11
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `FIRE_DETECTION`
--

-- --------------------------------------------------------

--
-- Table structure for table `READINGS`
--

CREATE TABLE `READINGS` (
  `SENSORID` int(11) NOT NULL,
  `TEMPERATURE` char(5) DEFAULT NULL,
  `LUMINOSITY` char(5) DEFAULT NULL,
  `ALERT` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DATE_TIME` char(26) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `READINGS`
--

INSERT INTO `READINGS` (`SENSORID`, `TEMPERATURE`, `LUMINOSITY`, `ALERT`, `DATE_TIME`) VALUES
(5678, '16.19', '15.2', '0', '	2020-10-26 15:03:1'),
(5678, '15.25', '15.1', '0', '	2020-10-26 15:03:4'),
(5678, '15.56', '15.1', '0', '	2020-10-26 15:04:1'),
(5678, '15.5', '14.8', '0', '	2020-10-26 15:04:4');

-- --------------------------------------------------------

--
-- Table structure for table `SENSOR`
--

CREATE TABLE `SENSOR` (
  `SENSORID` int(11) NOT NULL,
  `LATITUDE_degree` int(5) DEFAULT NULL,
  `LATITUDE_minute` int(5) DEFAULT NULL,
  `LATITUDE_second` decimal(10,2) DEFAULT NULL,
  `LONGITUDE_degree` int(5) DEFAULT NULL,
  `LONGITUDE_minute` int(5) DEFAULT NULL,
  `LONGITUDE_second` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `SENSOR`
--

INSERT INTO `SENSOR` (`SENSORID`, `LATITUDE_degree`, `LATITUDE_minute`, `LATITUDE_second`, `LONGITUDE_degree`, `LONGITUDE_minute`, `LONGITUDE_second`) VALUES
(5678, 33, 48, '58.80', 18, 28, '22.00');

-- --------------------------------------------------------

--
-- Table structure for table `USER`
--

CREATE TABLE `USER` (
  `USERID` int(11) NOT NULL,
  `NAME` varchar(20) DEFAULT NULL,
  `PHONE_NUMBER` char(10) DEFAULT NULL,
  `PASSWORD` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DEPARTMENT` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `USER`
--

INSERT INTO `USER` (`USERID`, `NAME`, `PHONE_NUMBER`, `PASSWORD`, `DEPARTMENT`) VALUES
(1234, 'Steve Thomi', '0719786789', 'strongPassword', 'Forest.CONGO');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `READINGS`
--
ALTER TABLE `READINGS`
  ADD PRIMARY KEY (`SENSORID`,`DATE_TIME`);

--
-- Indexes for table `SENSOR`
--
ALTER TABLE `SENSOR`
  ADD PRIMARY KEY (`SENSORID`);

--
-- Indexes for table `USER`
--
ALTER TABLE `USER`
  ADD PRIMARY KEY (`USERID`),
  ADD UNIQUE KEY `PHONE_NUMBER` (`PHONE_NUMBER`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
