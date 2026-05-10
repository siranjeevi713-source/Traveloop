-- Traveloop Database Schema

CREATE DATABASE IF NOT EXISTS traveloop;
USE traveloop;

-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    profile_image VARCHAR(255) DEFAULT 'default_avatar.png',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    role ENUM('user', 'admin') DEFAULT 'user'
);

-- Trips Table
CREATE TABLE trips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    cover_image VARCHAR(255),
    status ENUM('upcoming', 'completed', 'draft') DEFAULT 'draft',
    budget_limit DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Destinations Table
CREATE TABLE destinations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100),
    order_index INT DEFAULT 0,
    arrival_date DATE,
    departure_date DATE,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- Itinerary Days Table
CREATE TABLE itinerary_days (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    day_number INT NOT NULL,
    date DATE,
    notes TEXT,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- Itinerary Activities Table
CREATE TABLE itinerary_activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    day_id INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    time_start TIME,
    time_end TIME,
    location VARCHAR(255),
    estimated_cost DECIMAL(10, 2) DEFAULT 0.00,
    activity_type ENUM('adventure', 'sightseeing', 'food', 'nightlife', 'trekking', 'cultural', 'other') DEFAULT 'other',
    FOREIGN KEY (day_id) REFERENCES itinerary_days(id) ON DELETE CASCADE
);

-- Expenses Table
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    category ENUM('hotel', 'transport', 'food', 'shopping', 'activities', 'emergency', 'other') DEFAULT 'other',
    amount DECIMAL(10, 2) NOT NULL,
    description VARCHAR(255),
    expense_date DATE,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- Packing Lists Table
CREATE TABLE packing_lists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    category ENUM('Clothes', 'Electronics', 'Documents', 'Medicines', 'Essentials', 'Other') DEFAULT 'Other',
    is_packed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- Notes Table
CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    trip_id INT,
    title VARCHAR(150) NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE SET NULL
);

-- Shared Trips Table
CREATE TABLE shared_trips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    shared_by INT NOT NULL,
    share_token VARCHAR(255) UNIQUE NOT NULL,
    is_public BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE,
    FOREIGN KEY (shared_by) REFERENCES users(id) ON DELETE CASCADE
);

-- Global Activities/Recommendations Table
CREATE TABLE activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    category ENUM('adventure', 'sightseeing', 'food', 'nightlife', 'trekking', 'cultural') NOT NULL,
    location VARCHAR(255),
    image_url VARCHAR(255),
    rating DECIMAL(2, 1),
    estimated_cost DECIMAL(10, 2)
);

-- Notifications Table
CREATE TABLE notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
