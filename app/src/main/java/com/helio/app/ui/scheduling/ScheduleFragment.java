package com.helio.app.ui.scheduling;

import android.app.TimePickerDialog;
import android.content.Intent;
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
import androidx.fragment.app.FragmentTransaction;
import androidx.lifecycle.ViewModelProvider;

import com.helio.app.MainActivity;
import com.helio.app.R;
import com.helio.app.ui.SettingsFragment;

import java.util.Calendar;

public class ScheduleFragment extends Fragment {

    private ScheduleViewModel scheduleViewModel;

    private Button setting;


    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        scheduleViewModel =
                new ViewModelProvider(this).get(ScheduleViewModel.class);
        View returnView = inflater.inflate(R.layout.fragment_schedule, container, false);


        setting = returnView.findViewById(R.id.btn_setting);
        setting.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Fragment childFragment = new SettingsFragment();
                FragmentTransaction transaction = getChildFragmentManager().beginTransaction();
                transaction.replace(R.id.child_fragment_container, childFragment).commit();
            }
        });


        return returnView;
    }


}