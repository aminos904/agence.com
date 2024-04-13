-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : sam. 13 avr. 2024 à 04:54
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `agence`
--

-- --------------------------------------------------------

--
-- Structure de la table `dep`
--

CREATE TABLE `dep` (
  `id` int(11) NOT NULL COMMENT 'Primary Key',
  `nom` varchar(255) DEFAULT NULL,
  `emplacement` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `employes`
--

CREATE TABLE `employes` (
  `ID` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT 'NULL',
  `prenom` varchar(255) DEFAULT '''NULL''',
  `matricule` varchar(255) DEFAULT 'NULL',
  `fonction` varchar(255) DEFAULT NULL,
  `dep` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `employes`
--

INSERT INTO `employes` (`ID`, `nom`, `prenom`, `matricule`, `fonction`, `dep`) VALUES
(1, 'han', 'amn', '1131', 'tech', 'IT'),
(2, 'aahan', 'amdaddfn', '1fda131', 'tech', 'IT'),
(3, '1920', 'aaddd', '94', 'ds', 'ti'),
(5, 'asda', 'asdas', 'sas', 'sadas', 'asd'),
(6, 'hana', 'DKFK119191', 'amin', 'spec eng', 'ENG.'),
(8, 'saasd', '23456667', 'aaasa', 'dfd', 'sdfsd'),
(11, 'dcdss', '23456667', 'cdcd', 'sdcdsc', 'sdcd'),
(12, 'asa', '23456667', 'asas', 'asa', 'saas'),
(13, '1344', 'zx', 'czx', 'yhjyrt', 'gr'),
(15, '23213', 'sadsa', 'sdsd', 'fsdf', 'rt'),
(16, 'scsca', '234332', 'amincccc', 'fsd', 'dsf'),
(17, 'dfsd', 'dsf', 'ff', 'sdf', 'd');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL COMMENT 'Primary Key',
  `nom` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `hash` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `nom`, `username`, `password`, `hash`) VALUES
(1, 'amine', 'amin', 'amin', NULL),
(2, 'gfhfg', 'fhgh', 'fghg', 'gfhfg'),
(3, 'erg', 'erger', 'egr', 'erg'),
(5, 'dfsdfd', 'sdfsd', 'dsfd', 'dfsdfd');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `dep`
--
ALTER TABLE `dep`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `employes`
--
ALTER TABLE `employes`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `matricule` (`matricule`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`),
  ADD UNIQUE KEY `usename` (`username`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `username_2` (`username`),
  ADD UNIQUE KEY `username_3` (`username`),
  ADD UNIQUE KEY `nom_2` (`nom`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `dep`
--
ALTER TABLE `dep`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key';

--
-- AUTO_INCREMENT pour la table `employes`
--
ALTER TABLE `employes`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key', AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
