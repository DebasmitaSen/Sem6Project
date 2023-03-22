-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 22, 2023 at 08:10 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `person`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendence`
--

CREATE TABLE `attendence` (
  `sl_no` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `login_info` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendence`
--

INSERT INTO `attendence` (`sl_no`, `id`, `name`, `login_info`) VALUES
(15, 14, 'Debu', '2023-03-21 14:58:44'),
(21, 14, 'Debu', '2023-03-22 15:29:39'),
(24, 3, 'Rahul', '2023-03-22 15:52:31'),
(25, 14, 'Debu', '2023-03-22 18:37:01'),
(26, 3, 'Rahul', '2023-03-22 18:37:33');

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `id` int(15) NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Image` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`id`, `Name`, `Image`) VALUES
(3, 'Rahul', 'Data/3'),
(14, 'Debu', 'Data/14'),
(20, 'Rajdip', 'Data/20'),
(31, 'Sambho', 'Data/31'),
(43, 'Romit', 'Data/43'),
(84, 'Rajesh', 'Data/84');

-- --------------------------------------------------------

--
-- Table structure for table `total_attendence`
--

CREATE TABLE `total_attendence` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `total_att` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `total_attendence`
--

INSERT INTO `total_attendence` (`id`, `name`, `total_att`) VALUES
(3, 'Rahul', 2),
(14, 'Debu', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendence`
--
ALTER TABLE `attendence`
  ADD PRIMARY KEY (`sl_no`);

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `total_attendence`
--
ALTER TABLE `total_attendence`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendence`
--
ALTER TABLE `attendence`
  MODIFY `sl_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
