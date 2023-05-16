-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2023 at 03:36 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `students_details`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendence`
--

CREATE TABLE `attendence` (
  `sl_no` int(11) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `login_info` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendence`
--

INSERT INTO `attendence` (`sl_no`, `id`, `name`, `login_info`) VALUES
(2, 95, 'Rahul', '2023-05-05 15:31:22'),
(3, 95, 'Rahul', '2023-05-07 12:50:14'),
(4, 22, 'Romit', '2023-05-07 12:50:19'),
(5, 61, 'Anirban', '2023-05-07 12:55:27'),
(6, 87, 'kusal paul', '2023-05-07 12:56:13'),
(7, 95, 'Rahul', '2023-05-07 16:38:29'),
(8, 22, 'Romit', '2023-05-07 16:39:57'),
(9, 61, 'Anirban', '2023-05-07 16:40:35'),
(10, 79, 'Debasmita', '2023-05-07 16:40:39'),
(11, 105, 'Rajdip', '2023-05-07 16:53:13'),
(12, 95, 'Rahul', '2023-05-09 05:32:29'),
(13, 22, 'Romit', '2023-05-09 05:33:08'),
(14, 79, 'Debasmita', '2023-05-09 05:33:22'),
(15, 61, 'Anirban', '2023-05-09 05:33:46'),
(17, 105, 'Rajdip', '2023-05-09 05:54:00'),
(18, 95, 'Rahul', '2023-05-09 11:15:15'),
(19, 95, 'Rahul', '2023-05-09 18:44:28'),
(20, 79, 'Debasmita', '2023-05-09 18:46:36'),
(21, 95, 'Rahul', '2023-05-10 04:29:28'),
(23, 23, 'Brotin', '2023-05-10 06:54:43'),
(24, 95, 'Rahul', '2023-05-10 07:32:57'),
(25, 79, 'Debasmita', '2023-05-10 14:31:35'),
(26, 95, 'Rahul', '2023-05-10 14:32:03'),
(27, 95, 'Rahul', '2023-05-11 13:02:10'),
(28, 87, 'kusal paul', '2023-05-11 13:03:19'),
(29, 22, 'Romit', '2023-05-11 13:03:35'),
(30, 87, 'kusal paul', '2023-05-12 04:27:15'),
(31, 95, 'Rahul', '2023-05-12 04:27:49'),
(32, 105, 'Rajdip', '2023-05-12 04:29:02'),
(33, 11, 'ssm', '2023-05-12 04:32:39'),
(34, 79, 'Debasmita', '2023-05-12 08:07:27'),
(35, 95, 'Rahul', '2023-05-12 08:07:43'),
(36, 22, 'Romit', '2023-05-12 08:08:13'),
(37, 87, 'kusal paul', '2023-05-12 08:08:53'),
(38, 123, 'dilar', '2023-05-12 08:11:45');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`login_id`, `username`, `password`) VALUES
(1, 'admin', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `student_info`
--

CREATE TABLE `student_info` (
  `id` int(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `image_path` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_info`
--

INSERT INTO `student_info` (`id`, `name`, `image_path`) VALUES
(11, 'ssm', 'Data/11'),
(22, 'Romit', 'Data/22'),
(23, 'Brotin', 'Data/23'),
(61, 'Anirban', 'Data/61'),
(79, 'Debasmita', 'Data/79'),
(87, 'kusal paul', 'Data/87'),
(95, 'Rahul', 'Data/95'),
(105, 'Rajdip', 'Data/105'),
(123, 'dilar', 'Data/123');

-- --------------------------------------------------------

--
-- Table structure for table `total_attendence`
--

CREATE TABLE `total_attendence` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `total_att` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `total_attendence`
--

INSERT INTO `total_attendence` (`id`, `name`, `total_att`) VALUES
(11, 'ssm', 1),
(22, 'Romit', 5),
(23, 'Brotin', 2),
(61, 'Anirban', 3),
(79, 'Debasmita', 5),
(87, 'kusal paul', 4),
(95, 'Rahul', 12),
(105, 'Rajdip', 3),
(123, 'dilar', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendence`
--
ALTER TABLE `attendence`
  ADD PRIMARY KEY (`sl_no`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `student_info`
--
ALTER TABLE `student_info`
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
  MODIFY `sl_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendence`
--
ALTER TABLE `attendence`
  ADD CONSTRAINT `attendence_ibfk_1` FOREIGN KEY (`id`) REFERENCES `student_info` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
