package com.example.blog.util;

import java.time.LocalDateTime;

public class GetDateTime {
    public static String getTime(){
        LocalDateTime dateTime=LocalDateTime.now(); 
        String date = dateTime.toString().substring(0,10);
        String time= dateTime.toString().substring(11,19);
        String currentDate=date+" "+time;
        return currentDate;
    }
}
