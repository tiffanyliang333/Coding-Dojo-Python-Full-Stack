-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema recipes_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema recipes_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recipes_schema` DEFAULT CHARACTER SET utf8 ;
USE `recipes_schema` ;

-- -----------------------------------------------------
-- Table `recipes_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipes_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipes_schema`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipes_schema`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `instructions` TEXT(1000) NULL,
  `date_made` DATETIME NULL DEFAULT NOW(),
  `under_30` VARCHAR(3) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_recipes_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `recipes_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
