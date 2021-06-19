-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2021 at 05:09 PM
-- Server version: 8.0.19
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `be_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(40) NOT NULL,
  `code` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `user_name`, `password`, `code`) VALUES
(1, 'ritumahajan284@gmail.com', 'admin123', 0);

-- --------------------------------------------------------

--
-- Table structure for table `biryanis`
--

CREATE TABLE `biryanis` (
  `bid` int NOT NULL,
  `B_name` varchar(30) NOT NULL,
  `price` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `biryanis`
--

INSERT INTO `biryanis` (`bid`, `B_name`, `price`) VALUES
(1, 'chicken biryani', 210),
(2, 'Mutton Biryani', 253),
(3, 'Chicken family pack', 552),
(4, 'Special chicken biryani', 337),
(5, 'Special mutton biryani', 351),
(6, 'Supreme chicken biryani', 784),
(7, 'Supreme mutton biryani', 819),
(8, 'Egg Biryani', 154),
(9, 'veg biryani', 154),
(10, 'veg family pack', 383),
(11, 'veg supreme pack', 574);

-- --------------------------------------------------------

--
-- Table structure for table `breads`
--

CREATE TABLE `breads` (
  `brid` int NOT NULL,
  `breadname` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `breads`
--

INSERT INTO `breads` (`brid`, `breadname`, `price`) VALUES
(1, 'Tandoori Roti', 40),
(2, 'Rumali roti', 40);

-- --------------------------------------------------------

--
-- Table structure for table `curries`
--

CREATE TABLE `curries` (
  `cid` int NOT NULL,
  `cname` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `curries`
--

INSERT INTO `curries` (`cid`, `cname`, `price`) VALUES
(1, 'Butter chicken Boneless', 245),
(2, 'nizami handi', 171);

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_id` int NOT NULL,
  `name` varchar(30) NOT NULL,
  `token` int NOT NULL,
  `total` int DEFAULT NULL,
  `payment` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_id`, `name`, `token`, `total`, `payment`) VALUES
(6, 'shashank naik', 48, NULL, NULL),
(7, 'srushti patil', 12, NULL, NULL),
(8, 'srushti patil', 24, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dessert`
--

CREATE TABLE `dessert` (
  `did` int NOT NULL,
  `dname` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `dessert`
--

INSERT INTO `dessert` (`did`, `dname`, `price`) VALUES
(1, 'Qubani ka meetha', 107),
(2, 'Double ka meetha', 73),
(3, 'cheesecake', 100),
(4, 'snickers pie', 80),
(5, 'dark chocolate', 50),
(6, 'sweet cherry dessert', 60),
(7, 'Chocolate brownie', 100),
(8, 'coconut cake', 150);

-- --------------------------------------------------------

--
-- Table structure for table `kebabs`
--

CREATE TABLE `kebabs` (
  `kid` int NOT NULL,
  `kname` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `kebabs`
--

INSERT INTO `kebabs` (`kid`, `kname`, `price`) VALUES
(1, 'chicken tikka kebab', 243),
(2, 'tandoori chicken', 243),
(3, 'chicken reshmi kebab', 243),
(4, 'chicken garlic kebab', 243),
(5, 'doner kebab', 110),
(6, 'pocket kebab', 80);

-- --------------------------------------------------------

--
-- Table structure for table `offers`
--

CREATE TABLE `offers` (
  `ofid` int NOT NULL,
  `dish1` varchar(30) NOT NULL,
  `dish2` varchar(30) NOT NULL,
  `actualPrice` int NOT NULL,
  `offeerPrice` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `offers`
--

INSERT INTO `offers` (`ofid`, `dish1`, `dish2`, `actualPrice`, `offeerPrice`) VALUES
(1, 'chicken biryani', 'doner kebab', 320, 300),
(2, 'veg biryani', 'chocolate brownie', 254, 230),
(3, 'chicken family pack', 'pocket kebab', 632, 600),
(4, 'egg biryani', 'butter chicken boneless', 399, 350);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `oid` int NOT NULL,
  `customer_id` int NOT NULL,
  `order_name` varchar(50) NOT NULL,
  `quantity` int NOT NULL,
  `price` int NOT NULL,
  `take_away` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`oid`, `customer_id`, `order_name`, `quantity`, `price`, `take_away`) VALUES
(4, 8, 'veg biryanichocolate brownie', 1, 230, 'no'),
(5, 8, 'chicken biryani', 1, 210, 'no'),
(6, 8, 'nizami handi', 1, 171, 'no');

-- --------------------------------------------------------

--
-- Table structure for table `special_order`
--

CREATE TABLE `special_order` (
  `spe_id` int NOT NULL,
  `order_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `special_order`
--

INSERT INTO `special_order` (`spe_id`, `order_name`, `price`) VALUES
(1, 'cheese Burgur', 50),
(2, 'cheese burst pizza', 150),
(3, 'Pasta with Lamb Ragù', 250),
(4, 'Malted Custard French Toast', 100);

-- --------------------------------------------------------

--
-- Table structure for table `starter`
--

CREATE TABLE `starter` (
  `sid` int NOT NULL,
  `sname` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `starter`
--

INSERT INTO `starter` (`sid`, `sname`, `price`) VALUES
(1, 'chilli chicken', 264),
(2, 'chicken 65', 264),
(3, 'pepper chicken', 264),
(4, 'paneer 65', 196),
(5, 'veg manchurian ', 189);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `biryanis`
--
ALTER TABLE `biryanis`
  ADD PRIMARY KEY (`bid`);

--
-- Indexes for table `breads`
--
ALTER TABLE `breads`
  ADD PRIMARY KEY (`brid`);

--
-- Indexes for table `curries`
--
ALTER TABLE `curries`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `dessert`
--
ALTER TABLE `dessert`
  ADD PRIMARY KEY (`did`);

--
-- Indexes for table `kebabs`
--
ALTER TABLE `kebabs`
  ADD PRIMARY KEY (`kid`);

--
-- Indexes for table `offers`
--
ALTER TABLE `offers`
  ADD PRIMARY KEY (`ofid`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `special_order`
--
ALTER TABLE `special_order`
  ADD PRIMARY KEY (`spe_id`);

--
-- Indexes for table `starter`
--
ALTER TABLE `starter`
  ADD PRIMARY KEY (`sid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `biryanis`
--
ALTER TABLE `biryanis`
  MODIFY `bid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `breads`
--
ALTER TABLE `breads`
  MODIFY `brid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `curries`
--
ALTER TABLE `curries`
  MODIFY `cid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `customer_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `dessert`
--
ALTER TABLE `dessert`
  MODIFY `did` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `kebabs`
--
ALTER TABLE `kebabs`
  MODIFY `kid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `offers`
--
ALTER TABLE `offers`
  MODIFY `ofid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `oid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `special_order`
--
ALTER TABLE `special_order`
  MODIFY `spe_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `starter`
--
ALTER TABLE `starter`
  MODIFY `sid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
