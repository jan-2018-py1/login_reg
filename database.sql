-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema login_reg_jan_2018
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema login_reg_jan_2018
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `login_reg_jan_2018` DEFAULT CHARACTER SET utf8 ;
USE `login_reg_jan_2018` ;

-- -----------------------------------------------------
-- Table `login_reg_jan_2018`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_reg_jan_2018`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
