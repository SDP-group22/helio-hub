package com.helio.app;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class AddScheduleOpenActivity extends AppCompatActivity {
    private Button mBtnSubmit;
    private Button mBtnBack;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_schedule_open);

        //To activate the "submit" button
        mBtnSubmit = findViewById(R.id.btn_submit);
        mBtnSubmit.setOnClickListener(v -> {
            // Display toast to screen
            Toast.makeText(AddScheduleOpenActivity.this, R.string.set_time_message, Toast.LENGTH_SHORT).show();
        });

        //To activate the "back to add schedule" button
        mBtnBack = findViewById(R.id.btn_back);
        mBtnBack.setOnClickListener(v -> {
            // jump back to AddScheduleCloseActivity.class
            Intent intent = new Intent(AddScheduleOpenActivity.this, MainActivity.class);
            startActivity(intent);
        });
    }
}