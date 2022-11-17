-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cookies_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cookies_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cookies_schema` DEFAULT CHARACTER SET utf8 ;
USE `cookies_schema` ;

-- -----------------------------------------------------
-- Table `cookies_schema`.`cookie_order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cookies_schema`.`cookie_order` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `customer_name` VARCHAR(255) NULL,
  `cookie_type` VARCHAR(255) NULL,
  `cookie_box_qty` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
