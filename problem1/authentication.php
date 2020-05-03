<!DOCTYPE html>
<html>
<head>
    <title>YourBrick | Welcome</title>
    <link rel="stylesheet" type="text/css" href="style4.css">
</head>
<body>
<?php      
    include('connection.php');  
    $username = $_POST['user'];  
    $password = $_POST['pass'];  
      
        //to prevent from mysqli injection  
        $username = stripcslashes($username);  
        $password = stripcslashes($password);  
        $username = mysqli_real_escape_string($con, $username);  
        $password = mysqli_real_escape_string($con, $password);  
      
        $sql = "select *from login where username = '$username' and password = '$password'";  
        $result = mysqli_query($con, $sql);   
        $count = mysqli_num_rows($result);  
          
        if($count == 1){  
            echo "<h1><center> Login successful </center></h1>"; 

        } 
        else{  
            echo "<h1> <center>Login failed. Invalid username or password.</h1>";  
        }     
?>
</body>
</html>
