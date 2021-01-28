package com.helio.app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class AddScheduleActivity extends AppCompatActivity {

    private Button mBtnButton1;
    private Button mBtnButton2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_schedule);

        //To activate the "Set opening time" button
        mBtnButton1 = (Button) findViewById(R.id.btn_SetOpeningTime);
        mBtnButton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //jump to AddScheduleOpenActivity.class
                Intent intent = new Intent(AddScheduleActivity.this, AddScheduleOpenActivity.class);
                startActivity(intent);
            }
        });

        //To activate the "Set closing time" button
        mBtnButton2 = (Button) findViewById(R.id.btn_SetClosingTime);
        mBtnButton2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //jump to AddScheduleCloseActivity.class
                Intent intent = new Intent(AddScheduleActivity.this, AddScheduleCloseActivity.class);
                startActivity(intent);
            }
        });


    }
}