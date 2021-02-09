package com.helio.app.ui.scheduling;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;
import androidx.lifecycle.ViewModelProvider;

import com.helio.app.R;
import com.helio.app.ui.settings.SingleBlindSettingsFragment;

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
                Fragment childFragment = new SingleBlindSettingsFragment();
                FragmentTransaction transaction = getChildFragmentManager().beginTransaction();
                transaction.replace(R.id.child_fragment_container, childFragment).commit();
            }
        });


        return returnView;
    }


}