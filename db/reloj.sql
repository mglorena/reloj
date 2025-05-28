-- reloj.Asistencia definition

CREATE TABLE `Asistencia` (
  `Legajo` int(11) DEFAULT NULL,
  `Fecha` datetime DEFAULT NULL,
  `Tipo` varchar(100) DEFAULT NULL,
  `AsistenciaId` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`AsistenciaId`)
) ENGINE=InnoDB AUTO_INCREMENT=11503 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- reloj.Personas definition

CREATE TABLE `Personas` (
  `PersonaId` int(11) NOT NULL AUTO_INCREMENT,
  `Apellido` varchar(150) NOT NULL,
  `Nombre` varchar(150) NOT NULL,
  `Legajo` int(11) NOT NULL,
  `TipoDNI` varchar(5) DEFAULT NULL,
  `CargoDesc` varchar(150) DEFAULT NULL,
  `Categoria` varchar(45) DEFAULT NULL,
  `UserId` int(11) DEFAULT NULL,
  `Telefono` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Domicilio` varchar(150) DEFAULT NULL,
  `Active` bit(1) DEFAULT NULL,
  `VacacionesDias` int(11) DEFAULT NULL,
  `Observaciones` varchar(500) DEFAULT NULL,
  `Antiguedad` int(11) DEFAULT NULL,
  `Compensatorio` int(11) DEFAULT NULL,
  `CUIL` datetime DEFAULT NULL,
  `FechaNac` datetime DEFAULT NULL,
  `FechaIngreso` datetime DEFAULT NULL,
  `DNI` varchar(45) DEFAULT NULL,
  `AntAnses` int(11) DEFAULT NULL,
  `Turno` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PersonaId`)
) ENGINE=InnoDB AUTO_INCREMENT=347 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;