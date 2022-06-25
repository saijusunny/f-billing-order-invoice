-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2022 at 08:03 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fbilling`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `commentid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `companyid` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `salestaxno` varchar(255) DEFAULT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `currencysign` varchar(255) DEFAULT NULL,
  `currsignplace` varchar(255) DEFAULT NULL,
  `decimalseperator` varchar(255) DEFAULT NULL,
  `excurrency` varchar(255) DEFAULT NULL,
  `dateformat` varchar(255) DEFAULT NULL,
  `exdate` varchar(255) DEFAULT NULL,
  `taxtype` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `printimageornot` int(11) NOT NULL,
  `tax1name` varchar(255) DEFAULT NULL,
  `tax1rate` float DEFAULT NULL,
  `printtax1` int(11) DEFAULT NULL,
  `tax2name` varchar(255) DEFAULT NULL,
  `tax2rate` float DEFAULT NULL,
  `printtax2` int(11) DEFAULT NULL,
  `menu_and_wincolour` varchar(255) DEFAULT NULL,
  `attachment_file_type` varchar(255) DEFAULT NULL,
  `miscellanoustab_cbutton1` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton2` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton3` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton4` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton5` int(11) DEFAULT NULL,
  `miscellanoustab_cbutton6` int(11) DEFAULT NULL,
  `Estimate_prefix` varchar(255) DEFAULT NULL,
  `est_Headerboxbackgroundcolor` varchar(255) DEFAULT NULL,
  `Customizeestimatetextlabels` varchar(255) DEFAULT NULL,
  `Defaultestimatetemplate` varchar(255) DEFAULT NULL,
  `Customizeestimatetextlabels1` varchar(255) DEFAULT NULL,
  `Customizeestimatetextlabels2` varchar(255) DEFAULT NULL,
  `Customizeestimatetextlabels3` varchar(255) DEFAULT NULL,
  `Customizeestimatetextlabels4` varchar(255) DEFAULT NULL,
  `Customizeestimatetextlabels5` varchar(255) DEFAULT NULL,
  `Startingestimatenumber` int(11) DEFAULT NULL,
  `Predefinedtextforestimates` varchar(255) DEFAULT NULL,
  `adv_Selectedtemplatepreview` varchar(255) DEFAULT NULL,
  `porder_prefix` varchar(255) DEFAULT NULL,
  `headrebox_color` varchar(255) DEFAULT NULL,
  `starting_porderno` int(11) DEFAULT NULL,
  `text_label1` varchar(255) DEFAULT NULL,
  `text_label2` varchar(255) DEFAULT NULL,
  `text_label3` varchar(255) DEFAULT NULL,
  `text_label4` varchar(255) DEFAULT NULL,
  `text_label5` varchar(255) DEFAULT NULL,
  `text_label6` varchar(255) DEFAULT NULL,
  `text_label7` varchar(255) DEFAULT NULL,
  `predefindterms_porder` varchar(255) DEFAULT NULL,
  `email_template` varchar(255) NOT NULL,
  `text_field` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`companyid`, `name`, `address`, `email`, `salestaxno`, `currency`, `currencysign`, `currsignplace`, `decimalseperator`, `excurrency`, `dateformat`, `exdate`, `taxtype`, `image`, `printimageornot`, `tax1name`, `tax1rate`, `printtax1`, `tax2name`, `tax2rate`, `printtax2`, `menu_and_wincolour`, `attachment_file_type`, `miscellanoustab_cbutton1`, `miscellanoustab_cbutton2`, `miscellanoustab_cbutton3`, `miscellanoustab_cbutton4`, `miscellanoustab_cbutton5`, `miscellanoustab_cbutton6`, `Estimate_prefix`, `est_Headerboxbackgroundcolor`, `Customizeestimatetextlabels`, `Defaultestimatetemplate`, `Customizeestimatetextlabels1`, `Customizeestimatetextlabels2`, `Customizeestimatetextlabels3`, `Customizeestimatetextlabels4`, `Customizeestimatetextlabels5`, `Startingestimatenumber`, `Predefinedtextforestimates`, `adv_Selectedtemplatepreview`, `porder_prefix`, `headrebox_color`, `starting_porderno`, `text_label1`, `text_label2`, `text_label3`, `text_label4`, `text_label5`, `text_label6`, `text_label7`, `predefindterms_porder`, `email_template`, `text_field`) VALUES
