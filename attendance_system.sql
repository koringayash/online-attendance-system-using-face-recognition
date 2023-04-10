-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2023 at 11:19 AM
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
-- Database: `attendance_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `sno` int(11) NOT NULL,
  `Id_no` varchar(10) NOT NULL,
  `present` int(1) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`sno`, `Id_no`, `present`, `date`, `time`) VALUES
(1, '20CP030', 0, '2023-03-23', '14:44:40'),
(2, '20CP042', 1, '2023-03-23', '14:44:40'),
(3, '20CP067', 0, '2023-03-23', '14:44:40'),
(4, '20CP074', 1, '2023-03-23', '14:44:40'),
(5, '20CP030', 0, '2023-04-01', '10:43:12'),
(6, '20CP067', 1, '2023-04-01', '10:43:12'),
(7, '20EE059', 0, '2023-04-01', '10:43:12'),
(8, '20CP030', 0, '2023-04-01', '10:53:02'),
(9, '20CP067', 1, '2023-04-01', '10:53:02'),
(10, '20EE059', 0, '2023-04-01', '10:53:02'),
(11, '20CP030', 0, '2023-04-01', '10:53:12'),
(12, '20CP067', 0, '2023-04-01', '10:53:12'),
(13, '20EE059', 0, '2023-04-01', '10:53:12'),
(14, '20CP030', 0, '2023-04-01', '10:53:24'),
(15, '20CP067', 1, '2023-04-01', '10:53:24'),
(17, '20CP030', 0, '2023-04-01', '15:16:06'),
(18, '20CP067', 1, '2023-04-01', '15:16:06'),
(19, '20CP074', 1, '2023-04-01', '15:16:06'),
(20, '20EE059', 0, '2023-04-01', '15:16:06'),
(21, '20CP030', 0, '2023-04-03', '16:03:29'),
(22, '20CP067', 1, '2023-04-03', '16:03:29'),
(23, '20CP073', 0, '2023-04-03', '16:03:29'),
(24, '20CP074', 0, '2023-04-03', '16:03:29'),
(25, '20EE059', 0, '2023-04-03', '16:03:29');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(15) NOT NULL,
  `mes` varchar(500) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `img_file` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `mes`, `date`, `img_file`) VALUES
(2, 'Koringa Yash', 'koringayash@gmail.com', '7600796406', 'This is message', '2023-03-23 14:39:20', ''),
(4, 'Koringa Yash', 'koringayash@gmail.com', '7600796406', 'Tari mane chodu', '2023-03-24 13:35:56', '909_YASH_SIGN new.jpg'),
(5, 'Koringa Yash', 'koringayash@gmail.com', '7600796406', 'This is Message', '2023-03-24 13:36:20', 'AADHAR BACK.jpeg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
