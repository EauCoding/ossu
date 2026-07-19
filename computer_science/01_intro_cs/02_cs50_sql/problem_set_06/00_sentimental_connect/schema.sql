CREATE TABLE `users` (
    `id` INT AUTO_INCREMENT,
    `first_name` VARCHAR(50) NOT NULL,
    `last_name` VARCHAR(50) NOT NULL,
    `username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(150) NOT NULL,
    PRIMARY KEY(`id`)
)
;

CREATE TABLE `schools_and_universities` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `type` ENUM('Primary', 'Secondary', 'Higher Education') NOT NULL,
    `location` VARCHAR(100) NOT NULL,
    `year` YEAR NOT NULL,
    PRIMARY KEY(`id`)
)
;

CREATE TABLE `companies` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `industry` ENUM('Technology', 'Education', 'Business') NOT NULL,
    `location` VARCHAR(100) NOT NULL,
    PRIMARY KEY(`id`)
)
;

CREATE TABLE `connections` (
    `id` INT AUTO_INCREMENT,
    `school_and_university_start_date` DATE NOT NULL,
    `school_and_university_end_date` DATE,
    `school_and_university_degree` VARCHAR(5) NOT NULL,
    `company_start_date` DATE NOT NULL,
    `company_end_date` DATE,
    `user_id` INT,
    `to_user_id` INT,
    `to_school_and_university_id` INT,
    `to_company_id` INT,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`to_user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`to_school_and_university_id`) REFERENCES `schools_and_universities`(`id`),
    FOREIGN KEY(`to_company_id`) REFERENCES `companies`(`id`)
)
;
