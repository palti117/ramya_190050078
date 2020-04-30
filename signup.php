<!DOCTYPE html>
<html>
<head>
    <title>SignUp | YourBrick</title>
    <link rel="stylesheet" type="text/css" href="style3.css">
</head>
<body>
    <div class="info">
        <h1 class="center coral" id="main"><strong>YOURBRICK.com</strong></h1>
        <h2 class="center coral">Build your bricks for future!</h2>
    </div>
    <div class="loginbox">
    <img src="avatar2.png" class="avatar">
        <h1>SignUp Here!</h1>
        <form method="POST" action="">
            <p>Username</p>
            <input type="text" name="user" placeholder ="Enter Username" required>
            <p>Password</p>
            <input type="password" name="pass" placeholder="Enter Password" required>
            <!--<p>email</p>
            <input type="email" name="mail" required>-->
            <input type="submit" name="" value="SignUp">
        </form>
    </div>
    <?php  
    if(isset($_POST["submit"])){  
        if(!empty($_POST['user']) && !empty($_POST['pass'])) {  
            $user=$_POST['user'];  
            $pass=$_POST['pass'];  
            $con=mysqli_connect('localhost:3306','root','') or die(mysqli_error());  
            mysqli_select_db('users') or die("cannot select DB");  
            $query=mysqli_query("SELECT * FROM login WHERE username='".$user."'");  
            $numrows=mysqli_num_rows($query);  
            if($numrows==0){  
                $sql="INSERT INTO login(username,password) VALUES('$user','$pass')";  
                $result=mysqli_query($con,$sql);  
                if($result){ 
                    header("Location:log.html"); 
                } 
                else {  
                    echo "Failure!";  
                }  
          
            }
            else {  
                echo "That username already exists! Please try again with another.";  
            }  
          
        }
        else {  
            echo "All fields are required!";  
        }  
    }  
    ?>  
</body>  
</html>  