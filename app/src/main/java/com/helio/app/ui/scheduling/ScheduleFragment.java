package com.helio.app.ui.scheduling;

import android.app.TimePickerDialog;
import android.os.Bundle;
import android.os.Handler;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TimePicker;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.helio.app.R;

import java.util.Calendar;

public class ScheduleFragment extends Fragment {

    private ScheduleViewModel scheduleViewModel;


    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        scheduleViewModel =
                new ViewModelProvider(this).get(ScheduleViewModel.class);
        View returnView = inflater.inflate(R.layout.fragment_schedule, container, false);



        return returnView;
    }
}