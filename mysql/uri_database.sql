CREATE SCHEMA `uri_db` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE `Alunos` (
  `perfil` VARCHAR(30) NOT NULL,
  `Pontos` FLOAT(10,2) NULL,
  `Nome` VARCHAR(50) NULL,
  `Faculdade` VARCHAR(20) NULL,
  `Pais` CHAR(2) NULL,
  `Status` INT(1) NULL,
  `DataCadastro` DATETIME NULL,
  `DiaSemana` VARCHAR(15) NULL,
  `MesAno` VARCHAR(15) NULL,
  `Ano` INT(4) NULL,
  PRIMARY KEY (`perfil`))
ENGINE = InnoDB;



CREATE TABLE `Faculdades` (
  `rank` INT(4) NOT NULL,
  `SiglaFaculdade` VARCHAR(30) NULL,
  `NomeFaculdade` VARCHAR(50) NULL,
  `Pais` CHAR(2) NULL,
  `Resolvidos` INT(7) NULL,
  `Estudantes` INT(5) NULL,
  PRIMARY KEY (`rank`))
ENGINE = InnoDB;


CREATE TABLE `Paises` (
  `Rank` INT(4) NOT NULL,
  `Pais` VARCHAR(45) NULL,
  `Resolvidos` INT(9) NULL,
  `Estudantes` INT(7) NULL,
  `Country` CHAR(2) NULL,
  `Continent` CHAR(2) NULL,
  `Latitude` GEOMETRY NULL,
  `Longitude` VARCHAR(45) NULL,
  PRIMARY KEY (`Rank`))
ENGINE = InnoDB;