(10, ' Infox Technologies', 'Infopark Phase-1\nkochi\nph:56789098\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', '', '456789847898987', '', '$', 'after amount', '', '8347.26$', 'dd.mm.yyyy', '2022-06-24', '2', '386infox.png', 0, 'tax 1', 12.5, 0, 'tax 2', 6, 0, NULL, '', 0, 0, 0, 0, 0, 0, 'fghfdggffg', 'Maroon', 'Estimate     est', 'Simplified 2 (logo on right side)', 'Estimate#   est', 'Estimate date   8/9/2022', 'Due date   8/10/2022', 'Estimate to   customer', 'Estimate total   700', 3, 'conditions\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', 'Professional 1 (logo on left side)', 'P.ORD', '0', 5, 'Purchase Order', 'P.Order#', 'P.Order Date', 'Due date', 'Vendor', 'Delivery to', 'P.Order total', 'terms and conditions\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', 'Purchase Order E-Mail template', '{{Customer_Email}}{{Customer_Email}}{{Customer_Address}}{{Customer_Address}}{{Company_Email1}}{{Company_Email1}}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customerid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `contactperson` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cptelno` varchar(255) DEFAULT NULL,
  `cpfax` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `shipcontactperson` varchar(255) DEFAULT NULL,
  `shipcpemail` varchar(255) DEFAULT NULL,
  `shipcptelno` varchar(255) DEFAULT NULL,
  `shipcpfax` varchar(255) DEFAULT NULL,
  `taxexempt` varchar(255) DEFAULT NULL,
  `specifictax1` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `customertype` varchar(255) DEFAULT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `customerno` varchar(255) NOT NULL,
  `specifictax2` float NOT NULL,
  `vatregnumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customerid`, `companyid`, `category`, `status`, `businessname`, `businessaddress`, `shipname`, `shipaddress`, `contactperson`, `cpemail`, `cptelno`, `cpfax`, `cpmobileforsms`, `shipcontactperson`, `shipcpemail`, `shipcptelno`, `shipcpfax`, `taxexempt`, `specifictax1`, `discount`, `country`, `city`, `customertype`, `notes`, `customerno`, `specifictax2`, `vatregnumber`) VALUES
