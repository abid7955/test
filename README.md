# test
 Deployment Test by Commvault for SRE Role (Progress done till Mileston 2)
 Link: http://16.170.228.144:5000/

 Task: cloud-based Image management application using Amazon Web Services (AWS) and Python.

 ### Result/Progress: 
 Creation of EC2 Instance using boto3
 On running the file create ec-2.py, a new instance is created

 ![image](https://github.com/user-attachments/assets/1abecc24-1a21-431e-84da-c20d14f0d801)

 And if we check the AWS management console, we can see that the instance has been created with a public IP as well.

![image](https://github.com/user-attachments/assets/c641fa4b-b7d4-4af9-a596-a615fec288e1)

Ui of the website:
![image](https://github.com/user-attachments/assets/6c5872bd-787a-46bc-9496-7956c8fda1ff)

After choosing a file from the system, you get an option whether you'd like to encrypt that image or not

![image](https://github.com/user-attachments/assets/d22698b3-9156-482b-bbfa-cf52df41a4a6)

On successful upload, you will receive a notification
![image](https://github.com/user-attachments/assets/7ecf61fd-5b1e-4b1b-89df-0748cb3dbe95)

If you want to look at a list of all the uploaded images you can click on the option to redirect to different page

![image](https://github.com/user-attachments/assets/56bf5e8e-388e-4308-8398-2f34132ef5de)

As you can see, you get a list of the images you have uploaded along with an option to download it

And at the same time these files are visible in S3 bucket as well
![image](https://github.com/user-attachments/assets/f3ee42bb-48d0-409b-9c7a-4bf53a17ef91)
![image](https://github.com/user-attachments/assets/6e70877b-46c7-4bb2-859a-ab12725ceb42)

You can even use the filter to take a look at only encrypted images
![image](https://github.com/user-attachments/assets/3b6ebfc1-14fd-43bc-ae50-6eabc6c37ebc)





