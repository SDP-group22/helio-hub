package com.helio.app.ui.blinds;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.helio.app.R;
import com.helio.app.model.Motor;
import com.helio.app.ui.MotorIcon;

import java.util.ArrayList;

public class BlindsSettingsFragment extends Fragment {
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_blinds_settings, container, false);

        // Prepare the list of motors TODO (temporary)
        ArrayList<Motor> motors = new ArrayList<>();
        motors.add(new Motor("Bedroom", MotorIcon.BEDROOM));
        motors.add(new Motor("Kitchen", MotorIcon.KITCHEN));
        motors.add(new Motor("Next to TV", MotorIcon.TV));
        motors.add(new Motor("Living room", MotorIcon.HOUSE));

        // Setup the adapter with the motors
        BlindsRecViewAdapter adapter = new BlindsRecViewAdapter(getContext());
        adapter.setMotors(motors);

        // Insert into the recycler view
        RecyclerView recView = view.findViewById(R.id.blindsRCView);
        recView.setAdapter(adapter);
        recView.setLayoutManager(new LinearLayoutManager(getContext()));
        return view;
    }
}
