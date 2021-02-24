package com.helio.app.ui.blind;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.helio.app.R;
import com.helio.app.UserDataViewModel;
import com.helio.app.model.Motor;

import java.util.ArrayList;

public class SingleBlindSettingsFragment extends Fragment {

    private Motor motor;
    private UserDataViewModel model;

    private void setActionListeners(View view) {
        view.findViewById(R.id.btn_open).setOnClickListener(v -> {
            System.out.println("OPEN BUTTON PRESSED FOR " + model.getCurrentMotor());
            model.moveCurrentMotor(0);
        });
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View returnView = inflater.inflate(R.layout.fragment_single_blind_settings, container, false);
        assert getArguments() != null;
        int motorId = getArguments().getInt("currentMotorId");

        model = new ViewModelProvider(requireActivity()).get(UserDataViewModel.class);
        model.setCurrentMotor(motorId);
        model.fetchMotors().observe(
                getViewLifecycleOwner(),
                motors -> {
                    motor = motors.get(motorId);
                }
        );
        setActionListeners(returnView);
        return returnView;
    }

}