(3, NULL, 'Default', '1', 'sdsd', 'sdfs', 'fdgfd', 'fdgfd', 'sdfd', 'sdfs', '44', '451', '1454', 'dfg', 'fdgfd', '1452', '1452', '1', 2, 2, 'America', 'cxcvc', '0', 'xcvcvc', '5464564654', 0, 0),
(15482, NULL, 'Cust', '1', 'Customer2', 'errors\n\n', 'dfdfd', 'dfdffd\n\n', 'viswam', 'viswam@gmail.com', '111444', '144114', '1141414111', 'sfdf', 'sdfdf', '145', '5545', '1', 0, 4, 'America', 'ekm', 'Both(Client/Vender)', 'cfgffggfdgf\n\n\n\n', '165648', 0, 0),
(15515, NULL, 'Cust', '1', 'Customer2', 'errors\n', 'dfdfd', 'dfdffd\n', 'viswam', 'viswam@gmail.com', '111444', '144114', '1141414111', 'sfdf', 'sdfdf', '145', '5545', '1', 0, 4, 'America', 'ekm', 'Both(Client/Vender)', 'cfgffggfdgf\n\n\n', '18888', 0, 0),
(15541, NULL, 'Cust', '1', 'Elnixdfd', 'elnix eruveli\n', 'Elnixdfd', 'elnix eruveli\n\n', 'joby', 'joby@gmail.com', '1234567895', '+1 (212) 222 8888', 'None', 'joby joseph', 'jobyjoseph@gmail.com', '1234567895', '+1 (212) 222 8888', '1', 12, 12, 'America', 'chott', 'Vender', 'None\n\n', '245414', 0, 0),
(15542, NULL, 'Cust', '1', 'bvnvndfd', 'bnbvnbvbv\n\n', '', '\n\n', 'ghhjg', 'bnb@gmail.com', '', '', 'None', '', '', '', '', '1', 0, 0, '', '', 'Both(Client/Vender)', 'bvnvbn\n\n', '145854', 0, 0),
(15552, NULL, 'Default', '1', 'Cucxsdff', 'bnvvnbvn', '', '', 'bvnbvn', 'bnvbvn', '', '', NULL, '', '', '', '', '', 0, 0, '', '', NULL, NULL, '15455404545', 0, 0),
(15580, NULL, 'Default', '1', 'fghg', 'ghfhg\n', 'fghg', 'ghfhg\n\n', '', '', '', '', '', '', '', '', '', '1', 0, 0, '', '', 'Client', '\n', '1596', 0, 0),
(15582, NULL, 'Cust', '1', 'Elnix power', 'Chot\n\n\n\n', 'Elnix power', 'Chot\n\n\n\n\n', 'joby pjs', 'joby@gmail.com', '04843203913', '+1 (212) 222 8888', '8857486525', 'joby pjs', 'joby@gmail.com', '04843203913', '+1 (212) 222 8888', '1', 25, 10, 'India', 'cho', 'Client', 'llll\n\n\n', 'INV154', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `documents`
--

CREATE TABLE `documents` (
  `documentid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `add_document` varchar(500) DEFAULT NULL,
  `orderid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `documents`
--

INSERT INTO `documents` (`documentid`, `companyid`, `add_document`, `orderid`) VALUES
(30, NULL, 'as.png', 5);

-- --------------------------------------------------------

--
-- Table structure for table `estimate`
--

CREATE TABLE `estimate` (
  `estimateid` int(11) NOT NULL,
  `estimate_number` varchar(255) DEFAULT NULL,
  `estdate` date DEFAULT NULL,
  `duedate` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `emailon` varchar(255) DEFAULT NULL,
  `printon` varchar(255) DEFAULT NULL,
  `smson` varchar(255) DEFAULT NULL,
  `esttot` int(11) DEFAULT NULL,
  `totpaid` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `extracostname` varchar(255) DEFAULT NULL,
  `extracost` int(11) DEFAULT NULL,
  `template` varchar(255) DEFAULT NULL,
  `salesper` varchar(255) DEFAULT NULL,
  `discourate` int(11) DEFAULT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `title_text` varchar(255) NOT NULL,
  `header_text` varchar(255) NOT NULL,
  `footer_text` varchar(255) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `term_of_payment` varchar(255) NOT NULL,
  `terms` varchar(255) NOT NULL,
  `comments` varchar(255) NOT NULL,
  `private_notes` varchar(255) NOT NULL,
  `tax2` int(11) NOT NULL,
  `orderref` varchar(255) NOT NULL,
  `subtotal` int(11) NOT NULL,
  `extracostt` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  `ttax1` int(11) NOT NULL,
  `ttax2` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `estimate`
--

INSERT INTO `estimate` (`estimateid`, `estimate_number`, `estdate`, `duedate`, `status`, `emailon`, `printon`, `smson`, `esttot`, `totpaid`, `balance`, `extracostname`, `extracost`, `template`, `salesper`, `discourate`, `tax1`, `category`, `businessname`, `businessaddress`, `shipname`, `shipaddress`, `cpemail`, `cpmobileforsms`, `title_text`, `header_text`, `footer_text`, `companyid`, `customerid`, `Productserviceid`, `term_of_payment`, `terms`, `comments`, `private_notes`, `tax2`, `orderref`, `subtotal`, `extracostt`, `discount`, `ttax1`, `ttax2`) VALUES
(1, '146', '2022-04-19', '2022-04-19', NULL, NULL, NULL, NULL, 25254, 54, 122121, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'adda', 'afd', 'asd', 'as', 'sa', '', '', '', NULL, NULL, NULL, '', '', '', '', 0, '', 4500, 0, 0, 0, 0),
(2, NULL, '2022-04-23', '2022-04-23', NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'ad', 'adda', 'afd', 'asd', 'as', 'sa', '', '', '', NULL, NULL, NULL, '', '', '', '', 0, '', 0, 0, 0, 0, 0),
(3, NULL, '2022-04-23', '2022-04-23', 'Draft', NULL, NULL, NULL, 0, NULL, NULL, '', 0, '', '', 0, 5, '', 'ad hello', 'adda', 'afd', 'asd', 'as', 'sa', '', '', '', NULL, NULL, NULL, '', '', '', '', 0, '', 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `expenses`
--

CREATE TABLE `expenses` (
  `expensesid` int(11) NOT NULL,
  `customerid` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `expense_amount` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `vendor` varchar(255) DEFAULT NULL,
  `catagory` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `staff_members` varchar(255) DEFAULT NULL,
  `taxable` varchar(255) DEFAULT NULL,
  `customer` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `rebillable` varchar(255) DEFAULT NULL,
  `invoiced` varchar(255) DEFAULT NULL,
  `id_sku` int(11) DEFAULT NULL,
  `rebill_amount` int(11) DEFAULT NULL,
  `assign_customer` varchar(255) DEFAULT NULL,
  `receipt` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `extra_cost_name`
--

CREATE TABLE `extra_cost_name` (
  `extra_cost_nameid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `extra_cost_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `header_and_footer`
--

CREATE TABLE `header_and_footer` (
  `headerandfooterid` int(11) NOT NULL,
  `companyid` int(11) NOT NULL,
  `headerandfooter` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE `invoice` (
  `invoiceid` int(11) NOT NULL,
  `invoice_number` varchar(255) DEFAULT NULL,
  `invodate` date DEFAULT NULL,
  `duedate` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `emailon` varchar(255) DEFAULT NULL,
  `printon` varchar(255) DEFAULT NULL,
  `smson` varchar(255) DEFAULT NULL,
  `invoicetot` int(11) DEFAULT NULL,
  `totpaid` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `extracostname` varchar(255) DEFAULT NULL,
  `extracost` int(11) DEFAULT NULL,
  `template` varchar(255) DEFAULT NULL,
  `salesper` varchar(255) DEFAULT NULL,
  `discourate` int(11) DEFAULT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `recurring_period` int(11) DEFAULT NULL,
  `recurring_period_month` varchar(255) DEFAULT NULL,
  `next_invoice` date DEFAULT NULL,
  `stop_recurring` date DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `discount` int(11) DEFAULT NULL,
  `orderid` int(11) DEFAULT NULL,
  `estimateid` int(11) DEFAULT NULL,
  `paymentid` int(11) NOT NULL,
  `terms` varchar(255) NOT NULL,
  `tax2` int(11) NOT NULL,
  `totalbeforetax` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoice`
--

INSERT INTO `invoice` (`invoiceid`, `invoice_number`, `invodate`, `duedate`, `status`, `emailon`, `printon`, `smson`, `invoicetot`, `totpaid`, `balance`, `extracostname`, `extracost`, `template`, `salesper`, `discourate`, `tax1`, `category`, `businessname`, `businessaddress`, `shipname`, `shipaddress`, `cpemail`, `cpmobileforsms`, `recurring_period`, `recurring_period_month`, `next_invoice`, `stop_recurring`, `companyid`, `customerid`, `Productserviceid`, `discount`, `orderid`, `estimateid`, `paymentid`, `terms`, `tax2`, `totalbeforetax`, `quantity`) VALUES
(1, '002', '2022-06-01', '2022-06-30', NULL, NULL, NULL, NULL, 18000, 9000, 9000, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer1', 'cust1address', 'Customer1', 'cust1address', 'oqoq@gmail', '12345', NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL, 2, NULL, 0, '', 0, 0, 3),
(62, '004', '2022-06-01', '2022-06-29', NULL, NULL, NULL, NULL, 6000, 3000, 3000, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer6', 'cust6address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL, 5, NULL, 0, '', 0, 0, 0),
(63, '0021', '2022-06-07', '2022-06-29', NULL, NULL, NULL, NULL, 20000, 10000, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer1', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL, 9, NULL, 0, '', 0, 0, 0),
(65, '0005', '2022-06-01', '2022-06-29', NULL, NULL, NULL, NULL, 5000, 2500, 2500, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', 2112, NULL, NULL, NULL, NULL, NULL, 8, NULL, 2, NULL, 0, '', 0, 0, 0),
(66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 12121, 1212, 1221212, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL, 0, '', 0, 0, 0),
(67, '2121', NULL, NULL, NULL, NULL, NULL, NULL, 111, 111, 111, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer3', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, 0, '', 0, 0, 0),
(68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 200, 10010, 144, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL, 0, '', 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `invoice_private_notes`
--

CREATE TABLE `invoice_private_notes` (
  `invoicepvtnoteid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `private_notes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `invoice_settings`
--

CREATE TABLE `invoice_settings` (
  `invoice_prefix` varchar(255) DEFAULT NULL,
  `starting_invoice_number` varchar(255) DEFAULT NULL,
  `bgcolour` varchar(255) DEFAULT NULL,
  `invoice` varchar(255) DEFAULT NULL,
  `invoice2` varchar(255) DEFAULT NULL,
  `invoice_date` varchar(255) DEFAULT NULL,
  `order_ref` varchar(255) DEFAULT NULL,
  `terms` varchar(255) DEFAULT NULL,
  `invoice_to` varchar(255) DEFAULT NULL,
  `ship_to` varchar(255) DEFAULT NULL,
  `id_sku` varchar(255) DEFAULT NULL,
  `product_service` varchar(255) DEFAULT NULL,
  `quantity` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `unit_price` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `subtotal` varchar(255) DEFAULT NULL,
  `discount` varchar(255) DEFAULT NULL,
  `discount_rate` varchar(255) DEFAULT NULL,
  `tax1` varchar(255) DEFAULT NULL,
  `invoice_total` varchar(255) DEFAULT NULL,
  `total_paid` varchar(255) DEFAULT NULL,
  `balance` varchar(255) DEFAULT NULL,
  `terms_conditions` varchar(255) DEFAULT NULL,
  `tax_exempted` varchar(255) DEFAULT NULL,
  `page` varchar(255) DEFAULT NULL,
  `of` varchar(255) DEFAULT NULL,
  `terms_notes` varchar(310) DEFAULT NULL,
  `settingsid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoice_settings`
--

INSERT INTO `invoice_settings` (`invoice_prefix`, `starting_invoice_number`, `bgcolour`, `invoice`, `invoice2`, `invoice_date`, `order_ref`, `terms`, `invoice_to`, `ship_to`, `id_sku`, `product_service`, `quantity`, `description`, `unit_price`, `price`, `subtotal`, `discount`, `discount_rate`, `tax1`, `invoice_total`, `total_paid`, `balance`, `terms_conditions`, `tax_exempted`, `page`, `of`, `terms_notes`, `settingsid`, `companyid`) VALUES
('INV', '13', 'Lime', 'Invoice\n\n\n\n\n\n\n', 'Invoice#\n\n\n\n\n\n\n', 'Invoice date\n\n\n\n\n\n\n', 'Order ref.#\n\n\n\n\n\n\n', 'Terms\n\n\n\n\n\n\n', 'Invoice to\n\n\n\n\n\n\n', 'Ship tosdsad\n\n\n\n\n\n\n', 'ID/SKU\n\n\n\n\n\n\n', 'Product/Service\n\n\n\n\n\n\n', 'Quantity\n\n\n\n\n\n\n', 'Description\n\n\n\n\n\n\n', 'Unit Price\n\n\n\n\n\n\n', 'Price\n\n\n\n\n\n\n', 'Subtotal\n\n\n\n\n\n\n', 'Discount\n\n\n\n\n\n\n', 'Discount rate\n\n\n\n\n\n\n', 'TAX1\n\n\n\n\n\n\n', 'Invoice Total\n\n\n\n\n\n\n', 'Total Paid\n\n\n\n\n\n\n', 'Balance\n\n\n\n\n\n\n', 'Terms and Conditions\n\n\n\n\n\n\n', 'Tax Exempted\n\n\n\n\n\n\n', 'Page\n\n\n\n\n\n\n', 'of\n\n\n\n\n\n\n', 'Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods, and agrees to be bound to these contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller.\n\n\n', 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `markinvoice`
--

CREATE TABLE `markinvoice` (
  `paymentid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `invoice_balance` varchar(255) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `paid_by` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `full_paid` varchar(255) DEFAULT NULL,
  `payment_receipt` varchar(255) DEFAULT NULL,
  `attach_invoice` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `orderid` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `emailed_on` date DEFAULT NULL,
  `printed_on` date DEFAULT NULL,
  `sms_on` date DEFAULT NULL,
  `Order_total` int(11) DEFAULT NULL,
  `extra_cost_name` varchar(300) DEFAULT NULL,
  `extra_cost` int(11) DEFAULT NULL,
  `template` varchar(500) DEFAULT NULL,
  `sales_person` varchar(300) DEFAULT NULL,
  `discount_rate` int(11) DEFAULT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category` varchar(300) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL,
  `sum_discount` int(11) DEFAULT NULL,
  `sum_tax` int(11) DEFAULT NULL,
  `sum_subtotal` int(11) DEFAULT NULL,
  `private_notes` varchar(500) DEFAULT NULL,
  `totalbeforetax` int(11) NOT NULL,
  `tax2` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`orderid`, `order_date`, `due_date`, `businessname`, `status`, `emailed_on`, `printed_on`, `sms_on`, `Order_total`, `extra_cost_name`, `extra_cost`, `template`, `sales_person`, `discount_rate`, `tax1`, `category`, `businessaddress`, `shipname`, `shipaddress`, `cpemail`, `cpmobileforsms`, `companyid`, `Productserviceid`, `customerid`, `sum_discount`, `sum_tax`, `sum_subtotal`, `private_notes`, `totalbeforetax`, `tax2`) VALUES
(1, '2022-04-18', '2022-04-18', 'Customer3', 'Invoiced', NULL, NULL, NULL, 27, 'saaads', 13, 'adsd', 'asd', 2, 21, 'asaads', 'cust3address', 'adadad', 'adadad,adadad', 'asc@ad', '2323', NULL, NULL, NULL, 0, 2, 12, '', 0, 0),
(5, '2022-04-11', '2022-04-18', 'Customer2', 'Draft', NULL, '2022-04-18', NULL, 148, 'saaads', 34, 'adsd', '', 2, 6, 'sdfa safd', 'cust2address', 'King', 'King,ing', 'you@gmail', '98765', NULL, NULL, NULL, 2, 6, 108, 'wsaera', 0, 0),
(6, '2022-04-20', '2022-04-20', 'ad', NULL, NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'adda', 'afd', 'asd', 'as', 'sa', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0),
(7, '2022-04-20', '2022-04-20', 'ad', NULL, NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'adda', 'afd', 'asd', 'as', 'sa', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `order_settings`
--

CREATE TABLE `order_settings` (
  `invoice_prefix` varchar(255) DEFAULT NULL,
  `starting_invoice_number` varchar(255) DEFAULT NULL,
  `bgcolour` varchar(255) DEFAULT NULL,
  `orders` varchar(255) DEFAULT NULL,
  `order2` varchar(255) DEFAULT NULL,
  `order_date` varchar(255) DEFAULT NULL,
  `due_date` varchar(255) DEFAULT NULL,
  `order_to` varchar(255) DEFAULT NULL,
  `order_total` varchar(255) DEFAULT NULL,
  `footer_note` varchar(310) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `settingsid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_settings`
--

INSERT INTO `order_settings` (`invoice_prefix`, `starting_invoice_number`, `bgcolour`, `orders`, `order2`, `order_date`, `due_date`, `order_to`, `order_total`, `footer_note`, `companyid`, `settingsid`) VALUES
('ORD', '10', 'Default', 'Order\n\n\n\n\n\n\n', 'Order#\n\n\n\n\n\n\n', 'Order date\n\n\n\n\n\n\n', 'Due date\n\n\n\n\n\n\n', 'Order to\n\n\n\n\n\n\n', 'Order total\n\n\n\n\n\n\n', 'Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods, and agrees to be bound to these contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller.\n\n\n', NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `invoiceid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `show_paid` int(11) DEFAULT NULL,
  `send_payment` int(11) DEFAULT NULL,
  `insert_paypal` int(11) DEFAULT NULL,
  `attach_updated` int(11) DEFAULT NULL,
  `payment_receipt` varchar(255) DEFAULT NULL,
  `payment_invoice` varchar(255) DEFAULT NULL,
  `amount_received` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `payment_received` varchar(255) DEFAULT NULL,
  `payment_rece` varchar(255) DEFAULT NULL,
  `payment_date` varchar(255) DEFAULT NULL,
  `payment_amount` varchar(255) DEFAULT NULL,
  `total_amount` varchar(255) DEFAULT NULL,
  `total_paid` varchar(255) DEFAULT NULL,
  `balance_due` varchar(255) DEFAULT NULL,
  `prefix` varchar(255) DEFAULT NULL,
  `load_logo` varchar(255) DEFAULT NULL,
  `load_button` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`invoiceid`, `companyid`, `show_paid`, `send_payment`, `insert_paypal`, `attach_updated`, `payment_receipt`, `payment_invoice`, `amount_received`, `description`, `payment_received`, `payment_rece`, `payment_date`, `payment_amount`, `total_amount`, `total_paid`, `balance_due`, `prefix`, `load_logo`, `load_button`) VALUES
(65, NULL, 1, 1, 1, 1, 'Payment Receipt    payment', 'Payment for Invoice#   INV001', 'Amount received from:  customer', 'Description:   dfghjk', 'Payment Received in:   7/9/2022', 'Payment Receipt#:   dfghjk', 'Payment Date:  09/5/2022', 'Payment Amount:   4000', 'Total Amount Due  3000', 'Total Paid:1000', 'Balance Due  0', 'RCPT    cfgyj', 'create p oder.png', 'dlc.png');

-- --------------------------------------------------------

--
-- Table structure for table `porder`
--

CREATE TABLE `porder` (
  `porderid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `porderdate` varchar(255) DEFAULT NULL,
  `duedate` varchar(255) DEFAULT NULL,
  `customname` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `emailon` varchar(255) DEFAULT NULL,
  `printon` varchar(255) DEFAULT NULL,
  `smson` varchar(255) DEFAULT NULL,
  `ordertot` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `extracostname` varchar(255) DEFAULT NULL,
  `extracost` int(11) DEFAULT NULL,
  `template` varchar(255) DEFAULT NULL,
  `salesper` varchar(255) DEFAULT NULL,
  `discourate` int(11) DEFAULT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL,
  `businessaddress` varchar(255) DEFAULT NULL,
  `shipname` varchar(255) DEFAULT NULL,
  `shipaddress` varchar(255) DEFAULT NULL,
  `cpemail` varchar(255) DEFAULT NULL,
  `cpmobileforsms` varchar(255) DEFAULT NULL,
  `businessname` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `porder`
--

INSERT INTO `porder` (`porderid`, `companyid`, `porderdate`, `duedate`, `customname`, `status`, `emailon`, `printon`, `smson`, `ordertot`, `total`, `extracostname`, `extracost`, `template`, `salesper`, `discourate`, `tax1`, `category`, `Productserviceid`, `customerid`, `businessaddress`, `shipname`, `shipaddress`, `cpemail`, `cpmobileforsms`, `businessname`) VALUES
(5, 10, '2022-06-01', '2022-06-20', 'Customer2', NULL, NULL, NULL, NULL, 455454, 455454, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Customer2');

-- --------------------------------------------------------

--
-- Table structure for table `productservice`
--

CREATE TABLE `productservice` (
  `Productserviceid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `sku` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `unitprice` varchar(255) DEFAULT NULL,
  `peices` int(11) DEFAULT NULL,
  `cost` varchar(255) DEFAULT NULL,
  `taxable` varchar(255) DEFAULT NULL,
  `priceminuscost` int(11) DEFAULT NULL,
  `serviceornot` varchar(255) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `stocklimit` int(11) DEFAULT NULL,
  `warehouse` varchar(255) DEFAULT NULL,
  `privatenote` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `productservice`
--

INSERT INTO `productservice` (`Productserviceid`, `companyid`, `sku`, `category`, `name`, `description`, `status`, `unitprice`, `peices`, `cost`, `taxable`, `priceminuscost`, `serviceornot`, `stock`, `stocklimit`, `warehouse`, `privatenote`, `image`, `quantity`) VALUES
(1, NULL, 1, 'Default', 'Pencil', 'Black', '1', '10', 10, '5', '1', 5, '1', 0, 0, '', NULL, NULL, NULL),
(3, NULL, 3, 'Default', 'Bench', 'Wooden', '0', '12', 0, '5', '0', 7, '0', 3, 2, 'Section A', NULL, NULL, NULL),
(4, NULL, 4, 'Default', 'Chair', 'Plastic', '1', '50', 8, '15', '1', 35, '0', 9, 20, 'Section B', NULL, NULL, NULL),
(5, NULL, 5, 'Default', 'dress', 'asddds', '0', '50', 100, '10', '0', 40, '0', 100, 20, 'section1', NULL, NULL, NULL),
(6, NULL, 6, 'Default', 'asdsaa', 'dsaf', '0', '100', 20, '20', '0', 80, '1', 0, 0, '', NULL, NULL, NULL),
(7, NULL, 7, 'Default', 'sadsfsfad', 'asf', '0', '60', 10, '30', '0', 30, '0', 100, 20, 'section 1', 'asdada', 'as.png', NULL),
(8, NULL, 8, 'Default', 'qweeeee', 'fda', '0', '50', 0, '140', '0', 50, '1', 0, 0, '', '', NULL, 3),
(9, NULL, 10, 'Default', 'qedf', 'fd', '0', '60', 12, '3', '0', 57, '0', 100, 20, 'wre', 'ddwe', 'as.png', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `recurring`
--

CREATE TABLE `recurring` (
  `recurringid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `recurring_period` int(11) DEFAULT NULL,
  `next_invoice` date DEFAULT NULL,
  `stop_recurring` date DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sms`
--

CREATE TABLE `sms` (
  `smsid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `sms_type` varchar(255) DEFAULT NULL,
  `sms_text` varchar(255) DEFAULT NULL,
  `customerid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sms_account`
--

CREATE TABLE `sms_account` (
  `smsaccountid` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `api_secret` varchar(255) DEFAULT NULL,
  `route` varchar(255) DEFAULT NULL,
  `api_key` varchar(255) DEFAULT NULL,
  `smsid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `storingproduct`
--

CREATE TABLE `storingproduct` (
  `orderid` int(11) DEFAULT NULL,
  `estimateid` int(11) DEFAULT NULL,
  `invoiceid` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `sku` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `unitprice` int(11) DEFAULT NULL,
  `peices` int(255) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `taxable` varchar(255) DEFAULT NULL,
  `priceminuscost` int(11) DEFAULT NULL,
  `serviceornot` varchar(255) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `stocklimit` int(11) DEFAULT NULL,
  `warehouse` varchar(255) DEFAULT NULL,
  `privatenote` varchar(255) DEFAULT NULL,
  `image` longblob DEFAULT NULL,
  `storingproductid` int(11) NOT NULL,
  `Productserviceid` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `porderid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `storingproduct`
--

INSERT INTO `storingproduct` (`orderid`, `estimateid`, `invoiceid`, `companyid`, `sku`, `category`, `name`, `description`, `status`, `unitprice`, `peices`, `cost`, `taxable`, `priceminuscost`, `serviceornot`, `stock`, `stocklimit`, `warehouse`, `privatenote`, `image`, `storingproductid`, `Productserviceid`, `quantity`, `porderid`) VALUES
(1, NULL, NULL, NULL, '3', 'Default', 'Bench', 'Wooden', '0', 12, 0, 5, '0', 7, '0', 3, 2, 'Section A', 'Long lasting...........', NULL, 705, 3, 1, NULL),
(5, NULL, NULL, NULL, '4', 'Default', 'Chair', 'Plastic', '1', 50, 8, 15, '1', 35, '0', 9, 20, 'Section B', 'Flexible', NULL, 707, 4, 2, NULL),
(5, NULL, NULL, NULL, '2', 'Default', 'Mobile', 'Vivo', '0', 10, 8, 5, '0', 5, '1', 0, 8, '', 'good quality', NULL, 710, 2, 1, NULL),
(6, NULL, NULL, NULL, '6', 'Default', 'asdsaa', 'dsaf', '0', 100, 20, 20, '0', 80, '1', 0, 0, '', NULL, NULL, 718, 6, 1, NULL),
(6, NULL, NULL, NULL, '12', 'Default', 'asdasdwe', 'wsa', '0', 0, 0, 0, '0', 0, '0', 0, 0, '', '', NULL, 719, 10, 1, NULL),
(7, NULL, NULL, NULL, '7', 'Default', 'sadsfsfad', 'asf', '0', 60, 10, 30, '0', 30, '0', 100, 20, 'section 1', 'asdada', NULL, 720, 7, 1, NULL),
(7, NULL, NULL, NULL, '322', 'Default', 'wsadas', 'asd', '0', 0, 0, 0, '0', 0, '1', 0, 0, '', '', NULL, 721, 322, 1, NULL),
(NULL, 2, NULL, NULL, '5', 'Default', 'dress', 'asddds', '0', 50, 100, 10, '0', 40, '0', 100, 20, 'section1', NULL, NULL, 722, 5, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `terms_of_payment`
--

CREATE TABLE `terms_of_payment` (
  `terms_of_paymentID` int(11) NOT NULL,
  `companyid` int(11) NOT NULL,
  `terms_of_payment` varchar(255) DEFAULT NULL,
  `Date_shift` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userID` int(11) NOT NULL,
  `companyid` int(11) DEFAULT NULL,
  `displayloginscreen` int(11) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `confirm_password` varchar(255) DEFAULT NULL,
  `create_invoice` int(11) DEFAULT NULL,
  `delete_invoice` int(11) DEFAULT NULL,
  `void_invoice` int(11) DEFAULT NULL,
  `mark_invoice_as_paid` int(11) DEFAULT NULL,
  `create_order` int(11) DEFAULT NULL,
  `delete_order` int(11) DEFAULT NULL,
  `turn_order_into_invoice` int(11) DEFAULT NULL,
  `send_sms_nofitication` int(11) DEFAULT NULL,
  `create_estimate` int(11) DEFAULT NULL,
  `delete_estimate` int(11) DEFAULT NULL,
  `turn_oestimate_into_invoice` int(11) DEFAULT NULL,
  `create_expense` int(11) DEFAULT NULL,
  `delete_expense` int(11) DEFAULT NULL,
  `rebill_exprense` int(11) DEFAULT NULL,
  `create_customer` int(11) DEFAULT NULL,
  `delete_customer` int(11) DEFAULT NULL,
  `import_customer` int(11) DEFAULT NULL,
  `create_product_service` int(11) DEFAULT NULL,
  `delete_product_service` int(11) DEFAULT NULL,
  `import_product_service` int(11) DEFAULT NULL,
  `run_reports` int(11) DEFAULT NULL,
  `generate_recurring_invoice` int(11) DEFAULT NULL,
  `create_purchase_order` int(11) DEFAULT NULL,
  `delete_purchase_order` int(11) DEFAULT NULL,
  `modify_invoice_settings` int(11) DEFAULT NULL,
  `modify_order_settings` int(11) DEFAULT NULL,
  `modify_estimate_settings` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`commentid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`companyid`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customerid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `documents`
--
ALTER TABLE `documents`
  ADD PRIMARY KEY (`documentid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `estimate`
--
ALTER TABLE `estimate`
  ADD PRIMARY KEY (`estimateid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `Productserviceid` (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `expenses`
--
ALTER TABLE `expenses`
  ADD PRIMARY KEY (`expensesid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `extra_cost_name`
--
ALTER TABLE `extra_cost_name`
  ADD PRIMARY KEY (`extra_cost_nameid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `header_and_footer`
--
ALTER TABLE `header_and_footer`
  ADD PRIMARY KEY (`headerandfooterid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`invoiceid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `Productserviceid` (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `invoice_private_notes`
--
ALTER TABLE `invoice_private_notes`
  ADD PRIMARY KEY (`invoicepvtnoteid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `invoice_settings`
--
ALTER TABLE `invoice_settings`
  ADD PRIMARY KEY (`settingsid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `markinvoice`
--
ALTER TABLE `markinvoice`
  ADD PRIMARY KEY (`paymentid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`orderid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `Productserviceid` (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `order_settings`
--
ALTER TABLE `order_settings`
  ADD PRIMARY KEY (`settingsid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`invoiceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `porder`
--
ALTER TABLE `porder`
  ADD PRIMARY KEY (`porderid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `Productserviceid` (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `productservice`
--
ALTER TABLE `productservice`
  ADD PRIMARY KEY (`Productserviceid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `recurring`
--
ALTER TABLE `recurring`
  ADD PRIMARY KEY (`recurringid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `sms`
--
ALTER TABLE `sms`
  ADD PRIMARY KEY (`smsid`),
  ADD KEY `customerid` (`customerid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `sms_account`
--
ALTER TABLE `sms_account`
  ADD PRIMARY KEY (`smsaccountid`),
  ADD KEY `smsid` (`smsid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `storingproduct`
--
ALTER TABLE `storingproduct`
  ADD PRIMARY KEY (`storingproductid`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `terms_of_payment`
--
ALTER TABLE `terms_of_payment`
  ADD PRIMARY KEY (`terms_of_paymentID`),
  ADD KEY `companyid` (`companyid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`),
  ADD KEY `companyid` (`companyid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `commentid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `companyid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15583;

--
-- AUTO_INCREMENT for table `documents`
--
ALTER TABLE `documents`
  MODIFY `documentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `estimate`
--
ALTER TABLE `estimate`
  MODIFY `estimateid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT for table `expenses`
--
ALTER TABLE `expenses`
  MODIFY `expensesid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `extra_cost_name`
--
ALTER TABLE `extra_cost_name`
  MODIFY `extra_cost_nameid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT for table `header_and_footer`
--
ALTER TABLE `header_and_footer`
  MODIFY `headerandfooterid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `invoice`
--
ALTER TABLE `invoice`
  MODIFY `invoiceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `invoice_private_notes`
--
ALTER TABLE `invoice_private_notes`
  MODIFY `invoicepvtnoteid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `markinvoice`
--
ALTER TABLE `markinvoice`
  MODIFY `paymentid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `orderid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `invoiceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `porder`
--
ALTER TABLE `porder`
  MODIFY `porderid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `productservice`
--
ALTER TABLE `productservice`
  MODIFY `Productserviceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=323;

--
-- AUTO_INCREMENT for table `recurring`
--
ALTER TABLE `recurring`
  MODIFY `recurringid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sms`
--
ALTER TABLE `sms`
  MODIFY `smsid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sms_account`
--
ALTER TABLE `sms_account`
  MODIFY `smsaccountid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `storingproduct`
--
ALTER TABLE `storingproduct`
  MODIFY `storingproductid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=723;

--
-- AUTO_INCREMENT for table `terms_of_payment`
--
ALTER TABLE `terms_of_payment`
  MODIFY `terms_of_paymentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `documents`
--
ALTER TABLE `documents`
  ADD CONSTRAINT `documents_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `estimate`
--
ALTER TABLE `estimate`
  ADD CONSTRAINT `estimate_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `estimate_ibfk_2` FOREIGN KEY (`Productserviceid`) REFERENCES `productservice` (`Productserviceid`) ON DELETE CASCADE,
  ADD CONSTRAINT `estimate_ibfk_3` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `expenses`
--
ALTER TABLE `expenses`
  ADD CONSTRAINT `expenses_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `expenses_ibfk_2` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `extra_cost_name`
--
ALTER TABLE `extra_cost_name`
  ADD CONSTRAINT `extra_cost_name_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);

--
-- Constraints for table `header_and_footer`
--
ALTER TABLE `header_and_footer`
  ADD CONSTRAINT `header_and_footer_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);

--
-- Constraints for table `invoice_private_notes`
--
ALTER TABLE `invoice_private_notes`
  ADD CONSTRAINT `invoice_private_notes_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `invoice_settings`
--
ALTER TABLE `invoice_settings`
  ADD CONSTRAINT `invoice_settings_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);

--
-- Constraints for table `markinvoice`
--
ALTER TABLE `markinvoice`
  ADD CONSTRAINT `markinvoice_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `order_settings`
--
ALTER TABLE `order_settings`
  ADD CONSTRAINT `order_settings_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `porder`
--
ALTER TABLE `porder`
  ADD CONSTRAINT `porder_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `porder_ibfk_2` FOREIGN KEY (`Productserviceid`) REFERENCES `productservice` (`Productserviceid`) ON DELETE CASCADE,
  ADD CONSTRAINT `porder_ibfk_3` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `productservice`
--
ALTER TABLE `productservice`
  ADD CONSTRAINT `productservice_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `recurring`
--
ALTER TABLE `recurring`
  ADD CONSTRAINT `recurring_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `recurring_ibfk_2` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `sms`
--
ALTER TABLE `sms`
  ADD CONSTRAINT `sms_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`) ON DELETE CASCADE,
  ADD CONSTRAINT `sms_ibfk_2` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `sms_account`
--
ALTER TABLE `sms_account`
  ADD CONSTRAINT `sms_account_ibfk_1` FOREIGN KEY (`smsid`) REFERENCES `sms` (`smsid`) ON DELETE CASCADE,
  ADD CONSTRAINT `sms_account_ibfk_2` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `storingproduct`
--
ALTER TABLE `storingproduct`
  ADD CONSTRAINT `storingproduct_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE CASCADE;

--
-- Constraints for table `terms_of_payment`
--
ALTER TABLE `terms_of_payment`
  ADD CONSTRAINT `terms_of_payment_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
