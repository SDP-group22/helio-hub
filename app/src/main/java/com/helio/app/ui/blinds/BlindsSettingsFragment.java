package com.helio.app.ui.blinds;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.helio.app.Blinds;
import com.helio.app.R;
import com.helio.app.ui.MotorIcon;

import java.util.ArrayList;

public class BlindsSettingsFragment extends Fragment {
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_blinds_settings, container, false);

        // Prepare the list of motors TODO (temporary)
        ArrayList<Blinds> blinds = new ArrayList<>();
        blinds.add(new Blinds("Bedroom", MotorIcon.BEDROOM));
        blinds.add(new Blinds("Kitchen", MotorIcon.KITCHEN));
        blinds.add(new Blinds("Next to TV", MotorIcon.TV));
        blinds.add(new Blinds("Living room", MotorIcon.HOUSE));

        // Setup the adapter with the motors
        BlindsRecViewAdapter adapter = new BlindsRecViewAdapter(getContext());
        adapter.setBlinds(blinds);

        // Insert into the recycler view
        RecyclerView recView = view.findViewById(R.id.blindsRCView);
        recView.setAdapter(adapter);
        recView.setLayoutManager(new LinearLayoutManager(getContext()));
        return view;
    }
}
