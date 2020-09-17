-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 16, 2020 at 05:54 PM
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
-- Table structure for table `SENSOR`
--

CREATE TABLE `SENSOR` (
  `SENSORID` int(11) NOT NULL,
  `LOCATION` char(25) DEFAULT NULL,
  `TEMPERATURE` char(10) DEFAULT NULL,
  `HUMIDITY` char(10) DEFAULT NULL,
  `ALERT` char(35) DEFAULT NULL,
  `SENSOR_TYPE` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `USER`
--

CREATE TABLE `USER` (
  `USERID` int(11) NOT NULL,
  `NAME` varchar(20) DEFAULT NULL,
  `PHONE_NUMBER` char(10) DEFAULT NULL,
  `PASSWORD` varchar(10) DEFAULT NULL,
  `LOGINSTATUS` char(10) DEFAULT NULL,
  `ADMINISTRATION` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `SENSOR`
--
ALTER TABLE `SENSOR`
  ADD PRIMARY KEY (`SENSORID`),
  ADD UNIQUE KEY `LOCATION` (`LOCATION`);

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
