package com.helio.app.ui.schedule;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.helio.app.AddScheduleCloseActivity;
import com.helio.app.AddScheduleOpenActivity;
import com.helio.app.R;

public class ScheduleFragment extends Fragment {

    private ScheduleViewModel scheduleViewModel;

    private Button btnChangeOpening;
    private Button btnChangeClosing;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        scheduleViewModel =
                new ViewModelProvider(this).get(ScheduleViewModel.class);
        View v = inflater.inflate(R.layout.fragment_schedule, container, false);

        // To activate the "Set opening time" button
        btnChangeOpening = v.findViewById(R.id.btn_SetOpeningTime);
        btnChangeOpening.setOnClickListener(v1 -> {
            // jump to AddScheduleOpenActivity.class
            Intent intent = new Intent(getActivity(), AddScheduleOpenActivity.class);
            startActivity(intent);
        });

        // To activate the "Set closing time" button
        btnChangeClosing = v.findViewById(R.id.btn_SetClosingTime);
        btnChangeClosing.setOnClickListener(v1 -> {
            // jump to AddScheduleCloseActivity.class
            Intent intent = new Intent(getActivity(), AddScheduleCloseActivity.class);
            startActivity(intent);
        });

        return v;
    }
}