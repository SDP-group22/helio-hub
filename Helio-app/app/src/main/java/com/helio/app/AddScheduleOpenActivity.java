package com.helio.app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class AddScheduleOpenActivity extends AppCompatActivity {
    private Button mBtnSubmit;
    private Button mBtnBack;
    private EditText mEtHour;
    private EditText mEtMinute;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_schedule_open);

        //To activate the "submit" button
        mBtnSubmit = (Button) findViewById(R.id.btn_submit);
        mBtnSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //Toast
                Toast.makeText(AddScheduleOpenActivity.this,"Submited!",Toast.LENGTH_SHORT).show();
            }
        });

        //To activate the "back to add schedule" button
        mBtnBack = (Button) findViewById(R.id.btn_back);
        mBtnBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //jump back to AddScheduleCloseActivity.class
                Intent intent = new Intent(AddScheduleOpenActivity.this, AddScheduleActivity.class);
                startActivity(intent);
            }
        });

        //Record the input number for et_hour
        mEtHour = (EditText) findViewById(R.id.et_hour);
        mEtHour.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        //Record the input number for et_minute
        mEtMinute = (EditText) findViewById(R.id.et_minute);
        mEtMinute.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });




    }
}