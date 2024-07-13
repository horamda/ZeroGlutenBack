-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-07-2024 a las 01:08:03
-- Versión del servidor: 11.3.2-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `final`
--
CREATE DATABASE IF NOT EXISTS `final` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `final`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `catalogo`
--

CREATE TABLE `catalogo` (
  `id` int(11) NOT NULL,
  `nombre` char(30) NOT NULL,
  `precio` varchar(7) NOT NULL,
  `imagen` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `catalogo`
--

INSERT INTO `catalogo` (`id`, `nombre`, `precio`, `imagen`) VALUES
(10, 'Hamburguesa', '1000', 'HamburgVegetal.png'),
(11, 'Helado', '5000', 'gelato.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `formulario`
--

CREATE TABLE `formulario` (
  `id` int(11) NOT NULL,
  `numero_consulta` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `motivo_contacto` varchar(50) NOT NULL,
  `serv_utilizado` varchar(50) NOT NULL,
  `ubicacion` varchar(50) NOT NULL,
  `mensaje` text NOT NULL,
  `newsletter` varchar(10) DEFAULT NULL,
  `enviado` datetime DEFAULT NULL,
  `leido` tinyint(1) DEFAULT 0
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `formulario`
--

INSERT INTO `formulario` (`id`, `numero_consulta`, `nombre`, `email`, `motivo_contacto`, `serv_utilizado`, `ubicacion`, `mensaje`, `newsletter`, `enviado`, `leido`) VALUES
(10, 'C002', 'Ana', 'zerogluten.adm@gmail.com', 'consulta', 'Tienda online', 'Buenos Aires - GBA', 'Me llega el mail de confirmacion? prueba 1', 'SÃ­', '2024-07-11 22:22:05', 0),
(9, 'C001', 'Paloma', 'palomisc9@gmail.com', 'Opinion', 'Tienda online', 'Buenos Aires - GBA', 'Holaa! me encanta la pagina, sigan asi :)', 'SÃ­', '2024-07-11 22:21:14', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurants`
--

CREATE TABLE `restaurants` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `province` varchar(255) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `restaurants`
--

INSERT INTO `restaurants` (`id`, `name`, `address`, `province`, `latitude`, `longitude`, `phone`, `website`, `image`) VALUES
(3, 'restaurante 2', 'direccion 2', 'buenos aires', 10, 15, '36699777', 'http://www.pepe2.com.ar', 'r2.jpg'),
(5, 'restaurante 3', 'direccion 3', 'buenos aires', 10, 15, '36699777', 'http://www.pepe2.com.ar', 'r4.jpg'),
(6, 'restaurante 4', 'direccion 4', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r5.jpg'),
(7, 'restaurante 5', 'direccion 5', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r6.jpg'),
(8, 'restaurante 6', 'direccion 6', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r7.jpg'),
(9, 'restaurante 7', 'direccion 7', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r8.jpg'),
(10, 'restaurante 8', 'direccion 8', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r9.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `correo` varchar(60) NOT NULL,
  `contrasenia` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `correo`, `contrasenia`) VALUES
(1, 'albrengi@hotmail.com', 'admzero24');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `formulario`
--
ALTER TABLE `formulario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `formulario`
--
ALTER TABLE `formulario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- Base de datos: `restaurant_db`
--
CREATE DATABASE IF NOT EXISTS `restaurant_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `restaurant_db`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurants`
--

CREATE TABLE `restaurants` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `province` varchar(255) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `restaurants`
--
ALTER TABLE `restaurants`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `restaurants`
--
ALTER TABLE `restaurants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Base de datos: `restaurant_db_new`
--
CREATE DATABASE IF NOT EXISTS `restaurant_db_new` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `restaurant_db_new`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurants`
--

CREATE TABLE `restaurants` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `province` varchar(255) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `restaurants`
--

INSERT INTO `restaurants` (`id`, `name`, `address`, `province`, `latitude`, `longitude`, `phone`, `website`, `image`) VALUES
(3, 'restaurante 2', 'direccion 2', 'buenos aires', 10, 15, '36699777', 'http://www.pepe2.com.ar', 'r2.jpg'),
(5, 'restaurante 3', 'direccion 3', 'buenos aires', 10, 15, '36699777', 'http://www.pepe2.com.ar', 'r4.jpg'),
(6, 'restaurante 4', 'direccion 4', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r5.jpg'),
(7, 'restaurante 5', 'direccion 5', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r6.jpg'),
(8, 'restaurante 6', 'direccion 6', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r7.jpg'),
(9, 'restaurante 7', 'direccion 7', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r8.jpg'),
(10, 'restaurante 8', 'direccion 8', 'buenos aires', 15, 15, '36699777', 'http://www.pepe4.com.ar', 'r9.jpg'),
(12, 'restaurate pepe', 'direccion x', 'salta', 523, 525, '891321321321', 'https://www.pepe.com', 'celicity.png');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `restaurants`
--
ALTER TABLE `restaurants`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `restaurants`
--
ALTER TABLE `restaurants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- Base de datos: `sistemakpi`
--
CREATE DATABASE IF NOT EXISTS `sistemakpi` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `sistemakpi`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `kpi`
--

CREATE TABLE `kpi` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `repartidor`
--

CREATE TABLE `repartidor` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `sucursal` varchar(255) DEFAULT NULL,
  `photo` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `repartidorkpi`
--

CREATE TABLE `repartidorkpi` (
  `id` int(11) NOT NULL,
  `repartidor_id` int(11) NOT NULL,
  `kpi_id` int(11) NOT NULL,
  `value` float NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT 0,
  `created_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `kpi`
--
ALTER TABLE `kpi`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `repartidor`
--
ALTER TABLE `repartidor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indices de la tabla `repartidorkpi`
--
ALTER TABLE `repartidorkpi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `repartidor_id` (`repartidor_id`),
  ADD KEY `kpi_id` (`kpi_id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `kpi`
--
ALTER TABLE `kpi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `repartidor`
--
ALTER TABLE `repartidor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `repartidorkpi`
--
ALTER TABLE `repartidorkpi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `repartidor`
--
ALTER TABLE `repartidor`
  ADD CONSTRAINT `repartidor_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `repartidorkpi`
--
ALTER TABLE `repartidorkpi`
  ADD CONSTRAINT `repartidorkpi_ibfk_1` FOREIGN KEY (`repartidor_id`) REFERENCES `repartidor` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `repartidorkpi_ibfk_2` FOREIGN KEY (`kpi_id`) REFERENCES `kpi` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
