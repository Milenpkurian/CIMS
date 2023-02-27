-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2023 at 09:48 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dep`
--

-- --------------------------------------------------------

--
-- Table structure for table `chemicals`
--

CREATE TABLE `chemicals` (
  `id` varchar(100) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `item_type` varchar(100) DEFAULT NULL,
  `in_stock` varchar(100) DEFAULT NULL,
  `received_date` date DEFAULT NULL,
  `expiry_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chemicals`
--

INSERT INTO `chemicals` (`id`, `item_name`, `item_type`, `in_stock`, `received_date`, `expiry_date`) VALUES
('CH010', 'Chlorine', 'Organic', '20 L', '2023-01-04', '2023-03-09'),
('RT004', 'Fluride', 'Inorganic', '40 L', '2023-02-21', '2023-02-27'),
('RT009', 'Flurine', 'Inorganic', '20 L', '2023-02-15', '2023-05-25'),
('ST002', 'Methane', 'Organic', '30 L', '2023-02-09', '2023-02-28'),
('ST004', 'Methane', 'Organic', '76 L', '2023-02-02', '2023-02-28'),
('ST006', 'Butane', 'Organic', '40 L', '2023-02-11', '2023-02-28');

-- --------------------------------------------------------

--
-- Table structure for table `computers`
--

CREATE TABLE `computers` (
  `id` varchar(100) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `defective` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `computers`
--

INSERT INTO `computers` (`id`, `item_name`, `quantity`, `defective`) VALUES
('CS010', 'Acer Veriton UX1', 15, 3),
('CS102', 'Acer Veriton Z2151', 10, 1),
('CS103', 'HP Pavilion Core i3 ', 5, 0);

-- --------------------------------------------------------

--
-- Table structure for table `electronics`
--

CREATE TABLE `electronics` (
  `id` varchar(100) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `defective` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `electronics`
--

INSERT INTO `electronics` (`id`, `item_name`, `quantity`, `defective`) VALUES
('CS001', 'Fan', 10, 2),
('CS002', 'Bulb', 50, 2);

-- --------------------------------------------------------

--
-- Table structure for table `equipments`
--

CREATE TABLE `equipments` (
  `id` varchar(100) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `defective` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `equipments`
--

INSERT INTO `equipments` (`id`, `item_name`, `quantity`, `defective`) VALUES
('CS001', 'Table', 10, 2),
('ST002', 'crucible tong', 15, 5),
('ST003', 'Meker Burner', 3, 0),
('ST004', 'Electronic Balance', 5, 1),
('ST005', 'Clement  Apparatus', 5, 2),
('ST006', 'Centrifuge', 5, 1),
('ST007', 'Hot Plate', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `furniture`
--

CREATE TABLE `furniture` (
  `id` varchar(100) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `defective` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `furniture`
--

INSERT INTO `furniture` (`id`, `item_name`, `quantity`, `defective`) VALUES
('ST001', 'Table', 15, 3),
('ST002', 'Desk', 50, 2);

-- --------------------------------------------------------

--
-- Table structure for table `glasswares`
--

CREATE TABLE `glasswares` (
  `id` varchar(100) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `defective` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `glasswares`
--

INSERT INTO `glasswares` (`id`, `item_name`, `quantity`, `defective`) VALUES
('ST001', 'Beaker', 10, 2),
('ST002', 'Flask', 45, 10);

-- --------------------------------------------------------

--
-- Table structure for table `req_lab`
--

CREATE TABLE `req_lab` (
  `id` varchar(100) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `item_type` varchar(100) DEFAULT NULL,
  `req_qty` varchar(100) DEFAULT NULL,
  `need_for` varchar(500) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chemicals`
--
ALTER TABLE `chemicals`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `computers`
--
ALTER TABLE `computers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `electronics`
--
ALTER TABLE `electronics`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `equipments`
--
ALTER TABLE `equipments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `furniture`
--
ALTER TABLE `furniture`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `glasswares`
--
ALTER TABLE `glasswares`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `req_lab`
--
ALTER TABLE `req_lab`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
