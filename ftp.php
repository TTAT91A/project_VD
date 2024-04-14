<?php
// Secure PHP script that allows file upload via SFTP

// SFTP server settings
$sftp_server = "example.com";
$sftp_port = 22; // Default port for SFTP is 22
$sftp_username = "username";
$sftp_password = "password";

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["file"])) {
    // Get the uploaded file details
    $file_name = $_FILES["file"]["name"];
    $file_tmp = $_FILES["file"]["tmp_name"];

    // Establish SSH connection
    $connection = ssh2_connect($sftp_server, $sftp_port);
    if ($connection) {
        // Authenticate using password
        if (ssh2_auth_password($connection, $sftp_username, $sftp_password)) {
            // Initialize SFTP subsystem
            $sftp = ssh2_sftp($connection);
            if ($sftp) {
                // Specify remote file path
                $remote_file_path = "uploads/" . $file_name;
                
                // Upload the file
                if (ssh2_scp_send($connection, $file_tmp, $remote_file_path, 0644)) {
                    echo "File uploaded successfully!";
                } else {
                    echo "Failed to upload file.";
                }
            } else {
                echo "Failed to initialize SFTP subsystem.";
            }
        } else {
            echo "Authentication failed.";
        }

        // Close SSH connection
        ssh2_disconnect($connection);
    } else {
        echo "Failed to establish SSH connection.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>File Upload via SFTP</title>
</head>
<body>
    <h2>Upload a file via SFTP</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
</body>
</html>