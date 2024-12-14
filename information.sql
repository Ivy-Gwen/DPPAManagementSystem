-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 14, 2024 at 03:53 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `health_records_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `information`
--

CREATE TABLE `information` (
  `ID` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Phone_number` varchar(50) NOT NULL,
  `Date_of_Birth` varchar(50) NOT NULL,
  `Age` varchar(30) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Weight` varchar(20) NOT NULL,
  `Height` varchar(20) NOT NULL,
  `Health_Condition` varchar(50) NOT NULL,
  `Medicine` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `information`
--

INSERT INTO `information` (`ID`, `Name`, `Phone_number`, `Date_of_Birth`, `Age`, `Gender`, `Weight`, `Height`, `Health_Condition`, `Medicine`) VALUES
(1, 'Gwen', '09166950703', '10-25-2005', '19', 'Female', '46', '155', 'None', 'None'),
(2, 'Ivy', '09166950703', '10-25-2005', '19', 'Female', '46', '155', 'None', 'None'),
(3, 'Sophie', '09275970001', '09-29-2009', '15', 'Female', '50', '158', 'None', 'None');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `information`
--
ALTER TABLE `information`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
