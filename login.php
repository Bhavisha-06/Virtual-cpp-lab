<?php
// login.php

// Assuming you've validated and sanitized the input data from the form
$institute = $_POST['institute'];
$name = $_POST['name'];
$registration_number = $_POST['registration_number'];
$department = $_POST['department'];

// Connect to your MySQL database (replace these variables with your actual database credentials)
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "data";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Prepare SQL statement to insert login information into the logins table
$sql = "INSERT INTO logins (institute, name, registration_number, department) VALUES (?, ?, ?, ?)";
$stmt = $conn->prepare($sql);

// Bind parameters and execute the statement
$stmt->bind_param("ssss", $institute, $name, $registration_number, $department);
$stmt->execute();

// Close the statement and database connection
$stmt->close();
$conn->close();

// Redirect the user to the dashboard or home page after successful login
header("Location: dashboard.php");
exit();
?>
